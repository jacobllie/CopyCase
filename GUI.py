import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import time
from tkinter.messagebox import askokcancel, WARNING
import os
import threading


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kopier Case")

        self.get_parameters_var = tk.BooleanVar()
        self.export_var = tk.BooleanVar()
        self.import_var = tk.BooleanVar()
        self.set_parameters_var = tk.BooleanVar()
        self.delete_files = tk.BooleanVar()

        self.create_widgets()


    def create_widgets(self):
        """tk.Label(self.root, text="Select Options:").grid(row=0, columnspan=2, pady=5)

        tk.Button(self.root, text="Velg alle", command=self.choose_all).grid(row=0, column=2)
        tk.Checkbutton(self.root, text="Slett midlertidige filer", variable=self.delete_files).grid(row=1, column=0,                                                                                                sticky="w")
        tk.Checkbutton(self.root, text="Hent Case parametere (cli. goals, opt. objectives etc.)", variable=self.get_parameters_var).grid(row=2, column=0,
                                                                                                sticky="w")
        tk.Checkbutton(self.root, text="Eksporter alle studier, planer og doser", variable=self.export_var).grid(row=3, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Importer alle eksporterte filer", variable=self.import_var).grid(row=4, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Sett Case parametere", variable=self.set_parameters_var).grid(row=5, column=0, sticky="w")
        tk.Button(self.root, text="OK", command=self.show_selected_options).grid(row=7, column=0,columnspan=1, pady=5)
        tk.Button(self.root, text="Lukk", command=self.close_window).grid(row=7, column=1,columnspan=2, pady=5)"""

        # Add widgets to the frames

        #self.root.columnconfigure(0, weight=0.5)  # First column

        tk.Label(self.root, text="NB! Dersom Caset inneholder en Approved plan, så må CopyCase kjøres to ganger (trykk hjelp for mer info)").\
            grid(row=0, column=0, columnspan=1, pady=1)


        tk.Label(self.root, text="Valg:").grid(row=1, column=0, columnspan=1, pady=1)

        tk.Checkbutton(self.root, text="Slett midlertidige filer", variable=self.delete_files).grid(row=8, column=0,
                                                                                                        sticky="w")
        tk.Checkbutton(self.root, text="Hent Case parametere (cli. goals, opt. objectives etc.)",
                       variable=self.get_parameters_var).grid(row=4, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Eksporter alle studier, planer og doser", variable=self.export_var).grid(
            row=5, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Importer alle eksporterte filer", variable=self.import_var).grid(row=6,
                                                                                                             column=0,
                                                                                                             sticky="w")
        tk.Checkbutton(self.root, text="Sett Case parametere", variable=self.set_parameters_var).grid(row=7,
                                                                                                          column=0,
                                                                                                          sticky="w")
        f1 = tk.Frame(self.root)
        f1.grid(row=2, columnspan=3)
        alle = tk.Button(f1, text="Velg alle", width=10,command=self.choose_all, font=("Helvetica", 10)).grid(row=1, column=0, padx=10)
        hjelp = tk.Button(f1, text="Hjelp",width=10, command=self.help,font=("Helvetica", 10)).grid(row=1,column=1)

        f2 = tk.Frame(self.root)
        f2.grid(row=9,columnspan=2)
        ok = tk.Button(f2, text="OK", width=10,command=self.show_selected_options, font=("Helvetica", 10)).grid(row=0, column=0,padx=15)
        lukk = tk.Button(f2, text="Lukk", width=10,command=self.close_window, font=("Helvetica", 10)).grid(row=0, column=2, padx=15)

        # Bind the Return key event to the show_selected_options method
        self.root.bind("<Return>", self.show_selected_options)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)


    def on_close(self):
        self.root.destroy()
        sys.exit(0)

    def show_selected_options(self, event=None):
        options = {
            "Get Parameters": self.get_parameters_var.get(),
            "Export": self.export_var.get(),
            "Import": self.import_var.get(),
            "Set Parameters": self.set_parameters_var.get(),
            "Delete Files": self.delete_files.get()
        }

        GUI.options_list = [self.get_parameters_var.get(),
                            self.export_var.get(),
                            self.import_var.get(),
                            self.set_parameters_var.get(),
                            self.delete_files.get()]


        selected_options = [key for key, value in options.items() if value]

        if selected_options:
            selected_text = "\n".join(selected_options)
            print("Selected Options", f"Selected options:\n{selected_text}")
        else:
            print("No Selection", "Please select at least one option.")

        self.root.destroy()

    # TODO: Dersom get parameters but not export is chosen, tell the user to manually export everything to correct folder

    def choose_all(self):
        self.delete_files.set(True)
        self.get_parameters_var.set(True)
        self.export_var.set(True)
        self.import_var.set(True)
        self.set_parameters_var.set(True)

        self.show_selected_options()

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


class INFOBOX():
    def __init__(self, root, title, message):
        self.root = root

        self.message = message
        self.title = title
        root.title(self.title)
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
        lbl = tk.Label(frame, text=self.message, fg='black', font=("Helvetica", 10))
        lbl.grid(row=1,column=0,columnspan=2,pady=5,sticky="nsew")
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
    def __init__(self, root):
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

    def update_plan(self, plan_number):
        self.plan_label.config(text=plan_number)

    def update_operation(self, text):
        self.operation_label.config(text=text)

    def update_progress(self, iteration):
        self.value_label.config(text="{}%".format(iteration))
        self.progress_var.set(iteration)  # Update the progress bar
        self.root.update_idletasks()  # Update the tkinter window

    def quit(self):
        self.root.destroy()

class ScrollBar(threading.Thread):
    def __init__(self, master, label_text, options):
        self.master = master
        threading.Thread.__init__(self)
        self.start()
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
        answer = askokcancel(title="Confirmation",
                             message="Er du sikker på at du vil sette parametere for case: {}".format(self.case),
                             icon=WARNING)
        if answer:
            pass
        else:
            sys.exit(0)