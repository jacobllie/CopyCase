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
from get_parameters_and_export import Get
from set_parameters import Set
from GUI import mainGUI, INFOBOX, ProgressBar
from dicom_import import Import, Import_new_patient
from utils import delete_files_and_folders


# TODO: Ta hensyn til om det eksisterer en plan i caset som det skal kopieres til
#  og eventuelt om det finnes en låst plan med et låst struktursett

def copycase():
    """
    copycase extracts case parameters such as clinical goals, optimization objectives, derived roi expressions and dose colors.
    It can also export plans and examinations either to a new case or to an existing case. It can import the plans and examinations
    and set the extracted case parameters
    :param path: needed for the help function in the gui to open a word document
    :return:
    """
    # Load patient and case data:
    try:
        patient = get_current("Patient")
    except:
        patient = None
        print("No patient loaded.")
    """try:
        case = get_current("Case")
    except SystemError:
        raise IOError("No case loaded.")"""
    try:
        patient_db = get_current("PatientDB")
    except:
        print("Could not get patient database.")


    destination = "C:\\temp\\tempexport\\"
    case_parameters = {}
    error = []

    #Getting case parameters and exporting images, beams, doses and plans to temporary folder


    root = tk.Tk()
    app = mainGUI(root, patient)
    root.mainloop()

    get_parameters, get_derived_rois, export_files, import_files, import_new_patient, set_parameters, delete_files, copy_to_case = app.options_list

    print({"delete files":delete_files,"get parameters":get_parameters, "get derived rois":get_derived_rois,"export files":export_files,
           "import files":import_files,"import new patient":import_new_patient,"set parameters":set_parameters,"copy to case":copy_to_case})

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

    """patient_name = patient.Name.split("^")

    #Initials used in filenames
    initials = ""
    for name in patient_name:
        # some names have more ^^ after the name which needs to be accounted for
        initials += name[0] if len(name) > 0 else "" """

    if get_parameters:
        # initialising GET class
        get = Get(destination, export_files=export_files,
                                          get_derived_rois=get_derived_rois)
        # extracting parameters and exporting if export files is true
        # merging local case parameters and get's case parameters
        case_parameters = {**case_parameters, **get.case_parameters}
        initials = "".join(n[0] for n in case_parameters["Name"].split("^") if len(n) > 0)
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
        importfolder = destination
        
        json_files = [file for file in os.listdir(destination) if ".json" in file]
        if not json_files:
            messagebox.showerror(message=f"No case parameter file in {destination}, choose get parameters")

        # case_parameters should always exists if get parameters have been run before
        case_parameters = json.load(open(os.path.join(destination, json_files[0])))

        prog = tk.Tk()
        app = ProgressBar(prog)
        if import_files:
            if import_new_patient:
                Import_new_patient(importfolder, case_parameters, patient_db)
            else:
                Import(importfolder, case_parameters)
        if set_parameters:
            set = Set(app, case_parameters, importfolder)
            error = set.error

    if error != [] and error != None:
        msg = tk.Tk()
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
