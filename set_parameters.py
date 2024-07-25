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


class SET:
    def __init__(self, Progress, initials, importfolder, patient, case):
        self.Progress = Progress
        self.initials = initials
        self.importfolder = importfolder
        self.patient = patient
        self.case = case

        self.set_parameters_func()

    def set_parameters_func(self):
        # TODO: Håndter kopier til case. Kanskje med en parameter som lagres?

        """
        Function that imports examinations, plans and doses to new case and sets isodose colortable, examination names,
        optimization objectives, clinical goals and plan CT names to generate a copied case.
        :param initials: str
        :param importfolder: str
        :param patient: RayStation PyScriptObject
        :param case: RayStation PyScriptObject
        :return: None
        """

        self._load_case_and_parameters()

        # Pass på at dette funker
        confirm = tk.Toplevel()
        # TODO: If the user cancels, make a new popup that asks which case should be modified
        app = ConfirmCase(confirm, self.case.CaseName)

        self._set_ColorTable()

        self._set_examination_names()

        # Generating roi algebra for derived rois
        self.Progress.update_operation("Oppdatererer derived rois")

        # This works only when the structureset is not approved
        self.error = generate_roi_algebra(self.case, self.derived_rois_dict, self.derived_rois_status, self.planningCT_names, self.Progress)


        self._set_plan_parameters()


    def _extract_number(self, string):
        try:
            return int(string.split()[-1])
        except ValueError:
            return float('inf')  # Put non-numeric values at the end

    def _load_case_and_parameters(self):
        case_parameters = json.load(open(os.path.join(self.importfolder, '{}_case_parameters.json'.format(self.initials))))
        self.ColorTable = case_parameters.get("ColorTable")
        self.copy_to_case = case_parameters.get("copy to case")
        self.examination_names = case_parameters.get("ExaminationNames")
        self.derived_rois_dict = case_parameters.get("derived rois dict")
        self.clinical_goals = case_parameters.get("ClinicalGoals")
        self.objectives = case_parameters.get("Objectives")
        self.derived_rois_status = case_parameters.get("derived rois status")
        self.isocenter_names = case_parameters.get("isocenter names")
        self.planningCT_names = case_parameters.get("planning CTs")
        self.imported_examination_names = case_parameters.get("ExaminationNames")

        print(self.copy_to_case)

        if self.copy_to_case:
            case = copy_to_case
        else:
            case = self._find_most_current_case()

        # loading case we want to set parameters on, if its not already loaded
        if self.case.CaseName != case.CaseName:
            # setting self case to newest case
            self.case = case
            # saving before changing case
            self.patient.Save()
            self.case.SetCurrent()


    def _find_most_current_case(self):
        """
                If there is a Case 1 and Case 3, the new case will be called Case 2, so it is not correct to assume that case 3 is
                the newest case with the  retrieve the case with the imported plans and doses.
                Instead, we retrieve the date and time for the case that was last modified and update it.
                """
        patient_db = get_current("PatientDB")
        patient_info = patient_db.QueryPatientInfo(
            Filter={"PatientID": self.patient.PatientID, "LastName": self.patient.Name.split("^")[0]})

        assert len(patient_info) > 0, "Patient info is empty"

        case_info = patient_db.QueryCaseInfo(PatientInfo=patient_info[0])

        datetimes = []
        for c in case_info:
            datetimes.append(c["LastModified"])

        """
        The range(len(lst)) generates a sequence of indices from 0 to len(lst)-1. 
        The key=lst.__getitem__ specifies that the comparison should be based on the 
        values in the list rather than the indices. It does the same as numpy.argmax
        """

        most_current_idx = max(range(len(datetimes)), key=datetimes.__getitem__)
        most_current_case = case_info[most_current_idx]["Name"]

        print(most_current_case)

        case = self.patient.Cases[most_current_case]
        print("The most currently modified case is {}".format(case.CaseName))

        if "Kopiert Case" in case.CaseName:
            # If we are already on a copied case we should not change its name
            pass
        else:
            # Changing name to documentation, because the original case should be the one to change
            copied_cases = [c.CaseName for c in self.patient.Cases if "Kopiert Case" in c.CaseName]

            # If the patient has copied cases
            # TODO: Bruk regex her?
            if len(copied_cases) > 0:
                # copied_cases[-1] gir den siste kopierte casen. [-1] gir tallet i kopiert case x.
                case.CaseName = "Kopiert Case {}".format(
                    int(copied_cases[-1][-1]) + 1)
            else:
                case.CaseName = "Kopiert Case 1"

        return case

    def _set_ColorTable(self):

        new_ColorTable = {}

        # Generating System.Drawing.Color objects from the ColorTable file
        for rel_dose in self.ColorTable:
            new_ColorTable[float(rel_dose)] = System.Drawing.Color.FromArgb(
                self.ColorTable[rel_dose][0], self.ColorTable[rel_dose][1], self.ColorTable[rel_dose][2], self.ColorTable[rel_dose][3]
            )

        # Updating colortable to match the original case
        self.case.CaseSettings.DoseColorMap.ColorTable = new_ColorTable
        self.case.CaseSettings.DoseColorMap.PresentationType = "Absolute"

    def _set_examination_names(self):
        # Updating examination names
        self.Progress.update_operation("Setter korrekt bildenavn")
        lung_examinations = []
        # first setting all names to end with tmp to ensure that we avoid duplicates which cause errors (e.g. CT 1 needs to be called CT 2),
        # but there is already a CT 2 which havent gotten its name yet
        for i, ex in enumerate(self.case.Examinations):
            # Changing prog to account for both adding tmp to exam names, then removing tmp
            prog = round(((i + 1) / (2 * len(self.case.Examinations))) * 100, 0)
            self.Progress.update_progress(prog)
            ex.Name = self.imported_examination_names[ex.Series[0].ImportedDicomUID] + "tmp"
        for i, ex in enumerate(self.case.Examinations):
            prog = round(50 + ((i + 1) / (2 * len(self.case.Examinations))) * 100, 0)
            self.Progress.update_progress(prog)
            ex.Name = self.imported_examination_names[ex.Series[0].ImportedDicomUID]
            #if "lung" in ex.GetProtocolName().lower():
            #lung_examinations.append(ex.Name)
        # if lung is in protocolname we might have a 4DCT
        if any(("lunge" in e.GetProtocolName().lower() for e in self.case.Examinations if e.GetProtocolName())):
            self._handle_lung_examinations()


    def _handle_lung_examinations(self):
        """This function takes examinations that contain "Lunge" in their protocol name, and checks whether or not they are part of a 4D ct group"""
        lung_examinations = [examination for examination in self.case.Examinations
                             if "lunge" in examination.GetProtocolName().lower()]
        fourDCT = []
        for i, ex in enumerate(lung_examinations):
            data = ex.GetAcquisitionDataFromDicom()
            # Need this in case of multiple 4DCT
            # average CTs also contain 4DCT, but only 4DCT examinations contains %
            if "4DCT" in data["SeriesModule"]["SeriesDescription"] and "%" in data["SeriesModule"][
                "SeriesDescription"]:
                fourDCT.append(ex.Name)

        # if the protocol name of the examination contains lunge, but there are no 4DCTs, we dont try to generate 4DCT group
        if not len(fourDCT) > 0:
            return

        # we sort the 4DCT examination list based on the breathing phase number (10%,20% etc.)
        fourDCT = sorted(fourDCT, key=self._extract_number)
        print("fourDCT")
        print(fourDCT)
        # In case of multiple 4DCTs, we get unique frame of references
        unique_FORs = []
        # Access the frame of reference of the 4DCT CT studies
        FORs = [self.case.Examinations[ct].EquipmentInfo.FrameOfReference for ct in fourDCT]
        # Find unique FOR
        for FOR in FORs:
            if FOR not in unique_FORs:
                unique_FORs.append(FOR)
        #unique_FORs.extend(FOR for FOR in FORs if FOR not in unique_FORs)
        print("Unique Frame of reference registrations")
        try:
            if unique_FORs:
                # Iterating over the unique FOR and making one 4DCT per FOR
                for i, FOR in enumerate(unique_FORs):
                    ct_group = [ct for ct in fourDCT if FOR == self.case.Examinations[ct].EquipmentInfo.FrameOfReference]
                    self.case.CreateExaminationGroup(ExaminationGroupName="4DCT {}".format(i),
                                                ExaminationGroupType="Collection4dct",
                                                ExaminationNames=ct_group)

            else:
                self.case.CreateExaminationGroup(ExaminationGroupName="4DCT",
                                            ExaminationGroupType="Collection4dct",
                                            ExaminationNames=fourDCT)
        except:
            # TODO: errormessage

    def _set_plan_parameters(self):
        CopyPlanName = []
        for i, plan in enumerate(self.case.TreatmentPlans):

            print(plan)

            # For some reason, if a plan copy is generated within the loop it appears in case. TreatmentPlans in the next iteration
            # So we skip it if it appears
            try:
                if plan.Name in CopyPlanName:
                    continue
            except:
                self.Progress.update_plan("Plan {}/{}".format(i + 1, len(self.case.TreatmentPlans)))
                pass

            original_plan_name = plan.Name

            # If plan has copy in
            if plan.Review:
                if plan.Review.ApprovalStatus == "Approved":
                    copyname = "{} Copy".format(plan.Name)
                    CopyPlanName.append(copyname)
                    if copyname not in [p.Name for p in self.case.TreatmentPlans]:
                        self.case.CopyPlan(PlanName=plan.Name, NewPlanName="{} Copy".format(plan.Name),
                                      KeepBeamSetNames=True)
                        plan = self.case.TreatmentPlans["{} Copy".format(plan.Name)]
                        plan_filename = original_plan_name.replace("/", "Y").replace(":", "X")
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

            # print("Plan filename")
            # print(plan_filename)

            PlanOptimization_new = plan.PlanOptimizations[0]

            self.Progress.update_operation("Legger til Optimization Objectives")

            # Adding optimization functions from the original plan for each ROI
            for j, arg_dict in enumerate(self.objectives):
                prog = round(((j + 1) / len(self.objectives)) * 100, 0)
                self.Progress.update_progress(prog)

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

            self.Progress.update_operation("Legger til Clinical Goals")

            eval_setup = plan.TreatmentCourse.EvaluationSetup
            for k, goal in enumerate(self.clinical_goals):
                prog = round(((k + 1) / len(self.clinical_goals)) * 100, 0)
                self.Progress.update_progress(prog)
                # Clinical goal settings  RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority
                RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority = self.clinical_goals[goal]
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
        self.Progress.quit()
        self.patient.Save()