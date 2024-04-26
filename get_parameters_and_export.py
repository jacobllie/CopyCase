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


def get_parameters_and_export(initials, destination, patient, case, export_files=True):
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

    error = ""

    #Including all ROIs for export and extracting derived roi expression
    ROIs = []
    for ROI in case.PatientModel.RegionsOfInterest:
        ROIs.append(ROI.Name)
    case.PatientModel.ToggleExcludeFromExport(ExcludeFromExport=False, RegionOfInterests=ROIs)

    #Get dose color map
    ColorTable = case.CaseSettings.DoseColorMap.ColorTable

    # Convert the System.Drawing.Color objects to RGB tuples to save as json
    ColorTable_serialized = {rel_dose: (color.A, color.R, color.G, color.B) for rel_dose, color in ColorTable.items()}

    #Get name of imaging scans
    examination_names = {case.Examinations[i].Series[0].ImportedDicomUID: case.Examinations[i].Name for i in
                         range(len(case.Examinations))}

    #Saving colortable
    with open(os.path.join(destination,'{}_ColorTable.json'.format(initials)), 'w') as f:
        json.dump(ColorTable_serialized, f)

    #Saving CT study names
    with open(os.path.join(destination,'{}_StudyNames.json'.format(initials)), 'w') as f:
        json.dump(examination_names, f)


    """Tror ikke vi kommer til å loope gjennom alle struktursett for å hente ut derived roi expression, det tar lang tid.
    Jeg tror heller vi fokuserer på struktursett koblet til planer
    # Saving derived roi expression and derived roi status of each roi in each structureset
    derived_rois = [roi.Name for roi in case.PatientModel.RegionsOfInterest if roi.DerivedRoiExpression]
    derived_rois_dict = {}
    start = time.time()
    for structureset in case.PatientModel.StructureSets:
        derived_rois_dict[structureset.OnExamination.Name] = {}
        #only looping through derived ROIs
        for roi in [r for r in structureset.RoiGeometries if r.OfRoi.Name in derived_rois]:
            expression = case.PatientModel.RegionsOfInterest[roi.OfRoi.Name].DerivedRoiExpression
            if roi.PrimaryShape:
                status = roi.PrimaryShape.DerivedRoiStatus
            else:
                status = None

            derived_rois_dict[structureset.OnExamination.Name][roi.OfRoi.Name] = (expression, status)

    print("elapsed time")
    print(time.time() - start)

    print(derived_rois_dict)
    """

    clinical_goals = {}
    beamsets = []
    isocenter_names = {}
    derived_rois_dict = {}
    derived_rois = [roi.Name for roi in case.PatientModel.RegionsOfInterest if roi.DerivedRoiExpression]
    derived_roi_geometries = {}
    planning_CTs = {}

    # Getting derived roi expressions

    derived_rois_dict = save_derived_roi_expressions(case, derived_rois)

    derived_roi_status = {}

    print(derived_rois_dict)

    machine_db = connect.get_current("MachineDB")
    commisioned_machines = machine_db.QueryCommissionedMachineInfo(Filter = {'IsLinac':True})
    commission_times = [m["CommissionTime"] for m in commisioned_machines]

    # checking which plans that doesnt have deprecated machines, those will be recalculated.
    # We are also checking if the plan has a beamset
    #plans_without_deprecated_machine = [p.BeamSets[0].MachineReference.CommissioningTime in commission_times for p in case.TreatmentPlans
    #                                    if p.BeamSets]
    plans_with_beam_and_without_deprecated_machine = [p for p in case.TreatmentPlans if p.BeamSets
                                        and p.BeamSets[0].MachineReference.CommissioningTime in commission_times]


    if len(plans_with_beam_and_without_deprecated_machine) == 0:
        print("There are no plans with both a beamset, and valid doses.")
        error += "\nThere are no plans with both a beamset, and valid doses."
        examination_with_external = [e for e in case.Examinations if e.EquipmentInfo.Modality == "CT" and
                       "External" in dir(case.PatientModel.StructureSets[e.Name].RoiGeometries) and
                       case.PatientModel.StructureSets[e.Name].RoiGeometries["External"].HasContours()]

        if len(examination_with_external) > 0:
            # If we have a CT study with external, we will update the derived roi status on this one
            derived_roi_status[examination_with_external[0].Name] = {}
            for roi in [r for r in structureset.RoiGeometries if r.OfRoi.Name in derived_rois]:
                # all derived rois have primary shape
                if roi.PrimaryShape.DerivedRoiStatus:
                    # red volumes have dirty shape
                    status = roi.PrimaryShape.DerivedRoiStatus.IsShapeDirty
                # non empty overriden rois
                else:
                    status = -1

                derived_roi_status[examination.Name][roi.OfRoi.Name] = status
        else:
            derived_roi_status = None


    #Looping trough plans
    exported_plans = []
    approved = False
    imported = False
    for i, plan in enumerate(plans_with_beam_and_without_deprecated_machine):#enumerate(case.TreatmentPlans):

        """Performing plan sanity check: Is the plan approved, is it imported, does it have clinical doses. All things
                required for scriptable dicom export"""

        # We are checking this in
        # If plan doesnt have any beamsets
        # if len(plan.BeamSets) < 1:
        #    continue

        # If the have beams with non-zero MU
        if not all([True if beam.BeamMU > 0 else False for beam in plan.BeamSets[0].Beams]):
            error += "\n{} has beams with non-zero MU".format(plan.Name)
            print("{} has beams with non-zero MU".format(plan.Name))
            continue

        try:
            if plan.Review.ApprovalStatus == "Approved":
                print(
                    "Plan {} er Approved og kan ikke eksporteres med scriptable export og må eksporteres manuelt.".format(
                        plan.Name))
                approved = True
        except:
            pass

        try:
            # Skipping imported plans as they cannot be exported to new case
            # if "IMPORTED" in plan.Comments.upper() or plan.BeamSets[0].FractionDose.DoseValues.IsClinical == True:
            if "IMPORTED" in plan.BeamSets[0].FractionDose.DoseValues.AlgorithmProperties.DoseAlgorithm.upper():
                print("Plan: {} is imported and cannot be exported".format(plan.Name))
                print(
                    "Imported funnet i plankommentar. Dersom dosene ikke er importerte, fjern Imported fra plankommentaren.")
                imported = True
            else:
                imported = False
        except:
            print("No comment in plan")

        if approved:
            error += "\n{} is approved".format(plan.Name)
        if imported:
            error += "\n{} has \"is imported\" in plan comment. If it is imported recalculate doses and remove the comment".format(
                plan.Name)


        # In 2023B Eval the nonexistent objects are None
        # In 12A the nonexistent objects are Null and cannot be extracted
        # This approach will work for both
        dose_computed = None
        try:
            if plan.TreatmentCourse.TotalDose.DoseValues:
                # Removing potential missing dose statistics
                plan.BeamSets[0].FractionDose.UpdateDoseGridStructures()
                dose_computed = True

            else:
                # Dose does not exist and needs to be recalculated
                plan.BeamSets[0].ComputeDose(ComputeBeamDoses=True, DoseAlgorithm="CCDose", ForceRecompute=False,
                                             RunEntryValidation=True)
                plan.BeamSets[0].FractionDose.UpdateDoseGridStructures()
                dose_computed = True
        except:
            try:
                print("No doses")
                # Dose does not exist and needs to be recalculated
                plan.BeamSets[0].ComputeDose(ComputeBeamDoses=True, DoseAlgorithm="CCDose", ForceRecompute=False,
                                             RunEntryValidation=True)
                plan.BeamSets[0].FractionDose.UpdateDoseGridStructures()
                dose_computed = True
            except:
                # Dose could not be recomputed, skip plan
                print("Could not recompute dose")
                dose_computed = False

        if dose_computed:
            # It is only necessary to gather clinical goals and objectives from plans with computed doses (which are exported)

            """Getting clinical goals and optimization objectives from plan with commissioned machine"""

            PlanOptimization = plan.PlanOptimizations[0]
            arguments = []
            # List to hold arg_dicts of all functions.
            # dictionary that holds the clinical goal objectives
            clinical_goals[plan] = {}

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
                clinical_goals[plan][i] = [ef.ForRegionOfInterest.Name, planning_goals.GoalCriteria, planning_goals.Type,
                                           planning_goals.AcceptanceLevel, planning_goals.ParameterValue,
                                           planning_goals.Priority]

            # Saving each plan with the CT study names
            # with open(os.path.join(destination,'{}_{}_planningCTs.json'.format(initials, plan.Name.replace("/","V"))), 'w') as f:
            #    json.dump(planning_CTs, f)

            # Saving clinical goals
            # Replace / with V in filename
            with open(os.path.join(destination, '{}_{}_ClinicalGoals.json'.format(initials, plan.Name.replace("/", "Y"))),
                      'w') as f:
                json.dump(clinical_goals[plan], f)

            # Saving objectives
            with open(os.path.join(destination, '{}_{}_objectives.json'.format(initials, plan.Name.replace("/", "Y"))),
                      'w') as f:
                json.dump(arguments, f)

        if not dose_computed:
            error += "\nCan't compute doses for {}".format(plan.Name)

        """Getting plan structureset derived roi expressions and status"""

        # Cannot get the plan examination if the plan doesnt have a beamset
        examination = plan.BeamSets[0].GetPlanningExamination()
        structureset = case.PatientModel.StructureSets[examination.Name]
        """We need this to know which structuresets we need to apply the derived roi expression to in the
                    set parameters."""
        planning_CTs[plan.Name] = examination.Name
        print(examination.Name)
        derived_roi_status[examination.Name] = {}

        derived_roi_status[examination.Name] = save_derived_roi_status(structureset, derived_rois,
                                                                       derived_roi_status[examination.Name])

        if dose_computed and not approved and not imported:
            isocenter_names[plan.Name] = plan.BeamSets[0].Beams[0].Isocenter.Annotation.Name
            #Changing name of beamset to be compatible with the ScriptableDicomExport function
            if export_files:
                plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace(":", "X")
                plan.Name = plan.Name.replace(":", "X").replace("/", "Y")
                beamsets.append("%s:%s" % (plan.Name, plan.BeamSets[0].DicomPlanLabel))
                exported_plans.append(plan)



    # saving derived roi expressions and derived roi geometry statuses
    with open(os.path.join(destination, '{}_derived_roi_dict.json'.format(initials)), 'w') as f:
        json.dump(derived_rois_dict, f)

    if derived_roi_status:
        with open(os.path.join(destination, '{}_derived_roi_status.json'.format(initials)), 'w') as f:
            json.dump(derived_roi_status, f)

    # Saving isocenter names
    with open(os.path.join(destination, '{}_isocenter_names.json'.format(initials)), 'w') as f:
        json.dump(isocenter_names, f)

    # saving planning CT names
    with open(os.path.join(destination, '{}_planningCT_names.json'.format(initials)), 'w') as f:
        json.dump(planning_CTs, f)

    #Exporting CT studies, doses beams and registrations
    #Saving changes before export
    patient.Save()

    if export_files and not approved and not imported:
        exporterror = Export(destination, case, beamsets)
        if exporterror:
            error += "\n"+exporterror
            #return error

    #Endrer navnet tilbake til det opprinnelige
    if export_files:
        for plan in exported_plans:
            try:
                plan.Name = plan.Name.replace("X", ":").replace("Y", "/")
            except:
                print("Could not change plan name")
            plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace("X", ":")

    """if error != "":
        msg = tk.Toplevel()
        app = INFOBOX(msg, "Error", error)
        msg.lift()
        msg.mainloop()"""

    patient.Save()

    return error