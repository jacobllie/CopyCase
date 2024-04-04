#Python script that copies a patient Case in RayStation
#The plans must be unaproved for this to work
# It is not possible to copy a copied case, as the export is not possible
import os
from connect import *
import json
import sys
import tkinter as tk
from tkinter import messagebox

# Import local files:
from delete_files_and_folders import delete_files_and_folders
from get_parameters_and_export import get_parameters_and_export
from import_and_set_parameters import import_and_set_parameters
from GUI import GUI, INFOBOX, ProgressBar


def copycase():

    destination = "C:\\temp\\tempexport"

    #Getting case parameters and exporting images, beams, doses and plans to temporary folder


    root = tk.Tk()
    app = GUI(root)

    root.mainloop()
    get_parameters, export_files, import_files, set_parameters, delete_files = app.options_list

    print(delete_files, get_parameters, export_files, import_files, set_parameters)

    # Hvis get_parameters er sant, kan vi slette eksisterende filer, men dersom bare delete files er sant, så
    # Kan det være man mener å slette filene etter import og set_parameters
    if delete_files and get_parameters:
        #deleting existing files and folders in tempexport
        try:
            delete_files_and_folders(destination)
        except:
            pass


    if not os.path.exists(destination):
        os.makedirs(destination)

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

    importfolder = destination

    if get_parameters:
        error = get_parameters_and_export(initials, destination, patient, case, export_files=export_files)
        if error:
            root = tk.Tk()
            root.withdraw()
            tk.messagebox.showwarning("Warning", error, icon="warning")
        if not export_files:
            if get_parameters and not export_files:
                #Message about needing to export manually
                root = tk.Tk()
                app = INFOBOX(root, destination)
                root.mainloop()
        if set_parameters:
            root = tk.Tk()
            app = ProgressBar(root)
            # Import ans set parameters is the work function
            # We need to call the update progress function inside the work function
            import_and_set_parameters(app, initials, importfolder, patient, case, import_files=import_files)
            root.mainloop()

    else:
        if set_parameters:
            #TODO: Skriv hva som gjøres i progressbar
            root = tk.Tk()
            app = ProgressBar(root)
            # Import ans set parameters is the work function
            # We need to call the update progress function inside the work function
            import_and_set_parameters(app, initials, importfolder, patient, case, import_files=import_files)
            root.mainloop()

    #TODO: Må vi endre hvordan filene slettes?
    # Files should not be deleted if we do not set parameters
    if set_parameters and delete_files:
        #deleting existing files and folders in tempexport
        try:
            delete_files_and_folders(destination)
        except:
            pass


# TODO: Test med pasient som har XRegionkode:0-tot:Frak plan navn, og se om filnavnene blir rett
