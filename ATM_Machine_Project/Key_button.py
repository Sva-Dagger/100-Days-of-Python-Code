import tkinter as tk
from tkinter import messagebox

# Function to handle PIN verification
def verify_pin():
    pin = pin_entry.get()
    if pin == "1234":  # Example PIN
        messagebox.showinfo("Success", "PIN verified successfully!")
        # Additional actions after successful PIN verification
    else:
        messagebox.showerror("Error", "Invalid PIN. Try again!")

# Function to open the PIN entry screen
def pin_entry_screen():
    global pin_entry
    pin_window = tk.Toplevel(root)
    pin_window.title("Enter PIN")
    pin_window.geometry("300x150")

    tk.Label(pin_window, text="Enter your PIN:").pack(pady=10)
    pin_entry = tk.Entry(pin_window, show='*')
    pin_entry.pack(pady=5)

    submit_button = tk.Button(pin_window, text="Submit", command=verify_pin)
    submit_button.pack(pady=10)

# Function to display different menu options
def option_one():
    messagebox.showinfo("Option 1", "Option 1 selected")

def option_two():
    messagebox.showinfo("Option 2", "Option 2 selected")

# Main window setup
root = tk.Tk()
root.title("Menu with PIN Entry")
root.geometry("400x300")

# Create a menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a submenu for options
options_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=options_menu)

options_menu.add_command(label="Option 1", command=option_one)
options_menu.add_command(label="Option 2", command=option_two)

# Add the PIN entry option in the menu
options_menu.add_separator()  # For visual separation
options_menu.add_command(label="Enter PIN", command=pin_entry_screen)

# Run the application
root.mainloop()
