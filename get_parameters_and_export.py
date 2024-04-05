# Function that extracts RayStation case parameters and exports

#import python modules
import json
import os
import sys

#import local files
from get_and_set_arguments_from_function import get_arguments_from_function, set_function_arguments
from dicom_export import Export


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

    clinical_goals = {}
    beamsets = []
    isocenter_names = {}

    #planning_CTs = {}

    #Looping trough plans

    exported_plans = []
    for plan in case.TreatmentPlans:

        """Getting clinical goals and optimization objectives from plan"""

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


        """Performing plan sanity check: Is the plan approved, is it imported, does it have clinical doses. All things
        required for scriptable dicom export"""
        print(plan.Name)

        if len(plan.BeamSets) < 1:
            continue

        approved = None
        try:
            if plan.Review.ApprovalStatus == "Approved":
                print(
                    "Plan {} er Approved og kan ikke eksporteres med scriptable export og må eksporteres manuelt.".format(
                        plan.Name))
                approved = True
        except:
            pass

        imported = None
        try:
            #Skipping imported plans as they cannot be exported to new case
            #if "IMPORTED" in plan.Comments.upper() or plan.BeamSets[0].FractionDose.DoseValues.IsClinical == True:
            if "IMPORTED" in plan.BeamSets[0].FractionDose.DoseValues.AlgorithmProperties.DoseAlgorithm.upper():
                print("Plan: {} is imported and cannot be exported".format(plan.Name))
                print("Imported funnet i plankommentar. Dersom dosene ikke er importerte, fjern Imported fra plankommentaren.")
                imported = True
            else:
                imported = False
        except:
            print("No comment in plan")

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
                #Dose does not exist and needs to be recalculated
                plan.BeamSets[0].ComputeDose(ComputeBeamDoses=True, DoseAlgorithm="CCDose", ForceRecompute=False,
                                             RunEntryValidation=True)
                plan.BeamSets[0].FractionDose.UpdateDoseGridStructures()
                dose_computed = True
            except:
                # Dose could not be recomputed, skip plan
                print("Could not recompute dose")
                dose_computed = False


        if dose_computed and not approved and not imported:
            isocenter_names[plan.Name] = plan.BeamSets[0].Beams[0].Isocenter.Annotation.Name
            #Changing name of beamset to be compatible with the ScriptableDicomExport function
            if export_files:
                plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace(":", "X")
                plan.Name = plan.Name.replace(":", "X").replace("/", "Y")
                beamsets.append("%s:%s" % (plan.Name, plan.BeamSets[0].DicomPlanLabel))
                exported_plans.append(plan)

    # TODO: Dette burde vel også samles opp i en fil per plan
    # Saving isocenter names
    with open(os.path.join(destination, '{}_isocenter_names.json'.format(initials)), 'w') as f:
        json.dump(isocenter_names, f)


    #Exporting CT studies, doses beams and registrations
    #Saving changes before export
    patient.Save()

    if export_files and not approved and not imported:
        error = Export(destination, case, beamsets)
        if error:
            return error

    #Endrer navnet tilbake til det opprinnelige
    if export_files:
        for plan in exported_plans:
            try:
                plan.Name = plan.Name.replace("X", ":").replace("Y", "/")
            except:
                print("Could not change plan name")
            plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace("X", ":")

    patient.Save()

    return None