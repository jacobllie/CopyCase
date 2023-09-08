import tkinter as tk
from tkinter import messagebox
import sys


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Options GUI")

        self.get_parameters_var = tk.BooleanVar()
        self.export_var = tk.BooleanVar()
        self.import_var = tk.BooleanVar()
        self.set_parameters_var = tk.BooleanVar()
        self.delete_files = tk.BooleanVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select Options:").grid(row=0, columnspan=2, pady=10)

        tk.Button(self.root, text="Choose All", command=self.choose_all).grid(row=0, column=3)
        tk.Checkbutton(self.root, text="Delete Temporary Files", variable=self.delete_files).grid(row=1, column=0,                                                                                                sticky="w")
        tk.Checkbutton(self.root, text="Get Case Parameters", variable=self.get_parameters_var).grid(row=2, column=0,
                                                                                                sticky="w")
        tk.Checkbutton(self.root, text="Export", variable=self.export_var).grid(row=3, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Import", variable=self.import_var).grid(row=4, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Set Case Parameters", variable=self.set_parameters_var).grid(row=5, column=0, sticky="w")
        tk.Button(self.root, text="Submit", command=self.show_selected_options).grid(row=7, columnspan=2, pady=10)
        tk.Button(self.root, text="Close", command=self.close_window).grid(row=7, column=1,columnspan=2, pady=10)

        # Bind the Return key event to the show_selected_options method
        self.root.bind("<Return>", self.show_selected_options)

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

    def close_window(self):
        self.root.destroy()
        sys.exit()


class INFOBOX:
    def __init__(self, root, destination):
        self.root = root
        self.destination = destination
        self.ok = tk.BooleanVar()
        self.create_widgets()

        root.title('Info')
        root.geometry("350x200+10+10")
    def create_widgets(self):

        message = "Eksporter alle planer, doser, bildeserier etc. manuelt til:\n\n"

        btn = tk.Button(self.root, text="OK", command=self.confirm)
        btn.place(x=150, y=110, height=50, width=70)
        lbl = tk.Label(self.root, text=message, fg='black', font=("Helvetica", 10))
        lbl.place(x=10, y=40)
        lbl = tk.Label(self.root, text=self.destination, fg='black', font=("Helvetica",10,"bold"))
        lbl = tk.Label(self.root, text=self.destination, fg='black', font=("Helvetica",10,"bold"))
        lbl.place(x=100, y=60)
        #tk.Label(self.root, text=message).grid(row=0, columnspan=2, pady=10)
        #tk.Button(self.root, text="OK", command=self.confirm).grid(row=2, column=1)
        #self.root.bind("<Return>", self.confirm())
        #self.root.bind("<Escape>", self.cancel())
        # Create a button to trigger the message box
        #ok_button.pack(padx=20, pady=10)

    # TODO: Dersom get parameters but not export is chosen, tell the user to manually export everything to correct folder

    def confirm(self):
        self.ok.set(True)
        self.root.destroy()

    def cancel(self):
        self.root.destroy()




if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
