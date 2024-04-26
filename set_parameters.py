#Importing python modules
import os
import sys

from connect import *
import json
import System.Drawing
import datetime
import tkinter as tk
from tkinter import ttk
import threading

# Importing local files:
from dicom_import import Import
from get_and_set_arguments_from_function import set_function_arguments
from GUI import ProgressBar, ConfirmCase, INFOBOX, ScrollBar
from utils import generate_roi_algebra


def extract_number(s):
    try:
        return int(s.split()[-1])
    except ValueError:
        return float('inf')  # Put non-numeric values at the end


def set_parameters_func(Progress, initials, importfolder, patient, case):
    """
    Function that imports examinations, plans and doses to new case and sets isodose colortable, examination names,
    optimization objectives, clinical goals and plan CT names to generate a copied case.
    :param initials: str
    :param importfolder: str
    :param patient: RayStation PyScriptObject
    :param case: RayStation PyScriptObject
    :return: None
    """

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

    if "Kopiert Case" in case.CaseName:
        # If we are already on a copied case we should not change its name
        pass
    else:
        # Changing name to documentation, because the original case should be the one to change
        copied_cases = [c.CaseName for c in patient.Cases if "Kopiert Case" in c.CaseName]

        # If the patient has copied cases
        # TODO: Bruk regex her
        if len(copied_cases) > 0:
            case.CaseName = "Kopiert Case {}".format(
                int(copied_cases[-1][-1])+1)
        else:
            case.CaseName = "Kopiert Case 1"

    # Pass på at dette funker
    confirm = tk.Toplevel()
    # TODO: If the user cancels, make a new popup that asks which case should be modified
    app = ConfirmCase(confirm, case.CaseName)
    #app = INFOBOX(confirm, "Confirm", "Er du sikker på at du vil sette parametere for case: {}".format(case.CaseName)
    #confirm.mainloop()

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

    #names of planning CTs
    planningCT_names = json.load(open(os.path.join(importfolder, '{}_planningCT_names.json'.format(initials))))

    #derived roi expressions
    derived_roi_dict = json.load(open(os.path.join(importfolder, '{}_derived_roi_dict.json'.format(initials))))

    try:
        #derived roi status
        derived_roi_status = json.load(open(os.path.join(importfolder, '{}_derived_roi_status.json'.format(initials))))
    except:
        print("No derived roi status, likely caused by not any ct studies having external geometry")
        derived_roi_status = None

    lung = None
    for i, examination in enumerate(case.Examinations):
        try:
            if "lung" in examination.GetProtocolName().lower():
                lung = True
                fourDCT = []
        except:
            lung = False
            print("Examination {} does not have protocol name".format(examination))
        break

    # Updating examination names
    Progress.update_operation("Setter korrekt bildenavn")
    for i,ex in enumerate(case.Examinations):
        # Changing prog to account for both adding tmp to exam names, then removing tmp
        prog = round(((i + 1) / (2*len(case.Examinations))) * 100, 0)
        Progress.update_progress(prog)
        ex.Name = examination_names_imported[ex.Series[0].ImportedDicomUID] + "tmp"
    for i,ex in enumerate(case.Examinations):
        prog = round(50 + ((i + 1) / (2*len(case.Examinations))) * 100, 0)
        Progress.update_progress(prog)
        ex.Name = examination_names_imported[ex.Series[0].ImportedDicomUID]
        data = ex.GetAcquisitionDataFromDicom()
        # Need this in case of multiple 4DCT
        unique_FOR = None
        if lung:
            if "4DCT" in data["SeriesModule"]["SeriesDescription"] and "%" in data["SeriesModule"]["SeriesDescription"]:
                fourDCT.append(ex.Name)
            if i == len(case.Examinations)-1:
                fourDCT = sorted(fourDCT, key=extract_number)
                print("fourDCT")
                print(fourDCT)
                # In case of multiple 4DCTs
                unique_FOR = []
                #Access the FOR of the 4DCT CT studies
                FORs = [case.Examinations[ct].EquipmentInfo.FrameOfReference for ct in fourDCT]
                # Find unique FOR
                unique_FOR.extend(FOR for FOR in FORs if FOR not in unique_FOR)
                print("Unique Frame of reference registrations")

    if lung:
        try:
            if unique_FOR:
                #Iterating over the unique FOR and making one 4DCT per FOR
                for i,FOR in enumerate(unique_FOR):
                    ct_group = [ct for ct in fourDCT if FOR == case.Examinations[ct].EquipmentInfo.FrameOfReference]
                    case.CreateExaminationGroup(ExaminationGroupName="4DCT {}".format(i),
                                                ExaminationGroupType="Collection4dct",
                                                ExaminationNames=ct_group)

            else:
                case.CreateExaminationGroup(ExaminationGroupName="4DCT",
                                            ExaminationGroupType="Collection4dct",
                                            ExaminationNames=fourDCT)
        except:
            pass

    # Generating roi algebra for derived rois
    Progress.update_operation("Oppdatererer derived rois")

    # This works only when the structureset is not approved
    roi_error = generate_roi_algebra(case, derived_roi_dict, derived_roi_status, planningCT_names, Progress)

    CopyPlanName = []
    for i, plan in enumerate(case.TreatmentPlans):

        print(plan)

        # For some reason, if a plan copy is generated within the loop it appears in case. TreatmentPlans in the next iteration
        # So we skip it if it appears
        try:
            if plan.Name in CopyPlanName:
                continue
        except:
            Progress.update_plan("Plan {}/{}".format(i + 1, len(case.TreatmentPlans)))
            pass

        original_plan_name = plan.Name
        #print(original_plan_name)

        #I dont think we need to do this so ignore for now
        """Only way to see which CT study a plan is connected to is to go into the scripting object 
        plan.BeamSets[0].FractionDose.OnDensity.FromExamination.Name. OnDensity is empty after importing the plans
        so I had to save the plan and the corresponding CT study name in a json file.

        planning_CTs = json.load(open(os.path.join(importfolder, '{}_{}_planningCTs.json'.format(initials, plan.Name))))

        First the correct CT study used for the radiation plan is extracted from case.Examinations[planning_CTs[plan.Name]]
        Then the correct structureset is extracted using the name of this examination
        #plan_examination = case.Examinations[planning_CTs[plan.Name]]
        #plan_structureset = case.PatientModel.StructureSets[plan_examination.Name]"""



        # If plan has copy in
        if plan.Review:
            if plan.Review.ApprovalStatus == "Approved":
                copyname = "{} Copy".format(plan.Name)
                CopyPlanName.append(copyname)
                if copyname not in [p.Name for p in case.TreatmentPlans]:
                    case.CopyPlan(PlanName=plan.Name, NewPlanName="{} Copy".format(plan.Name), KeepBeamSetNames=True)
                    plan = case.TreatmentPlans["{} Copy".format(plan.Name)]
                    plan_filename = original_plan_name.replace("/","Y").replace(":","X")
                else:
                    print("plan copy already exists")
                    continue

        else:
            # Need this to extract the correct file
            plan_filename = plan.Name
            print(plan_filename)

            # Changing the name of the beamset back to its original name.
            # This is only the case if an unapproved plan has been imported
            plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace("X", ":")
            plan.Name = plan.Name.replace("X", ":").replace("Y", "/")

            # Does not work if there are multiple beamsets
            # Changing name of isocenter if the doses are not considered clinical
            # NB. Removing consider imported dose as clinical check is not scriptable
            if not plan.TreatmentCourse.TotalDose.DoseValues.IsClinical:
                for beam in plan.BeamSets[0].Beams:
                    beam.Isocenter.Annotation.Name = isocenter_names[plan.Name]

        print("Here")

        #print("Plan Filename")
        #print(plan_filename)

        # Loading file with optimization objectives
        arguments = json.load(
            open(
                os.path.join(
                    importfolder,
                    "{}_{}_objectives.json".format(
                        initials, plan_filename
                    ),
                )
            )
        )

        #print("Plan filename")
        #print(plan_filename)


        PlanOptimization_new = plan.PlanOptimizations[0]

        Progress.update_operation("Legger til Optimization Objectives")

        # Adding optimization functions from the original plan for each ROI
        for j, arg_dict in enumerate(arguments):
            prog = round(((j+1) / len(arguments)) * 100, 0)
            Progress.update_progress(prog)

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

        """# Close progresswindow if we are on the last plan
        if i == len(case.TreatmentPlans)-1:
            Progress.quit()"""

        #Adding clinical goals
        clinical_goals = json.load(
            open(
                os.path.join(
                    importfolder,
                    "{}_{}_ClinicalGoals.json".format(
                        initials, plan_filename
                    ),
                ),
                "r",
            )
        )

        Progress.update_operation("Legger til Clinical Goals")

        eval_setup = plan.TreatmentCourse.EvaluationSetup
        for k, goal in enumerate(clinical_goals):
            prog = round(((k + 1) / len(clinical_goals)) * 100, 0)
            Progress.update_progress(prog)
            # Clinical goal settings  RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority
            RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority = clinical_goals[goal]
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

    # Quitting progresswindow
    Progress.quit()
    patient.Save()

    if roi_error != "":
        return roi_error

