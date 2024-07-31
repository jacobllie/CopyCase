import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import time
from tkinter import messagebox
import os
import threading
from typing import List
from connect import *


class mainGUI:
    def __init__(self, root:tk.Tk, patient):
        self.root = root
        self.root.title("Kopier Case")
        self.patient = patient

        self.get_parameters_var = tk.BooleanVar()
        self.derived_rois_var = tk.BooleanVar()
        self.export_var = tk.BooleanVar()
        self.import_var = tk.BooleanVar()
        self.set_parameters_var = tk.BooleanVar()
        self.delete_files = tk.BooleanVar()
        self.copy_to_case = None

        self.options_list = [self.get_parameters_var,
                             self.derived_rois_var,
                             self.export_var,
                             self.import_var,
                             self.set_parameters_var,
                             self.delete_files,
                             self.copy_to_case
                             ]

        self.create_widgets()

    def create_widgets(self):

        # Add widgets to the frames

        #self.root.columnconfigure(0, weight=0.5)  # First column

        tk.Label(self.root, text="NB! Dersom Caset inneholder en Approved plan, så må CopyCase kjøres to ganger (trykk hjelp for mer info)").\
            grid(row=0, column=0, columnspan=1, pady=1)


        tk.Label(self.root, text="Valg:").grid(row=1, column=0, columnspan=1, pady=1)

        f0 = tk.Frame(self.root)
        f0.grid(row=4, column=0, sticky="w")
        tk.Checkbutton(f0, text="Hent Case parametere (cli. goals, opt. objectives etc.)",
                       variable=self.get_parameters_var).grid(row=0, column=0, sticky="w")
        tk.Checkbutton(f0, text="-Hent regler for utledede ROIer (eksperimentelt)",
                       variable=self.derived_rois_var, command=self.get_parameters_subcheck).grid(row=1, column=0, sticky="nw", padx=(50, 0))

        tk.Checkbutton(self.root, text="Eksporter alle studier, planer og doser", variable=self.export_var,
                       command=self.handle_export_but_no_get_parameters).grid(row=6, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Importer alle eksporterte filer", variable=self.import_var).grid(row=7,
                                                                                                             column=0,
                                                                                                             sticky="w")
        tk.Checkbutton(self.root, text="Sett Case parametere", variable=self.set_parameters_var).grid(row=8,
                                                                                                          column=0,
                                                                                                          sticky="w")

        tk.Checkbutton(self.root, text="Slett midlertidige filer", variable=self.delete_files).grid(row=9, column=0,
                                                                                                    sticky="w")
        self._copy_to_case_widget()

        self._generate_okcancel_buttons()

        self._generate_choose_all_and_help_buttons()

        # Bind the Return key event to the show_selected_options method
        self.root.bind("<Return>", self.show_selected_options)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def _generate_choose_all_and_help_buttons(self):
        f2 = tk.Frame(self.root)
        f2.grid(row=2, columnspan=3)
        alle = tk.Button(f2, text="Velg/fjern alle", width=15, command=self.choose_all, font=("Helvetica", 10)).grid(row=1,
                                                                                                               column=0,
                                                                                                               padx=10)
        hjelp = tk.Button(f2, text="Hjelp", width=15, command=self.help, font=("Helvetica", 10)).grid(row=1, column=1)

    def _generate_okcancel_buttons(self):
        f3 = tk.Frame(self.root)
        f3.grid(row=10, columnspan=2)
        ok = tk.Button(f3, text="OK", width=10, command=self.show_selected_options, font=("Helvetica", 10)).grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=15)
        lukk = tk.Button(f3, text="Lukk", width=10, command=self.close_window, font=("Helvetica", 10)).grid(row=0,
                                                                                                            column=2,
                                                                                                            padx=15)
    def _copy_to_case_widget(self):
        f1 = tk.Frame(self.root)
        f1.grid(row=4, column=0, padx=(400, 0))
        tk.Label(f1, text="Kopier til et spesifikt case", font=("Helvetica", 12), justify="left").grid(row=0, column=0)
        tk.Label(f1, text="NB. Må bare spesifiseres når case parametere hentes", font=("Helvetica",9),justify="left").\
            grid(row=1,column=0)
        self.scrollbar = tk.Scrollbar(f1)
        self.scrollbar.grid(row=2, column=0, sticky="w", padx=(105, 0))
        current_case = get_current("Case")
        print(current_case.CaseName)
        # we remove the currently active case, because we dont want to copy a case to itself
        cases = [c.CaseName for c in self.patient.Cases if c.CaseName != current_case.CaseName]
        # if there is only one case, then the width will be set to 5
        w = max([len(c) for c in cases]) if len(cases) > 0 else 5
        self.case_listbox = tk.Listbox(f1, yscrollcommand=self.scrollbar.set, width=w + 3,
                                  height=5,
                                  selectmode="Single", activestyle="none")
        for i, c in enumerate(cases):
            self.case_listbox.insert(tk.END, c)

        self.case_listbox.grid(row=2, column=0, sticky="w")

        deselect = tk.Button(f1, text="Clear", width=10, command=self._deselect_listbox, font=("Helvetica", 10)).grid(
            row=3,
            column=0,
            sticky="w")

        self.scrollbar.config(command=self.case_listbox.yview)


    def _deselect_listbox(self, event=None):
        """Deselecting the currently selected element with selection clear method"""
        idx = self.case_listbox.curselection()
        if len(idx) < 1:
            return
        self.case_listbox.selection_clear(self.case_listbox.curselection())


    def get_parameters_subcheck(self, event=None):
        """This function ensures that if the user wants to extract derived ROIs, then the get parameters options needs
        to be checked."""
        if self.derived_rois_var.get():
            self.get_parameters_var.set(True)

    def handle_export_but_no_get_parameters(self, event=None):
        # The user cannot ask for export, but not get parameters. That does not work. The user can however,
        # ask for import but not set parameters
        if self.export_var.get() and not self.get_parameters_var.get():
            self.get_parameters_var.set(1)

    def on_close(self):
        self.root.destroy()
        sys.exit(0)

    def show_selected_options(self, event=None):

        idx = self.case_listbox.curselection()
        if len(idx) > 0:
            self.copy_to_case = self.case_listbox.get(idx)
        else:
            self.copy_to_case = None

        self.options_list = [self.get_parameters_var.get(),
                             self.derived_rois_var.get(),
                             self.export_var.get(),
                             self.import_var.get(),
                             self.set_parameters_var.get(),
                             self.delete_files.get(),
                             self.copy_to_case
                             ]

        # if not any of the mandatory options are chosen, which are all options except for the copy to case option,
        # then we do nothing
        if not any(self.options_list[:-1]):
            print("No mandatory options chosen")
            return
        self.root.destroy()

    def choose_all(self):
        # if all checkboxes are checked, we deselect them
        print(self.options_list)
        if all([o.get() for o in self.options_list[:-1]]):
            for c in self.options_list[:-1]:
                c.set(0)
        # but if not all boxes are checked, we select all of them
        else:
            for c in self.options_list[:-1]:
                c.set(1)
        pass


    def open_file(self):
        #path = 'H:\\Dokumenter\\Github\\CopyCase\\CopyCase Hjelp.docx'
        path = "I:\\STOLAV - Kreftklinikken\\Avdelinger kreft\\Avdeling for stråleterapi\\Fysikere\\Jacob\\CopyCase\\CopyCase Hjelp.docx"
        os.startfile(path, 'open')

    def help(self):
        newroot = tk.Toplevel(self.root)
        newroot.title("hjelp")
        helptext = "\tNB: \n \tDersom det finnes låste planer i caset, så må disse eksporteres manuelt til tempexport og skriptet må kjøres i to omganger. " \
                   "For mer info om dette, trykk på «Beskrivelse av manuell eksport».\n" \
                   "\tDersom du ikke ønsker å eksportere alt, så må det også gjøres manuelt.\n\n"\
                   "\tBeskrivelse av valg:\n"\
                   "\t<Hent Case parametere> henter ulike Case parametere som navn på CT studier, clinical goals og optimization objectives og legger disse i en lokal mappe som heter tempexport.\n\n" \
                   "\t<Eksporter alle studier, planer og doser> eksporterer alle bildestudier, alle planer og alle doser som DICOM filer til tempexport.\n\n" \
                   "\t<Importer alle eksporterte filer> importerer alle filene i tempexport til et nytt case.\n\n" \
                   "\t<Sett Case parametere> setter inn case parameterne som ble hentet i det første steget, " \
                   "men før dette skjer vil skriptet be om en bekreftelse. Pass på at case-navnet i meldingsboksen avviker fra det opprinnelig caset.\n\n" \
                   "\t<Slett midlertidige filer> sletter midlertidige filer dersom de eksisterer før nye parametere hentes, og sletter filene etter alle case parametere er satt."
        label = tk.Label(newroot, text=helptext,anchor="w", justify="left")
        label.pack(pady=5,padx=5)
        button = tk.Button(newroot,text="Beskrivelse av manuell eksport", command=self.open_file)
        button.pack()


    def close_window(self):
        self.root.destroy()
        sys.exit()


class INFOBOX:
    # using type hints for easier reading
    def __init__(self, root:tk.Tk, title: str, message: List[str]):

        if not isinstance(message, list):
            raise TypeError("Expected message in INFOBOX to be a list of strings")

        self.root = root
        self.message = message # list of
        self.title = title
        #root.title(self.title)
        self.ok = tk.BooleanVar()
        self.create_widgets()
        self.root.focus_force()


    def create_widgets(self):
        # i dont know why this needs to be here, but it has to
        #self.root.columnconfigure(0, weight=1)
        #self.root.rowconfigure(0, weight=1)

        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # i dont know why this needs to be here, but it has to
        frame.columnconfigure(0, weight=1)

        lbl = tk.Label(frame, text=self.title, fg='black', font=("Helvetica", 10, "bold"))
        lbl.grid(row=0, column=0,columnspan=2, pady=0,sticky="nsew")

        #lbl = tk.Label(frame, text=self.message, wraplength=380, justify="left", fg='black', font=("Helvetica", 10))
        #lbl.grid(row=1,column=0,columnspan=2,pady=0,sticky="nsew")
        lbl = tk.Text(frame, wrap="word", height=len(self.message)+5)#, width=len(max(self.message))+5)
        #lbl = tk.Text(frame, wrap="word")
        lbl.insert("1.0", "".join(self.message))
        lbl.config(state="disabled")  # Make the text widget read-only
        lbl.grid(row=1,column=0,columnspan=2,pady=0,sticky="nsew")

        # Create the scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=lbl.yview)
        scrollbar.grid(row=1,column=3,sticky="nsew")

        # Configure the Text widget to use the scrollbar
        lbl.config(yscrollcommand=scrollbar.set)

        btn = tk.Button(frame, text="OK", width=10,command=self.confirm, font=("Helvetica", 10, "bold"))
        btn.grid(row=3,column=0,columnspan=2,pady=(5,0))
        self.root.bind("<Return>", self.confirm)
        self.root.bind("<Escape>", self.cancel)


    def confirm(self, event=None):
        self.ok.set(True)
        self.root.destroy()

    def cancel(self, event=None):
        self.root.destroy()


class ProgressBar:
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.title("Progress")
        self.root.minsize(width=300, height=100)  # Set a minimum window size

        # Create a progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(column=0, row=0, columnspan=3, padx=20, pady=10, sticky="ew")

        # Configure columns to stretch horizontally
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        self.plan_label = ttk.Label(self.root, text="")  # Adjust wraplength as needed
        self.plan_label.grid(column=0, row=1, columnspan=3)

        self.operation_label = ttk.Label(self.root, text="", wraplength=250)  # Adjust wraplength as needed
        self.operation_label.grid(column=0, row=2, columnspan=3, pady=10)

        # Create a label to display progress percentage
        self.value_label = ttk.Label(self.root, text="0%")
        self.value_label.grid(column=0, row=3, columnspan=3, pady=10)

    def update_plan(self, plan_number:int):
        self.plan_label.config(text=plan_number)

    def update_operation(self, text:str):
        self.operation_label.config(text=text)

    def update_progress(self, iteration:int):
        self.value_label.config(text="{}%".format(iteration))
        self.progress_var.set(iteration)  # Update the progress bar
        self.root.update_idletasks()  # Update the tkinter window

    def quit(self):
        self.root.destroy()

class ScrollBar:
    def __init__(self, master, label_text, options):
        self.master = master
        #threading.Thread.__init__(self)
        #self.start()
        self.label_text = label_text
        self.options = options

        self.master.title("")

        self.label = tk.Label(master, text=label_text,width=50,height=2)
        self.label.pack()

        self.scrollbar = tk.Scrollbar(master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(master, yscrollcommand=self.scrollbar.set, width=50,height=10)
        for option in options:
            self.listbox.insert(tk.END, option)
        self.listbox.pack(fill=tk.BOTH)

        self.scrollbar.config(command=self.listbox.yview)

        btn = tk.Button(self.master, text="OK", command=self.master.destroy)
        btn.pack(fill=tk.BOTH)



class ConfirmCase:
    def __init__(self, root, case):
        self.root = root
        self.case = case
        self.root.withdraw()
        self.confirm()

    def confirm(self):
        answer = messagebox.askokcancel(title="Confirmation",
                             message="Er du sikker på at du vil sette parametere for case: {}".format(self.case),
                             icon=messagebox.WARNING)
        if answer:
            pass
        else:
            sys.exit(0)