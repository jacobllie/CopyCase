# This script imports dicom files from an importfolder to a new case
# It is based on a RayStation example script Example_03_DICOM_import_to_current_patient.py
from connect import *
import tkinter as tk
import sys

def Import(importfolder, patient, copy_to_case):
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
    error = None
    try:

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
        print("here")
        print(copy_to_case)
        warnings = patient.ImportDataFromPath(Path=importfolder, SeriesOrInstances=series, CaseName=copy_to_case)
        print("Warnings: %s" % warnings)
    except:
          error = "Could not import, are all the files present in \n" \
                  "C:\\temp\\tempexport"


    if error:
        errormessage = tk.Toplevel()
        app = tk.messagebox.showinfo("Message", error)
        sys.exit()

    patient.Save()

    return error

