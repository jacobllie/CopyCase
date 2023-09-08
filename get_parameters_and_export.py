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

    #Including all ROIs for export
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
    for plan in case.TreatmentPlans:
        print(plan.Name)

        if len(plan.BeamSets) < 1:
            continue

        #Tror ikke jeg trenger planning CTs egentlig
        #planning_CTs[plan.Name] = plan.BeamSets[0].FractionDose.OnDensity.FromExamination.Name

        #Changing name of beamset to be compatible with the ScriptableDicomExport function

        if export_files:
            plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace(":", "X")
            plan.Name = plan.Name.replace(":", "X").replace("/","Y")


        isocenter_names[plan.Name] = plan.BeamSets[0].Beams[0].Isocenter.Annotation.Name

        PlanOptimization = plan.PlanOptimizations[0]
        arguments = []
          # List to hold arg_dicts of all functions.
        # dictionary that holds the clinical goal objectives
        clinical_goals[plan] = {}
        #beamsets[plan] = plan.BeamSets
        #Assumes only one beamset

        beamsets.append("%s:%s"%(plan.Name,plan.BeamSets[0].DicomPlanLabel))
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
        #Accessing evaluation functions
        eval_functions = plan.TreatmentCourse.EvaluationSetup.EvaluationFunctions

        for i,ef in enumerate(eval_functions):
            #Clinical goal settings  RoiName, Goalriteria, GoalType, AcceptanceLevel, ParameterValue, Priority
            planning_goals = ef.PlanningGoal
            clinical_goals[plan][i] = [ef.ForRegionOfInterest.Name, planning_goals.GoalCriteria, planning_goals.Type,
                                       planning_goals.AcceptanceLevel, planning_goals.ParameterValue, planning_goals.Priority]

        #Saving each plan with the CT study names
        #with open(os.path.join(destination,'{}_{}_planningCTs.json'.format(initials, plan.Name.replace("/","V"))), 'w') as f:
        #    json.dump(planning_CTs, f)

        #Saving clinical goals
        #Replace / with V in filename
        with open(os.path.join(destination,'{}_{}_ClinicalGoals.json'.format(initials, plan.Name)), 'w') as f:
            json.dump(clinical_goals[plan], f)

        #Saving objectives
        with open(os.path.join(destination,'{}_{}_objectives.json'.format(initials, plan.Name)), 'w') as f:
            json.dump(arguments, f)

    # Saving isocenter names
    with open(os.path.join(destination, '{}_isocenter_names.json'.format(initials)), 'w') as f:
        json.dump(isocenter_names, f)


    #Exporting CT studies, doses beams and registrations
    #Saving changes before export
    patient.Save()

    if export_files:
        Export(destination, case, beamsets)

    #Endrer navnet tilbake til det opprinnelige
    for plan in case.TreatmentPlans:
        plan.Name = plan.Name.replace("X", ":").replace("Y", "/")
        plan.BeamSets[0].DicomPlanLabel = plan.BeamSets[0].DicomPlanLabel.replace("X", ":")

    patient.Save()

    pass