import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror(
                "Error",
                "Password length must be greater than 0"
            )
            return

        characters = ""

        if letters_var.get():
            characters += string.ascii_letters

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror(
                "Error",
                "Please select at least one character type"
            )
            return

        password = ""

        for i in range(length):
            password += random.choice(characters)

        result_label.config(text=password)

        if length < 8:
            strength_label.config(text="Strength: Weak")

        elif length <= 12:
            strength_label.config(text="Strength: Medium")

        else:
            strength_label.config(text="Strength: Strong")

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid number"
        )

def copy_password():
    password = result_label.cget("text")

    if password:
        window.clipboard_clear()
        window.clipboard_append(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard"
        )

window = tk.Tk()

window.title("Password Generator")
window.geometry("500x450")

title_label = tk.Label(
    window,
    text="Password Generator",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

length_label = tk.Label(
    window,
    text="Enter Password Length:",
    font=("Arial", 11)
)
length_label.pack()

length_entry = tk.Entry(
    window,
    font=("Arial", 11),
    width=20
)
length_entry.pack(pady=5)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

letters_check = tk.Checkbutton(
    window,
    text="Include Letters",
    variable=letters_var
)
letters_check.pack()

numbers_check = tk.Checkbutton(
    window,
    text="Include Numbers",
    variable=numbers_var
)
numbers_check.pack()

symbols_check = tk.Checkbutton(
    window,
    text="Include Symbols",
    variable=symbols_var
)
symbols_check.pack()

generate_button = tk.Button(
    window,
    text="Generate Password",
    font=("Arial", 11, "bold"),
    command=generate_password
)
generate_button.pack(pady=15)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold"),
    wraplength=450
)
result_label.pack(pady=10)

strength_label = tk.Label(
    window,
    text="",
    font=("Arial", 11, "bold")
)
strength_label.pack()

copy_button = tk.Button(
    window,
    text="Copy Password",
    font=("Arial", 11),
    command=copy_password
)
copy_button.pack(pady=10)

window.mainloop()