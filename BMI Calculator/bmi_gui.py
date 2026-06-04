import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror(
                "Error",
                "Weight and height must be greater than 0"
            )
            return

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
            suggestion = "Consider a balanced diet and consult a healthcare professional."

        elif bmi < 25:
            category = "Normal Weight"
            suggestion = "Maintain your healthy lifestyle."

        elif bmi < 30:
            category = "Overweight"
            suggestion = "Regular exercise and balanced nutrition may help."

        else:
            category = "Obese"
            suggestion = "Consider consulting a healthcare professional for guidance."

        result_label.config(
            text=f"BMI: {round(bmi, 2)}\n\nCategory: {category}\n\nSuggestion:\n{suggestion}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers"
        )

window = tk.Tk()

window.title("BMI Calculator")
window.geometry("500x450")

title_label = tk.Label(
    window,
    text="BMI Calculator",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

weight_label = tk.Label(
    window,
    text="Enter Weight (kg):",
    font=("Arial", 11)
)
weight_label.pack()

weight_entry = tk.Entry(
    window,
    font=("Arial", 11),
    width=20
)
weight_entry.pack(pady=5)

height_label = tk.Label(
    window,
    text="Enter Height (m):",
    font=("Arial", 11)
)
height_label.pack()

height_entry = tk.Entry(
    window,
    font=("Arial", 11),
    width=20
)
height_entry.pack(pady=5)

calculate_button = tk.Button(
    window,
    text="Calculate BMI",
    font=("Arial", 11, "bold"),
    command=calculate_bmi
)
calculate_button.pack(pady=15)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 11),
    wraplength=400,
    justify="center"
)
result_label.pack(pady=10)

window.mainloop()