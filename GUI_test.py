import tkinter as tk
from tkinter import messagebox

message_boxes = []  # List to store open message boxes

def show_message_box():
    message = "This is a simple message box!"
    box = messagebox.showinfo("Message Box", message)
    message_boxes.append(box)

def close_all_windows():
    for box in message_boxes:
        box.destroy()
    message_boxes.clear()
    root.destroy()  # Close the main window

# Create the main window
root = tk.Tk()
root.title("Message Box Example")

# Create a button to trigger the message box
show_button = tk.Button(root, text="Show Message Box", command=show_message_box)
show_button.pack(padx=20, pady=10)

# Start the tkinter main loop
root.protocol("WM_DELETE_WINDOW", close_all_windows)
root.mainloop()
