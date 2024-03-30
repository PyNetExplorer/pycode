import tkinter as tk
from tkinter import Menu

def say_hello():
    welcome_label.pack_forget()
    output_label.config(text="Hello! This app is created by PyNetExplorer. Follow me on GitHub!")

def about():
    welcome_label.pack_forget()
    output_label.config(text="Apply basic configurations and create web, mail and/or database servers")

def welcome():
    output_label.config(text="Hello! This app is created by PyNetExplorer. Follow me on GitHub!")
# Create the main window
window = tk.Tk()

# Set the title of the window
window.title("Linux Configuration App")

# Set the dimensions of the window (width x height)
window.geometry("1000x600")

# Create a label for the welcome message
welcome_label = tk.Label(window, text="Welcome to Linux Configuration App!", font=("Arial", 20), fg="white")
welcome_label.pack(pady=20)
welcome_label.configure(bg="dark green")

# Create a label for the output
output_label = tk.Label(window, text="", font=("Arial", 16), fg="white")
output_label.pack(pady=10)
output_label.configure(bg="dark green")

# Change color to forest green and font to white
window.configure(bg="dark green")


# Create a menu bar
menubar = Menu(window)
window.config(menu=menubar)

# Create a "File" menu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Welcome", command=welcome_label)
file_menu.add_command(label="Exit", command=window.quit)


# Create an "Actions" menu
actions_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Actions", menu=actions_menu)
actions_menu.add_command(label="Say Hello", command=say_hello)

# Create a "Help" menu
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Run the Tkinter event loop
window.mainloop()