import tkinter as tk
from tkinter import ttk
import time

class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Progress Bar Example")

        # Create a progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(pady=20)


    def update_progress(self, iteration):
        self.progress_var.set(iteration)
        if iteration == 100:
            root.destroy()
        pass
        """ for i in range(101):
            self.progress_var.set(i)  # Update the progress bar
            self.root.update()       # Update the tkinter window
            time.sleep(0.1)         # Simulate some work (replace with your actual work)
            if i == 100:
                self.root.destroy()"""

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Progress Bar in Tk")
    progressbar = ttk.Progressbar()
    progressbar.place(x=30, y=60, width=200)
    root.geometry("300x200")
    root.mainloop()






import tkinter as tk
from tkinter import ttk

class ProgressBar:
    def __init__(self, root):
        self.root = root
        self.root.title("Progress")

        # Create a progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(column=0, row=0, columnspan=2, padx=20, pady=20, sticky="ew")

        # Create a label to display progress percentage
        self.value_label = ttk.Label(self.root, text="Progress: 0%")
        self.value_label.grid(column=0, row=1, columnspan=2, pady=10)

        # Create a button to start the progress
        self.start_button = ttk.Button(self.root, text="Start Progress", command=self.start_progress)
        self.start_button.grid(column=0, row=2, padx=10, pady=10, sticky="e")

        # Create a button to reset the progress
        self.reset_button = ttk.Button(self.root, text="Reset", command=self.reset_progress)
        self.reset_button.grid(column=1, row=2, padx=10, pady=10, sticky="w")

        self.progress_value = 0

    def start_progress(self):
        # Simulate progress (update the progress bar and label)
        self.progress_value += 10
        if self.progress_value <= 100:
            self.progress_var.set(self.progress_value)
            self.value_label.config(text="Progress: {}%".format(self.progress_value))
            self.root.after(500, self.start_progress)  # Update every 500ms
        else:
            self.progress_value = 0

    def reset_progress(self):
        # Reset the progress bar and label
        self.progress_var.set(0)
        self.value_label.config(text="Progress: 0%")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressBar(root)
    root.mainloop()


