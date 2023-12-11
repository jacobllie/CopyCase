# This script imports dicom files from an importfolder to a new case
# It is based on a RayStation example script Example_03_DICOM_import_to_current_patient.py
from connect import *


def Import(importfolder, patient):
    """
    Function that Queries studies from path into a new case
    :param importfolder: str
    :param patient: RayStation PyScriptObject
    :return: None
    """
    #Getting patient database
    patient_db = get_current('PatientDB')

    # Patient ID for search criterias
    patient_id = patient.PatientID

    # Query patients from path by Patient ID
    matching_patients = patient_db.QueryPatientsFromPath(Path=importfolder, SearchCriterias={'PatientID': patient_id})

    # Query all the studies of the matching patient
    studies = patient_db.QueryStudiesFromPath(Path=importfolder, SearchCriterias=matching_patients[0])

    # Query all the series from all the matching studies
    series = []
    for study in studies:
      series += patient_db.QuerySeriesFromPath(Path=importfolder, SearchCriterias=study)


    # Import image series from importfolder to current patient
    # CaseName = None results in new case
    warnings = patient.ImportDataFromPath(Path=importfolder, SeriesOrInstances=series, CaseName=None)

    print("Warnings: %s" % warnings)

    patient.Save()

    pass

