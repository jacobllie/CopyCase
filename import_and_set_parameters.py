#Importing python modules
import os
import sys

from connect import *
import json
import System.Drawing
import datetime

# Importing local files:
from dicom_import import Import
from get_and_set_arguments_from_function import set_function_arguments

def extract_number(s):
    try:
        return int(s.split()[-1])
    except ValueError:
        return float('inf')  # Put non-numeric values at the end

def import_and_set_parameters(initials, importfolder, patient, case, import_files=True):
    """
    Function that imports examinations, plans and doses to new case and sets isodose colortable, examination names,
    optimization objectives, clinical goals and plan CT names to generate a copied case.
    :param initials: str
    :param importfolder: str
    :param patient: RayStation PyScriptObject
    :param case: RayStation PyScriptObject
    :return: None
    """

    if import_files:
        Import(importfolder, patient)

    """
    If there is a Case 1 and Case 3, the new case will be called Case 2, so it is not correct to assume that case 3 is 
    the newest case with the  retrieve the case with the imported plans and doses.
    Instead, we retrieve the date and time for the case that was last modified and update it.
    """

    patient_db = get_current("PatientDB")
    patient_info = patient_db.QueryPatientInfo(Filter={"PatientID":patient.PatientID, "LastName":patient.Name.split("^")[0]})

    assert len(patient_info) > 0, "Patient info is empty"

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

    isocenter_names = json.load(open(os.path.join(importfolder, '{}_isocenter_names.json'.format(initials))))

    #Exam names of original case
    examination_names_imported = json.load(open(os.path.join(importfolder, '{}_StudyNames.json'.format(initials))))

    for examination in case.Examinations:
        try:
            if "lung" in examination.GetProtocolName().lower():
                lung = True
                fourDCT = []
        except:
            lung = False
            print("Examination {} does not have protocol name".format(examination))
        break

    # Updating examination names

    for i,ex in enumerate(case.Examinations):
        ex.Name = examination_names_imported[ex.Series[0].ImportedDicomUID] + "tmp"""
    for ex in case.Examinations:
        ex.Name = examination_names_imported[ex.Series[0].ImportedDicomUID]
        data = ex.GetAcquisitionDataFromDicom()
        print(data)
        if lung:
            if "4DCT" in data["SeriesModule"]["SeriesDescription"] and "%" in data["SeriesModule"]["SeriesDescription"]:
                fourDCT.append(ex.Name)
            if i == len(case.Examinations)-1:
                fourDCT = sorted(fourDCT, key=extract_number)
                print("fourDCT")
                print(fourDCT)
    if lung:
        try:
            case.CreateExaminationGroup(ExaminationGroupName="4DCT",
                                        ExaminationGroupType="Collection4dct",
                                        ExaminationNames=fourDCT)
        except:
            pass

    for plan in case.TreatmentPlans:
        # For some reason, if a plan copy is generated within the loop it appears in case.TreatmentPlans in the next iteration
        # So we skip it if it appears
        try:
            if plan.Name == CopyPlanName:
                continue
        except:
            pass

        original_plan_name = plan.Name
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


        if plan.Review:
            if plan.Review.ApprovalStatus == "Approved":
                CopyPlanName = "{} Copy".format(plan.Name)
                case.CopyPlan(PlanName=plan.Name, NewPlanName=CopyPlanName)
                plan = case.TreatmentPlans[CopyPlanName]
        else:
            # Does not work if there are multiple beamsets
            for beam in plan.BeamSets[0].Beams:
                beam.Isocenter.Annotation.Name = isocenter_names[plan.Name]
            # Changing the name of the beamset back to its original name.
            # This is only the case if an unapproved plan has been imported
            plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace("X", ":")
            plan.Name = plan.Name.replace("X", ":").replace("Y", "/")


        # Loading file with optimization objectives
        arguments = json.load(
            open(
                os.path.join(
                    importfolder,
                    "{}_{}_objectives.json".format(
                        initials, original_plan_name.replace("/", "V").replace(":", "V")
                    ),
                )
            )
        )

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
        clinical_goals = json.load(
            open(
                os.path.join(
                    importfolder,
                    "{}_{}_ClinicalGoals.json".format(
                        initials, original_plan_name.replace("/", "V").replace(":", "V")
                    ),
                ),
                "r",
            )
        )

        eval_setup = plan.TreatmentCourse.EvaluationSetup
        for i in clinical_goals:
            # Clinical goal settings  RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority
            RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority = clinical_goals[i]
            try:
                eval_setup.AddClinicalGoal(RoiName=RoiName,
                                           GoalCriteria=Goalriteria,
                                           GoalType=GoalType,
                                           AcceptanceLevel=AcceptanceLevel,
                                           ParameterValue=ParameterValue,
                                           Priority=Priority
                                           )
            except:
                pass

        try:
            plan.PlanOptimizations[0].EvaluateOptimizationFunctions()
        except:
            print("Could not compute objective functions")
    patient.Save()

    pass