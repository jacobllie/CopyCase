# This script imports dicom files from an importfolder to a new case
# It is based on a RayStation example script Example_03_DICOM_import_to_current_patient.py
from connect import *
import tkinter as tk
import sys

def Import(importfolder, case_parameters):
    """
    Function that Queries studies from path into a new case
    :param importfolder: str
    :param patient: RayStation PyScriptObject
    :return: None
    """
    #Getting patient database
    patient_db = get_current('PatientDB')
    try:
        patient = get_current("Patient")
    except SystemError:
        raise IOError("No patient loaded.")
    
    copy_to_case = case_parameters["copy to case"]

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

def Import_new_patient(path, case_parameters, patient_db):
    """
    Function that Queries studies from path into a new case
    We assume that if the patient exists in the database, it has no spaces in the patient id
    """
    patient_id = case_parameters["PatientID"]
    patient_name = case_parameters["Name"].split("^")
    last_name = patient_name[0]
    first_name = patient_name[1] if len(patient_name) > 1 else None
    error = None
    try:
        print("Querying patient info")
        # checking for existing patient
        patient_info = patient_db.QueryPatientInfo(Filter={'PatientID': patient_id, 'FirstName':first_name, 'LastName':last_name})
        if patient_info:
            patient = patient_db.LoadPatient(PatientInfo = patient_info[0])
            # no patient found, importing new patient
        else:
            patient = None
        print("Querying patient from path")
        # Query patients from path by Patient ID
        matching_patients = patient_db.QueryPatientsFromPath(Path=path,
                                                                SearchCriterias={'PatientID': patient_id})

        print("Querying studies from path")
        # Query all the studies of the matching patient
        studies = patient_db.QueryStudiesFromPath(Path=path, SearchCriterias=matching_patients[0])


        print("Querying series from path")
        # Query all the series from all the matching studies
        series = []
        for study in studies:
            series += patient_db.QuerySeriesFromPath(Path=path, SearchCriterias=study)

        # Import image series from importfolder to current patient

        print("Importing files")
        if patient:
            # CaseName = None results in new case
            warnings = patient.ImportDataFromPath(Path=path, SeriesOrInstances=series, CaseName=None)
            print("Warnings: %s" % warnings)
        else:
            warnings = patient_db.ImportPatientFromPath(
                Path=path,
                SeriesOrInstances=series
            )

    except Exception as e:
        print(e)

    #patient.Save()

    return error