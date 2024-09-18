# Function that extracts RayStation case parameters and exports

#import python modules
import json
import os
import sys
import time
import connect
import tkinter as tk

#import local files
from get_and_set_arguments_from_function import get_arguments_from_function, set_function_arguments
from dicom_export import Export
from GUI import INFOBOX
from utils import save_derived_roi_expressions, save_derived_roi_status


class Get:
    def __init__(self, initials, destination, patient, case, export_files=True, get_derived_rois=True):
        # TODO: Få denne til å funke som class og legg til alle case parameter til case_parameters
        self.initials = initials
        self.destination = destination
        self.patient = patient
        self.case = case
        self.export_files = export_files
        self.get_derived_rois = get_derived_rois

        self.get_parameters_and_export()

    def get_parameters_and_export(self):
        """
        Function that extracts isodose colortable, imaging scan names,
        optimization objectives, clinical goals and plan CT names and
        saves them in json files. It also exports examinations, plans and doses
        :param initials: str
        :param destination: str
        :param patient: RayStation PyScriptObject
        :param case: RayStation PyScriptObject
        :return: None
        """

        """Main function to gather parameters and export data."""
        self.case_parameters = {}
        self.error = []


        self._include_all_rois_for_export()
        self._get_dose_color_map()
        self._get_examination_names()
        if self.get_derived_rois:
            self.derived_roi_status = {}
            self._extract_derived_roi_expressions()
        self._process_plans()
        if self.export_files:
            self._export_files()

        return

    def _include_all_rois_for_export(self):
        # Including all ROIs for export and extracting derived roi expression
        ROIs = [r.Name for r in self.case.PatientModel.RegionsOfInterest]
        self.case.PatientModel.ToggleExcludeFromExport(ExcludeFromExport=False, RegionOfInterests=ROIs)

    def _get_dose_color_map(self):
        # Get dose color map
        ColorTable = self.case.CaseSettings.DoseColorMap.ColorTable

        # Convert the System.Drawing.Color objects to RGB tuples to save as json
        self.case_parameters["ColorTable"] = {rel_dose: (color.A, color.R, color.G, color.B) for rel_dose, color in
                                              ColorTable.items()}
        ColorTable_serialized = {rel_dose: (color.A, color.R, color.G, color.B) for rel_dose, color in
                                 ColorTable.items()}

        """# Saving colortable
        with open(os.path.join(self.destination, '{}_ColorTable.json'.format(self.initials)), 'w') as f:
            json.dump(ColorTable_serialized, f)"""

    def _get_examination_names(self):
        # Get name examinations
        self.case_parameters["ExaminationNames"] = {
            self.case.Examinations[i].Series[0].ImportedDicomUID: self.case.Examinations[i].Name for i in
            range(len(self.case.Examinations))}
        examination_names = {self.case.Examinations[i].Series[0].ImportedDicomUID: self.case.Examinations[i].Name for i
                             in
                             range(len(self.case.Examinations))}

        # Saving CT study names
        """with open(os.path.join(self.destination, '{}_StudyNames.json'.format(self.initials)), 'w') as f:
            json.dump(examination_names, f)"""

    def _extract_derived_roi_expressions(self):
        self.derived_rois = [roi.Name for roi in self.case.PatientModel.RegionsOfInterest if roi.DerivedRoiExpression]
        self.derived_rois_dict = save_derived_roi_expressions(self.case, self.derived_rois)
        self.case_parameters["derived rois dict"] = self.derived_rois_dict
        # saving derived roi expressions and derived roi geometry statuses
        """with open(os.path.join(self.destination, '{}_derived_roi_dict.json'.format(self.initials)), 'w') as f:
            json.dump(self.derived_rois_dict, f)"""

    def _plans_w_beamset_and_beams(self):
        #print([p for p in self.case.TreatmentPlans if p.BeamSets and p.BeamSets[0].Beams])
        plans_with_beamset_and_beams = [p for p in self.case.TreatmentPlans if p.BeamSets and p.BeamSets[0].Beams]
        #plans_with_beamset_and_beams = []
        #for p in self.case.TreatmentPlans:
        #    if p.BeamSets:
        #        if p.BeamSets[0].Beams:

        #            plans_with_beamset_and_beams.append(p)
        #        else:
        #            self.error.extend(["\n{p.Name} does not have "])
        #    else:
        #        self.error.extend(["\nThere are no plans with a beamset and beams."])

        if len(plans_with_beamset_and_beams) == 0:
            print("There are no plans with both a beamset and beams.")
            self.error.extend(["\nThere are no plans with a beamset and beams."])
        return plans_with_beamset_and_beams

    def _sanity_check(self, plan):
        """Performing plan sanity check: Is the plan approved, is it imported, does it have clinical doses. All things
                            required for scriptable dicom export"""

        machine_db = connect.get_current("MachineDB")
        commisioned_machines = machine_db.QueryCommissionedMachineInfo(Filter={'IsLinac': True})
        commission_times = [m["CommissionTime"] for m in commisioned_machines]

        # If the have beams with non-zero MU
        if not all([True if beam.BeamMU > 0 else False for beam in plan.BeamSets[0].Beams]):
            self.error.extend(["\n{} has beams with non-zero MU".format(plan.Name)])
            print("{} has beams with non-zero MU".format(plan.Name))
            return [None]

        approved = False
        try:
            if plan.Review.ApprovalStatus == "Approved":
                print(
                    "Plan {} er Approved og kan ikke eksporteres med scriptable export og må eksporteres manuelt.".format(
                        plan.Name))
                approved = True
                self.error.extend(["\n{} is approved and needs to be exported manually".format(plan.Name)])
        except:
            pass
        imported = False
        try:
            # Skipping imported plans as they cannot be exported to new case
            # if "IMPORTED" in plan.Comments.upper() or plan.BeamSets[0].FractionDose.DoseValues.IsClinical == True:
            if "IMPORTED" in plan.BeamSets[0].FractionDose.DoseValues.AlgorithmProperties.DoseAlgorithm.upper():
                print("Plan: {} is imported and cannot be exported".format(plan.Name))
                print(
                    "Imported funnet i plankommentar. Dersom dosene ikke er importerte, fjern Imported fra plankommentaren.")
                imported = True
                self.error.extend([
                    "\n{} has \"is imported\" in plan comment. If it is imported recalculate doses and remove the comment".format(
                        plan.Name)])
        except:
            print("No comment in plan")

        # In 2023B Eval the nonexistent objects are None
        # In 12A the nonexistent objects are Null and cannot be extracted
        # This approach will work for both
        dose_computed = None
        if plan.BeamSets[0].MachineReference.CommissioningTime not in commission_times:
            self.error.extend(["\n{} has deprecated machine".format(plan.Name)])
        else:
            try:
                if plan.TreatmentCourse.TotalDose.DoseValues:
                    # Removing potential missing dose statistics
                    plan.BeamSets[0].FractionDose.UpdateDoseGridStructures()
                    dose_computed = True

                else:
                    # Dose does not exist and needs to be recalculated
                    plan.BeamSets[0].ComputeDose(ComputeBeamDoses=True, DoseAlgorithm="CCDose",
                                                 ForceRecompute=False,
                                                 RunEntryValidation=True)
                    plan.BeamSets[0].FractionDose.UpdateDoseGridStructures()
                    dose_computed = True
            except:
                try:
                    print("No doses")
                    # Dose does not exist and needs to be recalculated
                    plan.BeamSets[0].ComputeDose(ComputeBeamDoses=True, DoseAlgorithm="CCDose",
                                                 ForceRecompute=False,
                                                 RunEntryValidation=True)
                    plan.BeamSets[0].FractionDose.UpdateDoseGridStructures()
                    dose_computed = True
                except:
                    # Dose could not be recomputed, skip plan
                    print("Could not recompute dose")
                    dose_computed = False

        if not dose_computed:
            self.error.extend(["\nCan't compute doses for {}".format(plan.Name)])

        return [approved, imported, dose_computed]

    def _extract_clinical_goals_and_opt_objectives(self, plan):
        """Getting clinical goals and optimization objectives from plan with commissioned machine"""
        clinical_goals = {}
        objectives = {}
        PlanOptimization = plan.PlanOptimizations[0]
        arguments = []
        # List to hold arg_dicts of all functions.
        # dictionary that holds the clinical goal objectives
        clinical_goals[plan.Name] = {}
        objectives[plan.Name] = {}

        # Get arguments from objective functions.
        if PlanOptimization.Objective != None:
            for ConstFunction in PlanOptimization.Objective.ConstituentFunctions:
                arg_dict = get_arguments_from_function(ConstFunction)
                arg_dict['IsConstraint'] = False
                arguments.append(arg_dict)

        # Get arguments from constraint functions.
        for Constraint in PlanOptimization.Constraints:
            arg_dict = get_arguments_from_function(Constraint)
            arg_dict['IsConstraint'] = True
            arguments.append(arg_dict)
        # Accessing evaluation functions
        eval_functions = plan.TreatmentCourse.EvaluationSetup.EvaluationFunctions

        for i, ef in enumerate(eval_functions):
            # Clinical goal settings  RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority
            planning_goals = ef.PlanningGoal
            clinical_goals[plan.Name][i] = [ef.ForRegionOfInterest.Name, planning_goals.GoalCriteria,
                                       planning_goals.Type,
                                       planning_goals.AcceptanceLevel, planning_goals.ParameterValue,
                                       planning_goals.Priority]

        # TODO: fullfør stor json fil

        self.case_parameters["ClinicalGoals"][plan.Name] = clinical_goals[plan.Name]
        """with open(os.path.join(self.destination,
                               '{}_{}_ClinicalGoals.json'.format(self.initials, plan.Name.replace("/", "Y"))),
                  'w') as f:
            json.dump(clinical_goals[plan], f)"""

        # Saving objectives
        self.case_parameters["Objectives"][plan.Name] = arguments
        """with open(os.path.join(self.destination,
                               '{}_{}_objectives.json'.format(self.initials, plan.Name.replace("/", "Y"))),
                  'w') as f:
            json.dump(arguments, f)"""

    def _extract_derived_roi_statuses(self, examination, structureset):

        self.derived_roi_status[examination.Name] = {}
        # derived rois is defined in _extract_derived_roi_expressions()
        self.derived_roi_status[examination.Name] = save_derived_roi_status(structureset, self.derived_rois,
                                                                       self.derived_roi_status[examination.Name])
        self.case_parameters["derived rois status"][examination.Name] = self.derived_roi_status[examination.Name]
        # saving derived roi expressions and derived roi geometry statuses

    def _process_plans(self):

        self.case_parameters["isocenter names"] = {}
        self.case_parameters["ClinicalGoals"] = {}
        self.case_parameters["Objectives"] = {}
        self.case_parameters["derived rois status"] = {}
        self.case_parameters["planning CTs"] = {}
        self.beamsets = []

        # Looping trough plans
        self.exported_plans = []

        plans_w_beamset_and_beams = self._plans_w_beamset_and_beams()
        for i, plan in enumerate(plans_w_beamset_and_beams):  # enumerate(case.TreatmentPlans):

            s = self._sanity_check(plan)
            if not s[0]:
                print("Plan cannot be processes")
                continue
            else:
                approved, imported, dose_computed = self._sanity_check(plan)
            #except:
            #print("here")
            # if sanity check returns None, the plan does not have a beamset and we can do nothing
            #continue

            self._extract_clinical_goals_and_opt_objectives(plan)

            """Getting plan structureset derived roi expressions and status"""

            # Cannot get the plan examination if the plan doesnt have a beamset
            examination = plan.BeamSets[0].GetPlanningExamination()
            structureset = self.case.PatientModel.StructureSets[examination.Name]

            """We need this to know which structuresets we need to apply the derived roi expression to in the
                        set parameters."""
            self.case_parameters["planning CTs"][examination.Name] = plan.Name
            print(examination.Name)
            print(self.case_parameters["isocenter names"])
            print(plan.Name)
            self.case_parameters["isocenter names"][plan.Name] = plan.BeamSets[0].Beams[0].Isocenter.Annotation.Name

            if self.get_derived_rois:
                self._extract_derived_roi_statuses(examination, structureset)


            if dose_computed and not approved and not imported:
                # Changing name of beamset to be compatible with the ScriptableDicomExport function
                if self.export_files:
                    plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace(":", "X")
                    plan.Name = plan.Name.replace(":", "X").replace("/", "Y")
                    self.beamsets.append("%s:%s" % (plan.Name, plan.BeamSets[0].DicomPlanLabel))
                    self.exported_plans.append(plan)
                    self.patient.Save()
        # saving patient before exporting


    def _export_files(self):
        exporterror = Export(self.destination, self.case, self.beamsets)
        self.error.extend(exporterror)
        for plan in self.exported_plans:
            try:
                plan.Name = plan.Name.replace("X", ":").replace("Y", "/")
            except:
                print("Could not change plan name")
            plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace("X", ":")

        self.patient.Save()