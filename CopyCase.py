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
from get_parameters_and_export import Get
from set_parameters import Set
from GUI import mainGUI, INFOBOX, ProgressBar, ScrollBar
from dicom_import import Import


def copycase():
    # Load patient and case data:
    try:
        patient = get_current("Patient")
    except SystemError:
        raise IOError("No patient loaded.")
    try:
        case = get_current("Case")
    except SystemError:
        raise IOError("No case loaded.")


    destination = "C:\\temp\\tempexport"
    case_parameters = {}
    error = []

    #Getting case parameters and exporting images, beams, doses and plans to temporary folder


    root = tk.Tk()
    app = mainGUI(root, patient)
    root.mainloop()

    get_parameters, get_derived_rois, export_files, import_files, set_parameters, delete_files, copy_to_case = app.options_list


    print({"delete files":delete_files,"get parameters":get_parameters, "get derived rois":get_derived_rois,"export files":export_files,
           "import files":import_files,"set parameters":set_parameters,"copy to case":copy_to_case})


    # Hvis get_parameters er sant, kan vi slette eksisterende filer, men dersom bare delete files er sant, så
    # Kan det være man mener å slette filene etter import og set_parameters

    # if get parameters and export
    # if any files in tempexport
    # delete files

    case_parameters["copy to case"] = copy_to_case


    if delete_files and get_parameters:
        #deleting existing files and folders in tempexport
        try:
            delete_files_and_folders(destination)
        except:
            pass
    elif get_parameters or export_files and len([f for f in os.listdir(destination)]) > 0:
        # To avoid clutter, we delete the files in tempexport
        try:
            delete_files_and_folders(destination)
        except:
            pass

    if not os.path.exists(destination):
        os.makedirs(destination)

    patient_name = patient.Name.split("^")

    #Initials used in filenames
    initials = ""
    for name in patient_name:
        initials += name[0]

    importfolder = destination

    if get_parameters:
        # initialising GET class
        get = Get(initials, destination, patient, case, export_files=export_files,
                                          get_derived_rois=get_derived_rois)
        # extracting parameters and exporting if export files is true
        # merging local case parameters and get's case parameters
        case_parameters = {**case_parameters, **get.case_parameters}

        # saving one big case parameters file
        with open(os.path.join(destination, '{}_case_parameters.json'.format(initials)), 'w') as f:
            json.dump(case_parameters, f)
        if get.error:
            root = tk.Tk()
            # flattening the error, which is a list of list
            app = INFOBOX(root, "LOG", get.error)
            root.mainloop()
        if not export_files:
            #Message about needing to export manually
            message = "Eksporter alle relevante planer, doser, bildeserier etc. manuelt til:{}".format(destination)
            messagebox.showinfo("INFO", message)

    if import_files or set_parameters:

        # case_parameters should always exists if get parameters have been run before
        tmp = json.load(open(os.path.join(destination, '{}_case_parameters.json'.format(initials))))
        copy_to_case = tmp["copy to case"]

        prog = tk.Tk()
        app = ProgressBar(prog)
        if import_files:
            Import(importfolder, patient, copy_to_case)
        if set_parameters:
            set = Set(app, initials, importfolder, patient, case)
            error = set.error

    if error != [] and error != None:
        msg = tk.Tk()
        #options = error.split("\n")
        #app = ScrollBar(msg, "Error/Warning", error)
        app = INFOBOX(msg, "Error/Warning", error)
        msg.protocol("WM_DELETE_WINDOW", root.destroy)
        msg.mainloop()

    # TODO: If import and set parameters succesfull, then delete files

    if set_parameters and delete_files:
        #deleting existing files and folders in tempexport
        try:
            delete_files_and_folders(destination)
        except:
            pass

