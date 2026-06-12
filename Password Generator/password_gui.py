import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():

    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror(
                "Error",
                "Password length should be at least 4"
            )
            return

        characters = ""

        password = ""

        if letters_var.get():
            characters += string.ascii_letters
            password += random.choice(string.ascii_letters)

        if numbers_var.get():
            characters += string.digits
            password += random.choice(string.digits)

        if symbols_var.get():
            characters += string.punctuation
            password += random.choice(string.punctuation)

        if characters == "":
            messagebox.showerror(
                "Error",
                "Select at least one option"
            )
            return


        for i in range(length - len(password)):
            password += random.choice(characters)


        password_list = list(password)

        random.shuffle(password_list)

        password = "".join(password_list)


        result_label.config(
            text=password
        )


        if length < 8:
            strength_label.config(
                text="Strength: Weak"
            )

        elif length <= 12:
            strength_label.config(
                text="Strength: Medium"
            )

        else:
            strength_label.config(
                text="Strength: Strong"
            )


    except ValueError:

        messagebox.showerror(
            "Error",
            "Enter valid password length"
        )



def copy_password():

    password = result_label.cget("text")

    if password:

        window.clipboard_clear()

        window.clipboard_append(password)

        messagebox.showinfo(
            "Copied",
            "Password copied"
        )



window = tk.Tk()

window.title("Password Generator")

window.geometry("500x450")


title = tk.Label(
    window,
    text="Password Generator",
    font=("Arial",18,"bold")
)

title.pack(pady=10)



tk.Label(
    window,
    text="Enter Password Length:"
).pack()


length_entry = tk.Entry(
    window
)

length_entry.pack(pady=5)



letters_var = tk.BooleanVar(value=True)

numbers_var = tk.BooleanVar(value=True)

symbols_var = tk.BooleanVar(value=True)



tk.Checkbutton(
    window,
    text="Include Letters",
    variable=letters_var
).pack()


tk.Checkbutton(
    window,
    text="Include Numbers",
    variable=numbers_var
).pack()


tk.Checkbutton(
    window,
    text="Include Symbols",
    variable=symbols_var
).pack()



tk.Button(
    window,
    text="Generate Password",
    command=generate_password
).pack(pady=15)



result_label = tk.Label(
    window,
    text="",
    font=("Arial",12,"bold")
)

result_label.pack()



strength_label = tk.Label(
    window,
    text=""
)

strength_label.pack()



tk.Button(
    window,
    text="Copy Password",
    command=copy_password
).pack(pady=10)



window.mainloop()
