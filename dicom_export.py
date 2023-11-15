#Dette skriptet er basert på RayStations eksempel skript:  Example_05_DICOM_export.py
#The script exports files from a patient.
from connect import *
import json
import System


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
    examinations = case.Examinations
    print(case.CaseName)

    to_examinations = []
    from_examinations = []
    try:
        for i, registration in enumerate(case.Registrations):
            # Skipping invalid registrations
            if len(registration.StructureRegistrations) < 1:
                print("Invalid registration found")
                continue
            for_registration = registration
            # Frame of reference of the "To" examination.
            to_for = for_registration.ToFrameOfReference

            # Frame of reference of the "From" examination.
            from_for = for_registration.FromFrameOfReference

            # Find all examinations with frame of reference that matches 'to_for'.
            to_examinations.append([e for e in case.Examinations if e.EquipmentInfo.FrameOfReference == to_for])

            # Find all examinations with frame of reference that matches 'from_for'.
            from_examinations.append([e for e in case.Examinations if e.EquipmentInfo.FrameOfReference == from_for])

        """There might be multiple studies that might be in the same frame of reference. Therefore it is only necessary to have 
        one registration pair for each registration. 
        E.g. if CT1 is registered to Legeinntegning, and CT1 is in the same FOR as CT2,CT3 etc. then we will only have to export the 
        registration of CT1 and Legeinntegning, and the others will follow."""


        # Then we get these pairs
        print(["%s:%s" % (from_examinations[i][0].Name, to_examinations[i][0].Name) for i in
               range(len(from_examinations))]
              )

    except:
        print("The case does not contain any registrations")

    try:

        # It is not necessary to assign all of the parameters, you only need to assign the
        # desired export items. In this example we try to export with
        # IgnorePreConditionWarnings=False. This is an option to handle possible warnings.
        # RtStructureSetsForExaminations, RtStructureSetsReferencedFromBeamSets and RtStructureSetsWithDicomUIDs can all be used to select which structure set to export.
        # The lists are merged so if they point to the same structure set, only one DICOM RT Structure Set will be exported.
        # PhysicalBeamSetDoseForBeamSets: Type=Plan tilsvarer dose for the entire beam set (lest av fra eksportvindu).
        # EffectiveBeamSetDoseForBeamSets resulterer i feilmelding
        # PhysicalBeamDosesForBeamSets: Type = Beam tilsvarer all beam doses (lest av fra eksportvindu)
        # EffectiveBeamDosesForBeamSets resulterer i feilmelding


        result = case.ScriptableDicomExport(ExportFolderPath=destination,
                                            Examinations=[examination.Name for examination in examinations],
                                            RtStructureSetsForExaminations=[examination.Name for examination in
                                                                            examinations],
                                            # This exports the structure set that contains all structures for the examination. It will always be the SubStructureSet where IsDefault == True (it will always be unapproved)
                                            #RtStructureSetsReferencedFromBeamSets=beamsets, # This exports the structure set linked to beam_set
                                            #RtStructureSetsWithDicomUIDs = [structure_set.SubStructureSets[0].ModificationInfo.DicomUID], # This exports the structure_set based on its UID
                                            BeamSets=beamsets,
                                            PhysicalBeamSetDoseForBeamSets=beamsets,
                                            #EffectiveBeamSetDoseForBeamSets=beamsets,
                                            PhysicalBeamDosesForBeamSets=beamsets,
                                            #EffectiveBeamDosesForBeamSets=beamsets,
                                            SpatialRegistrationForExaminations=[
                                                "%s:%s" % (from_examinations[i][0].Name, to_examinations[i][0].Name) for
                                                i in range(len(from_examinations))],
                                            #DeformableSpatialRegistrationsForExaminations = ["%s:%s:%s"%(def_registration.InStructureRegistrationGroup.Name,
                                            #                                                             def_registration.FromExamination.Name,
                                            #                                                             def_registration.ToExamination.Name)],
                                            # TreatmentBeamDrrImages = [beam_set.BeamSetIdentifier()],
                                            # SetupBeamDrrImages = [beam_set.BeamSetIdentifier()],
                                            DicomFilter="",
                                            IgnorePreConditionWarnings=False
                                            )

        # It is important to read the result event if the script was successful.
        # This gives the user a chance to see possible warnings that were ignored, if for
        # example the IgnorePreConditionWarnings was set to True by mistake. The result
        # also contains other notifications the user should read.
        LogCompleted(result)

    except System.InvalidOperationException as error:

        LogWarning(error)

        print("\nTrying to export again with IgnorePreConditionWarnings=True\n")

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
                                                SpatialRegistrationForExaminations=[
                                                    "%s:%s" % (from_examinations[i][0].Name, to_examinations[i][0].Name) for
                                                    i in range(len(from_examinations))],
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
        except:
            print("Unsuccesfull Export")

    except Exception as e:
        print('Except %s' % e)


    pass
