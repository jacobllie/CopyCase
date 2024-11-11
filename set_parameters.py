#Importing python modules
import os
import sys

from connect import *
import json
import clr
# Implicit loading (just saying from System.Drawing import Color) is deprecated. We need to add System.Drawing as reference 
# whatever that
clr.AddReference("System.Drawing")
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


class Set:
    def __init__(self, Progress, case_parameters, importfolder):
        self.Progress = Progress
        self.case_parameters = case_parameters
        self.importfolder = importfolder

        self.set_parameters_func()

    def set_parameters_func(self):

        try:
            self.patient = get_current("Patient")
        except SystemError:
            raise IOError("No patient loaded.")
        try:
            self.case = get_current("Case")
        except SystemError:
            raise IOError("No case loaded.")

        """
        Function that imports examinations, plans and doses to new case and sets isodose colortable, examination names,
        optimization objectives, clinical goals and plan CT names to generate a copied case.
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

        if self.derived_rois_dict:
            # This works only when the structureset is not approved
            self.error = generate_roi_algebra(self.case, self.derived_rois_dict, self.derived_rois_status, self.planningCT_names, self.Progress)

        self._set_plan_parameters()



    def _load_case_and_parameters(self):
        # ColorTable {"30.0": [ 255, 64, 128, 128 ], ... relative dose as keys and RGB values in lists
        self.ColorTable = self.case_parameters.get("ColorTable")
        # Copy to case is simply a string with the name of the case we want to copy to, none otherwise
        self.copy_to_case = self.case_parameters.get("copy to case")
        # derived roi dict is a dictionary of all the derived roi expressions with all information necessary for correct
        # roi algebra
        self.derived_rois_dict = self.case_parameters.get("derived rois dict")
        # clinical goals contains a dictionary per plan with all the clinical goals indexed by numbers
        # "Hode/Hals ins.": { "0": ["Body","AtMost","DoseAtAbsoluteVolume",7140,2,4],
        self.clinical_goals = self.case_parameters.get("ClinicalGoals")
        #{"RoiName": "CTVp_68","IsRobust": false,"Weight": 300,"FunctionType": "UniformDose","DoseLevel": 6800,"IsConstraint": false},
        self.objectives = self.case_parameters.get("Objectives")
        # derived roi status has planning CT as key and derived roi status as value (True if shape is dirty,
        # -1 if  overridden empty or overridden non empty rois, False if shape is not dirty aka an updated roi)
        self.derived_rois_status = self.case_parameters.get("derived rois status")
        self.isocenter_names = self.case_parameters.get("isocenter names")
        #Name of plan as key and the Ct study name as value:  "Hode/Hals ins.": "ØNH"
        self.planningCT_names = self.case_parameters.get("planning CTs")
        #"ExaminationNames": {"1.2.752.243.1.1.20240717140505510.7000.41203": "Legeinntegning ønh",
        self.imported_examination_names = self.case_parameters.get("ExaminationNames")

        # we set the current case either to the newest one or to the one that the user wanted to copy to
        if self.copy_to_case:
            case = self.patient.Cases[self.copy_to_case]
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
        
        """r"{}$" uses python string format(). We use a regex string to narrow the search in case of multiple patients 
        with same name and id (but with suffix). $ tells us that the string stops after the patient's last name,
        so in case of suffixes (e.g. test patient_1) these are not included in the search""" 
        patient_info = patient_db.QueryPatientInfo(
            Filter={"PatientID": self.patient.PatientID, "LastName": r"{}$".format(self.patient.Name.split("^")[0])})

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

        most_current_idx = max(range(len(datetimes)), key=lambda i:datetimes[i])
        print(most_current_idx)
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
            # sorting the copied case names based on the number (Kopiert Case #)
            copied_cases_sorted = sorted(copied_cases,key=lambda c:int(c[-1]))
            # If the patient has copied cases
            if len(copied_cases) > 0:
                # copied_cases[-1] gir den siste kopierte casen. [-1] gir tallet i kopiert case x.
                case.CaseName = "Kopiert Case {}".format(
                    int(copied_cases_sorted[-1][-1]) + 1)
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
        # first setting all names to end with tmp to ensure that we avoid duplicates which cause errors (e.g. CT 1 needs to be called CT 2),
        # but there is already a CT 2 which havent gotten its name yet

        # we only iterate the imported exams
        imported_exams = [e for e in self.case.Examinations if e.Series[0].ImportedDicomUID in self.imported_examination_names.keys()]
        # if imported exam has same name as an existing examination, the imported exam needs to have another name
        existing_examination_names = [e.Name for e in self.case.Examinations
                                      if e.Series[0].ImportedDicomUID not in self.imported_examination_names.keys()]

        print(existing_examination_names)
        print([e.Name for e in imported_exams])
        for i, ex in enumerate(imported_exams):
            # Changing prog to account for both adding tmp to exam names, then removing tmp
            prog = round(((i + 1) / (2 * len(imported_exams))) * 100, 0)
            self.Progress.update_progress(prog)
            ex.Name = ex.Name + "tmp"

        for i, ex in enumerate(imported_exams):
            prog = round(50 + ((i + 1) / (2 * len(imported_exams))) * 100, 0)
            self.Progress.update_progress(prog)
            new_name = self.imported_examination_names[ex.Series[0].ImportedDicomUID]
            # if there already exists an examination with the same name, we add a 1 to the name
            if new_name in existing_examination_names:
                # if the examination has a plan connected to it, we need to change the name in the planningCT dicionary
                self._update_case_parameters_w_examination_keys(new_name)
                # updating the name of the examination so that planningCT and examination name are equal
                ex.Name = new_name + " 1"
            else:
                ex.Name = new_name
        # if lung is in protocolname we might have a 4DCT, only works for non anonymized patients
        if any(("lunge" in e.GetProtocolName().lower() for e in self.case.Examinations if e.GetProtocolName())):
            self._handle_lung_examinations()

    def _update_case_parameters_w_examination_keys(self, new_name):
        """If we copy a case to a specific case, and there exists an examination with the same name, we need to change
        the name of the imported examination to have a 1 at the end.
        If we do this we need to also update the keys of the case parameter dictionaries that use the examination name
        as key, which is the case for the planning CT names and the derived roi status"""
        if new_name in self.planningCT_names.keys():
            # we add a new element with the same plan, but change the name
            self.planningCT_names[new_name + " 1"] = self.planningCT_names[new_name]
            # then we delete the element that has the wrong name
            self.planningCT_names.pop(new_name)
        if new_name in self.derived_rois_status.keys():
            self.derived_rois_status[new_name + " 1"] = self.derived_rois_status[new_name]
            self.derived_rois_status.pop(new_name)

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
        except Exception as e:
            print(e)
            # TODO: errormessage
            pass


    def _extract_number(self, string):
        """help method for the _handle_lung_examinations functions"""
        try:
            return int(string.split()[-1])
        except ValueError:
            return float('inf')  # Put non-numeric values at the end


    def _set_plan_parameters(self):
        CopyPlanName = []
        for i, plan in enumerate(self.case.TreatmentPlans):

            print(plan)

            # For some reason, if a plan copy is generated within the loop it appears in case. TreatmentPlans in the next iteration
            # So we skip it if it appears
            if plan.Name in CopyPlanName:
                continue
            else:
                self.Progress.update_plan("Plan {}/{}".format(i + 1, len(self.case.TreatmentPlans)))

            # If plan has copy in
            if plan.Review:
                if plan.Review.ApprovalStatus == "Approved":
                    copyname = "{} Copy".format(plan.Name)
                    CopyPlanName.append(copyname)
                    if copyname not in [p.Name for p in self.case.TreatmentPlans]:
                        self.case.CopyPlan(PlanName=plan.Name, NewPlanName="{} Copy".format(plan.Name),
                                      KeepBeamSetNames=True)
                        plan = self.case.TreatmentPlans["{} Copy".format(plan.Name)]
                    else:
                        print("plan copy already exists")
                        continue

            else:
                # Changing the name of the beamset back to its original name.
                # This is only the case if an unapproved plan has been imported
                plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace("X", ":")
                plan.Name = plan.Name.replace("X", ":").replace("Y", "/")

                # Does not work if there are multiple beamsets
                # Changing name of isocenter if the doses are not considered clinical
                # NB. Removing consider imported dose as clinical check is not scriptable
                # handelling both RS2023B and 2024B
                try:
                    if not plan.TreatmentCourse.TotalDose.DoseValues.IsAccurate:#IsClinical: 
                        for beam in plan.BeamSets[0].Beams:
                            beam.Isocenter.Annotation.Name = self.isocenter_names[plan.Name]
                except:
                    print("Raystation 2024B")
                    if not plan.TreatmentCourse.TotalDose.DoseValues.IsClinical: 
                        for beam in plan.BeamSets[0].Beams:
                            beam.Isocenter.Annotation.Name = self.isocenter_names[plan.Name]   
            # print("Plan filename")
            # print(plan_filename)

            # need this to extract correct objectives and clinical goals
            plan_name = plan.Name



            PlanOptimization_new = plan.PlanOptimizations[0]

            self.Progress.update_operation("Legger til Optimization Objectives")

            objectives = self.objectives[plan_name]
            # Adding optimization functions from the original plan for each ROI
            for j, arg_dict in enumerate(objectives):
                prog = round(((j + 1) / len(objectives)) * 100, 0)
                self.Progress.update_progress(prog)

                with CompositeAction('Add Optimization Function'):
                    try:
                        f = PlanOptimization_new.AddOptimizationFunction(FunctionType=arg_dict['FunctionType'],
                                                                         RoiName=arg_dict['RoiName'],
                                                                         IsConstraint=arg_dict['IsConstraint'],
                                                                         IsRobust=arg_dict['IsRobust']
                                                                         )
                        set_function_arguments(f, arg_dict)

                    except Exception as e:
                        print(e)
                        print("Could not set objective for ROI {} ".format(arg_dict["RoiName"]))

            self.Progress.update_operation("Legger til Clinical Goals")

            eval_setup = plan.TreatmentCourse.EvaluationSetup

            clinical_goals = self.clinical_goals[plan_name]
            for k, goal in enumerate(clinical_goals):
                prog = round(((k + 1) / len(clinical_goals)) * 100, 0)
                self.Progress.update_progress(prog)
                # Clinical goal settings  RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority
                # handeling RS2023B and RS2024B
                try:
                    RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority = clinical_goals[goal]
                except:
                    RoiName, Goalriteria, GoalType, PrimaryAcceptanceLevel, ParameterValue, Priority = clinical_goals[goal]
                try:
                    eval_setup.AddClinicalGoal(RoiName=RoiName,
                                               GoalCriteria=Goalriteria,
                                               GoalType=GoalType,
                                               AcceptanceLevel=AcceptanceLevel,
                                               ParameterValue=ParameterValue,
                                               Priority=Priority
                                               )
                except Exception as e:
                    print(e)
                    pass

            try:
                plan.PlanOptimizations[0].EvaluateOptimizationFunctions()
            except Exception as e:
                print(e)
                print("Could not compute objective functions")

        # Quitting progresswindow
        self.Progress.quit()
        self.patient.Save()