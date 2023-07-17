#Importing python modules
import os
from connect import *
import json
import System.Drawing
import datetime

# Importing local files:
from dicom_import import Import
from get_and_set_arguments_from_function import set_function_arguments

def import_and_set_parameters(initials, importfolder, patient, case):
    """
    Function that imports examinations, plans and doses to new case and sets isodose colortable, examination names,
    optimization objectives, clinical goals and plan CT names to generate a copied case.
    :param initials: str
    :param importfolder: str
    :param patient: RayStation PyScriptObject
    :param case: RayStation PyScriptObject
    :return: None
    """
    Import(initials, importfolder, patient, case)

    """
    If there is a Case 1 and Case 3, the new case will be called Case 2, so it is not correct to assume that case 3 is 
    the newest case with the  retrieve the case with the imported plans and doses.
    Instead, we retrieve the date and time for the case that was last modified and update it.
    """

    patient_db = get_current("PatientDB")
    patient_info = patient_db.QueryPatientInfo(Filter={"PatientID":patient.PatientID, "LastName":patient.Name.split("^")[-1]})
    case_info = patient_db.QueryCaseInfo(PatientInfo=patient_info[0])

    datetimes = []
    for case in case_info:
        datetimes.append(case["LastModified"])

    """
    The range(len(lst)) generates a sequence of indices from 0 to len(lst)-1. 
    The key=lst.__getitem__ specifies that the comparison should be based on the 
    values in the list rather than the indices. It does the same as numpy.argmax
    """

    most_current_idx = max(range(len(datetimes)), key=datetimes.__getitem__)
    most_current_case = case_info[most_current_idx]["Name"]

    print("The most currently modified case is {}".format(most_current_case))

    case = patient.Cases[most_current_case]

    ColorTable = json.load(open(os.path.join(importfolder, '{}_ColorTable.json'.format(initials))))

    new_ColorTable = {}

    #Generating System.Drawing.Color objects from the ColorTable file
    for rel_dose in ColorTable:
        new_ColorTable[float(rel_dose)] = System.Drawing.Color.FromArgb(
            ColorTable[rel_dose][0], ColorTable[rel_dose][1], ColorTable[rel_dose][2], ColorTable[rel_dose][3]
        )

    #Updating colortable to match the original case
    case.CaseSettings.DoseColorMap.ColorTable = new_ColorTable
    case.CaseSettings.DoseColorMap.PresentationType = "Absolute"

    examination_names = json.load(open(os.path.join(importfolder, '{}_StudyNames.json'.format(initials))))

    #Updating examination names
    for examination in case.Examinations:
        examination.Name = examination_names[examination.Series[0].ImportedDicomUID]

    for plan in case.TreatmentPlans:
        print(plan.Name)

        #I dont think we need to do this so ignore for now
        """Only way to see which CT study a plan is connected to is to go into the scripting object 
        plan.BeamSets[0].FractionDose.OnDensity.FromExamination.Name. OnDensity is empty after importing the plans
        so I had to save the plan and the corresponding CT study name in a json file.

        planning_CTs = json.load(open(os.path.join(importfolder, '{}_{}_planningCTs.json'.format(initials, plan.Name))))

        First the correct CT study used for the radiation plan is extracted from case.Examinations[planning_CTs[plan.Name]]
        Then the correct structureset is extracted using the name of this examination
        #plan_examination = case.Examinations[planning_CTs[plan.Name]]
        #plan_structureset = case.PatientModel.StructureSets[plan_examination.Name]"""


        #Changing the name of the beamset back to its original name
        plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace("U", ":")

        # Loading file with optimization objectives
        arguments = json.load(open(os.path.join(importfolder, '{}_{}_objectives.json'.format(initials, plan.Name))))

        PlanOptimization_new = plan.PlanOptimizations[0]

        # Adding optimization functions from the original plan for each ROI
        for arg_dict in arguments:
            with CompositeAction('Add Optimization Function'):
                try:
                    f = PlanOptimization_new.AddOptimizationFunction(FunctionType=arg_dict['FunctionType'],
                                                                     RoiName=arg_dict['RoiName'],
                                                                     IsConstraint=arg_dict['IsConstraint'],
                                                                     IsRobust=arg_dict['IsRobust']
                                                                  )
                    set_function_arguments(f, arg_dict)

                except:
                    print("Could not set objective for ROI {} ".format(arg_dict["RoiName"]))


        #Adding clinical goals
        clinical_goals = json.load(open(os.path.join(importfolder,
                                                     '{}_{}_ClinicalGoals.json'.format(initials, plan.Name)), 'r'
                                        )
                                   )

        eval_setup = plan.TreatmentCourse.EvaluationSetup
        for i in clinical_goals:
            # Clinical goal settings  RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority
            RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority = clinical_goals[i]
            eval_setup.AddClinicalGoal(RoiName=RoiName,
                                       GoalCriteria=Goalriteria,
                                       GoalType=GoalType,
                                       AcceptanceLevel=AcceptanceLevel,
                                       ParameterValue=ParameterValue,
                                       Priority=Priority
                                       )
    patient.Save()

    pass