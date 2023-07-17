#Python script that copies a patient Case in RayStation
#The plans must be unaproved for this to work
import os
from connect import *
import json
import sys

# Import local files:
from delete_files_and_folders import delete_files_and_folders
from get_parameters_and_export import get_parameters_and_export
from import_and_set_parameters import import_and_set_parameters

destination = "C:\\temp\\tempexport"

delete_folder = True

if delete_folder == True:

    #deleting existing files and folders in tempexport
    try:
        delete_files_and_folders(exportfolder)
    except:
        pass

    if not os.path.exists(exportfolder):
        os.makedirs(exportfolder)

# Load patient and case data:
try:
    patient = get_current("Patient")
except SystemError:
    raise IOError("No patient loaded.")
try:
    case = get_current("Case")
except SystemError:
    raise IOError("No case loaded.")

patient_name = patient.Name.split("^")

#Initials used in filenames
initials = ""
for name in patient_name:
    initials += name[0]

#Getting case parameters and exporting images, beams, doses and plans to temporary folder
get_parameters_and_export(initials, destination, patient, case)

importfolder = destination

#Importing images, beams, doses and plans from temporary folder and setting case parameters
import_and_set_parameters(initials, importfolder, patient, case)