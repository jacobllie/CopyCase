# Function that extracts RayStation case parameters and exports

#import python modules
import json
import os
import sys
import time
import connect

#import local files
from get_and_set_arguments_from_function import get_arguments_from_function, set_function_arguments
from dicom_export import Export


def save_derived_roi_expressions(case, derived_rois):


    def loop_derived_roi_expression(children, operation):
        """
        This recursive function iterates through the children in a derived roi expression for a derived ROI.
        The children alterates between a PyScriptObject and a PyScriptCollection. The function counts how many occurences
        we have of the Operation attributes which reflects if we have roi expansion/contraction, roi algebra with
        only an A expression or both A and B expressions.
        :param children: PyScriptObject or PyScriptCollection
        :param operation: Number of operations in the derived roi expression
        :return: operation
        """
        if type(children) == connect.connect_cpython.PyScriptObject:
            keys = dir(children)
            if any(["Operation" in key for key in keys]):
                operation += 1
            else:
                pass
                #print("Operation {}".format(operation))

            #print("################")
            #print(keys)
            #print([getattr(children, key) for key in keys])

            if children.Children:
                operation = loop_derived_roi_expression(children.Children, operation)
            else:
                pass
                #print("end of the line")
        else:
            for child in children:
                operation = loop_derived_roi_expression(child, operation)

        return operation

    def save_derived_roi_children(children, operation, dict, num_operations):
        """
        This function is used when we want to extract the derived roi expression children and not only find the number of
        operations are present in the derived roi expression
        :param children: PyScriptObject or PyScriptCollection
        :param operation: Number of operations in derived roi expression
        :return: operation
        """
        if type(children) == connect.connect_cpython.PyScriptObject:
            print("################")
            keys = dir(children)
            print(operation)
            if any("Operation" in key for key in keys):
                # We are on an operation
                if operation == 0 and num_operations < 3:
                    # We are on an A operation
                    dict["A operation"] = children.Operation
                elif operation == 0 and num_operations == 3:
                    # We are on an A&B operation
                    dict["A&B operation"] = children.Operation
                elif operation == 1:
                    # we are on the A operation
                    dict["A operation"] = children.Operation
                elif operation == 2:
                    # we are on the B operation
                    dict["B operation"] = children.Operation

                operation += 1

            elif any("AnteriorDistance" in key for key in keys):
                print(keys)
                # we are on an expression
                if operation < 2:
                    # we are on the A expression
                    dict["A expression"] = {key: getattr(children, key) for key in
                                                                        dir(children) if not key.startswith('__')
                                                                        and "Children" not in key}
                else:
                    dict["B expression"] = {key: getattr(children, key) for key in
                                            dir(children) if not key.startswith('__')
                                            and "Children" not in key}
            elif any("RegionOfInterest" in key for key in keys):
                print(children.RegionOfInterest.Name)
                # We are on a region of interest
                #print(operation)
                if operation < 3:
                    # if the A roi key is not present it should be initialized
                    if "A rois" not in dict:
                        dict["A rois"] = []
                    dict["A rois"].append(children.RegionOfInterest.Name)
                else:
                    if "B rois" not in dict:
                        dict["B rois"] = []
                    dict["B rois"].append(children.RegionOfInterest.Name)
            if children.Children:
                operation = save_derived_roi_children(children.Children, operation, dict, num_operations)
            else:
                print("end of the line")
        else:
            for child in children:
                operation = save_derived_roi_children(child, operation, dict, num_operations)

        return operation



    derived_roi_expressions = {}
    for roi in derived_rois:
        derived_roi_expressions[roi] = {}
        dependent_rois = case.PatientModel.StructureSets[0].RoiGeometries[roi].GetDependentRois()
        expression = case.PatientModel.RegionsOfInterest[roi].DerivedRoiExpression
        derived_roi_expressions[roi]["Output expression"] = {key: getattr(expression, key) for key in
                                                                                dir(expression) if not key.startswith('__')
                                                                                and "Children" not in key}

        if len(dependent_rois) < 2:
            # We have a simple expansion/contraction
            derived_roi_expressions[roi]["A_rois"] = dependent_rois
        else:
            operation = 0
            operation = loop_derived_roi_expression(expression.Children, operation)
            save_derived_roi_children(expression.Children, operation=0, dict=derived_roi_expressions[roi], num_operations=operation)


    return derived_roi_expressions


def get_parameters_and_export(initials, destination, patient, case,export_files=True):
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


        """Getting plan structureset derived roi expressions and status"""

        examination = plan.BeamSets[0].GetPlanningExamination()
        structureset = case.PatientModel.StructureSets[examination.Name]
        print(examination.Name)
        derived_roi_status[examination.Name] = {}
        for roi in [r for r in structureset.RoiGeometries if r.OfRoi.Name in derived_rois]:
            # all derived rois have primary shape
            if roi.PrimaryShape.DerivedRoiStatus:
                # red volumes have dirty shape
                status = roi.PrimaryShape.DerivedRoiStatus.IsShapeDirty
            # non empty overriden rois
            else:
                status = -1

            derived_roi_status[examination.Name][roi.OfRoi.Name] = status

        """Performing plan sanity check: Is the plan approved, is it imported, does it have clinical doses. All things
        required for scriptable dicom export"""
        print(plan.Name)

        # If plan doesnt have any beamsets
        if len(plan.BeamSets) < 1:
            continue

        # If the have beams with non-zero MU
        if not all([True if beam.BeamMU > 0 else False for beam in plan.BeamSets[0].Beams]):
            print("{} has beams with non-zero MU".format(plan.Name))
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
            planning_CTs[plan.Name] = examination.Name
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