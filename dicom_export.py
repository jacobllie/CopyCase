#Dette skriptet er basert på RayStations eksempel skript:  Example_05_DICOM_export.py
#The script exports files from a patient.
from connect import *
import json
import sys


# Example on how to read the JSON error string.
def LogWarning(error):
    try:
        jsonWarnings = json.loads(str(error))
        # If the json.loads() works then the script was stopped due to
        # a non-blocking warning.
        print("WARNING! Export Aborted!")
        print("Comment:")
        print(jsonWarnings["Comment"])
        print("Warnings:")

        # Here the user can handle the warnings. Continue on known warnings,
        # stop on unknown warnings.
        for w in jsonWarnings["Warnings"]:
            print(w)
    except ValueError as error:
        print("Error occurred. Could not export.")



# The error was likely due to a blocking warning, and the details should be stated
# in the execution log.
# This prints the successful result log in an ordered way.
def LogCompleted(result):
    try:
        jsonWarnings = json.loads(str(result))
        print("Completed!")
        print("Comment:")
        print(jsonWarnings["Comment"])
        print("Warnings:")
        for w in jsonWarnings["Warnings"]:
            print(w)
        print("Export notifications:")
        # Export notifications is a list of notifications that the user should read.
        for w in jsonWarnings["Notifications"]:
            print(w)
    except ValueError as error:
        print("Error reading completion messages.")


def Export(destination, case, beamsets):
    """
    Function that exports examinations to a temporary folder
    :param destination:
    :param case:
    :param beamsets:
    :return:
    """
    print("Exporting")

    #må fjerne eventuelle corrected cbct og virtuelle ct for de kan ikke eksporteres. Har ingen bedre måte å identifisere
    # non clinical examinations på
    examinations = [exam for exam in case.Examinations if "AlgorithmVersion" not in dir(exam)]

    print(case.CaseName)

    errormessage = []
    to_examinations = []
    from_examinations = []
    spatial_reg_for_exams = None
    try:
        for i, registration in enumerate([r for r in case.Registrations]):
            # Skipping invalid registrations which are not applicable for scriptabledicomexport
            if len(registration.StructureRegistrations) < 1 or registration.FromFrameOfReference == registration.ToFrameOfReference:
                print("Invalid registration found")
                continue
            for_registration = registration
            # Frame of reference of the "To" examination.
            to_for = for_registration.ToFrameOfReference

            # Frame of reference of the "From" examination.
            from_for = for_registration.FromFrameOfReference

            # Find all examinations with frame of reference that matches 'to_for'.
            to_examinations.append([e for e in examinations if e.EquipmentInfo.FrameOfReference == to_for])

            # Find all examinations with frame of reference that matches 'from_for'.
            from_examinations.append([e for e in examinations if e.EquipmentInfo.FrameOfReference == from_for])

        # examination pairs for which the registration object shall be exported. Accounted for different lengths
        # of to and from examinations

        """There might be multiple studies that might be in the same frame of reference. Therefore it is only necessary to have 
                one registration pair for each registration. 
                E.g. if CT1 is registered to Legeinntegning, and CT1 is in the same FOR as CT2,CT3 etc. then we will only have to export the 
                registration of CT1 and Legeinntegning, and the others will follow."""
        spatial_reg_for_exams = ["%s:%s" % (from_examinations[i][0].Name, to_examinations[i][0].Name) for
                                            i in range(len(min([to_examinations, from_examinations], key=len)))]


    except Exception as e:
        print(e)
        print("The case does not contain any registrations")

    #checking for invalid geometries in planning CTs
    #Invalid geometries in non plan CTs will not affect the export, because they are not as strict.
    #Only plans with doses are exported, so we can use the
    # case.TreatmentPlans[].BeamSets[].FractionDose.OnDensity.FromExamination.Name, to find the correct examination for the plan that will be exported.

    invalid_geometries = []

    for beamset in beamsets:
        print(beamsets)
        # Beamsetidentifier = "planname:beamsetname"
        plan = beamset.split(":")[0]

        """Det er ikke nødvendig å identifisere invalide OAR dersom ikke planen skal eksporteres."""
        examination = case.TreatmentPlans[plan].BeamSets[0].GetPlanningExamination()
        structureset = case.PatientModel.StructureSets[examination.Name]

        # Check for invalid volumes in the structureset
        # Man kan ikke eksportere plan med ugyldige strukturer (rød firkant), men man kan eksportere
        # Volumer overriden strukturer (gule trekanter)

        # Ikke tomme volumer som er rød har primary shape og DerivedRoiStatus. IsShapeDirty = True

        # Tomme røde volumer har DerivedRoiExpression og Primary Shape er Null.

        # Overridden volumer har DerivedRoiStatus = Null

        for roi in structureset.RoiGeometries:
            # Det er bare derived Rois som blir invalid
            if roi.OfRoi.DerivedRoiExpression:
                # ikke tomme derived rois
                if roi.PrimaryShape:
                    if roi.PrimaryShape.DerivedRoiStatus:
                        # red volumes have dirty shape
                        if roi.PrimaryShape.DerivedRoiStatus.IsShapeDirty:
                            errormessage.extend(["\nInvalid Roi ({}) found in plan-CT: {}\n{} was not exported\n" \
                                            "override or underive".format(roi.OfRoi.Name, examination.Name,plan)])
                            print("Invalid Roi ({}) found in plan-CT: {}\noverride or underive"
                                  .format(roi.OfRoi.Name, examination.Name))
                            # Fjerner plan med ugyldige volumer
                            beamsets.remove(beamset)
                            break
                    # empty overriden rois
                    else:
                        continue
                # tomme ugyldige derived rois
                else:
                    errormessage.extend(["\nInvalid Roi ({}) found in plan-CT: {}\n{} was not exported\n" \
                                            "override or underive".format(roi.OfRoi.Name, examination.Name,plan)])
                    print("Invalid Roi ({}) found in plan-CT: {}\noverride or underive"
                          .format(roi.OfRoi.Name, examination.Name))
                    beamsets.remove(beamset)
                    break

    try:

        result = case.ScriptableDicomExport(ExportFolderPath=destination,
                                            Examinations=[examination.Name for examination in examinations],
                                            RtStructureSetsForExaminations=[examination.Name for examination in
                                                                            examinations],
                                            # This exports the structure set that contains all structures for the examination. It will always be the SubStructureSet where IsDefault == True (it will always be unapproved)
                                            # RtStructureSetsReferencedFromBeamSets=beamsets, # This exports the structure set linked to beam_set
                                            # RtStructureSetsWithDicomUIDs = [structure_set.SubStructureSets[0].ModificationInfo.DicomUID], # This exports the structure_set based on its UID
                                            BeamSets=beamsets,
                                            PhysicalBeamSetDoseForBeamSets=beamsets,
                                            # EffectiveBeamSetDoseForBeamSets=beamsets,
                                            PhysicalBeamDosesForBeamSets=beamsets,
                                            # EffectiveBeamDosesForBeamSets=beamsets,
                                            SpatialRegistrationForExaminations=spatial_reg_for_exams,
                                            # DeformableSpatialRegistrationsForExaminations = ["%s:%s:%s"%(def_registration.InStructureRegistrationGroup.Name,
                                            #                                                             def_registration.FromExamination.Name,
                                            #                                                             def_registration.ToExamination.Name)],
                                            # TreatmentBeamDrrImages = [beam_set.BeamSetIdentifier()],
                                            # SetupBeamDrrImages = [beam_set.BeamSetIdentifier()],
                                            DicomFilter="",
                                            IgnorePreConditionWarnings=True
                                            )

        # It is very important to read the result event if the script was successful.
        # This gives the user a chance to see any warnings that have been ignored.
        LogCompleted(result)
        errormessage.extend(["\nSuccesfull export"])

    except Exception as e:
        print("Unsuccesfull Export")

        error = str(e).split("--- End of inner exception stack trace ---")[0]
        # we need to split up the errormessage
        errormessage.extend(["\n\n%s" %error])
        errormessage.extend(["\nExporting only examinations"])
        print("Exporting only examinations")
        beamsets = []
        try:
            result = case.ScriptableDicomExport(ExportFolderPath=destination,
                                                Examinations=[examination.Name for examination in examinations],
                                                RtStructureSetsForExaminations=[examination.Name for examination in
                                                                                examinations],
                                                # This exports the structure set that contains all structures for the examination. It will always be the SubStructureSet where IsDefault == True (it will always be unapproved)
                                                # RtStructureSetsReferencedFromBeamSets=beamsets, # This exports the structure set linked to beam_set
                                                # RtStructureSetsWithDicomUIDs = [structure_set.SubStructureSets[0].ModificationInfo.DicomUID], # This exports the structure_set based on its UID
                                                BeamSets=beamsets,
                                                PhysicalBeamSetDoseForBeamSets=beamsets,
                                                # EffectiveBeamSetDoseForBeamSets=beamsets,
                                                PhysicalBeamDosesForBeamSets=beamsets,
                                                # EffectiveBeamDosesForBeamSets=beamsets,
                                                SpatialRegistrationForExaminations=spatial_reg_for_exams,
                                                # DeformableSpatialRegistrationsForExaminations = ["%s:%s:%s"%(def_registration.InStructureRegistrationGroup.Name,
                                                #                                                             def_registration.FromExamination.Name,
                                                #                                                             def_registration.ToExamination.Name)],
                                                # TreatmentBeamDrrImages = [beam_set.BeamSetIdentifier()],
                                                # SetupBeamDrrImages = [beam_set.BeamSetIdentifier()],
                                                DicomFilter="",
                                                IgnorePreConditionWarnings=True
                                                )
            errormessage.append("\nSuccessfully exported examinations")


        except:
            print("Could not export examinations")
            errormessage.append("\nCould not export examinations")

    return errormessage
