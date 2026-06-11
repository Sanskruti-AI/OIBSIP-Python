import tkinter as tk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_m = float(height_entry.get())

        if weight <= 0 or height_m <= 0:
            messagebox.showerror(
                "Error",
                "Weight and height must be greater than 0"
            )
            return

        bmi = weight / (height_m * height_m)

        if bmi < 18.5:
            category = "Underweight"
            suggestion = "Consider a balanced diet."

        elif bmi < 25:
            category = "Normal Weight"
            suggestion = "Maintain your healthy lifestyle."

        elif bmi < 30:
            category = "Overweight"
            suggestion = "Regular exercise may help."

        else:
            category = "Obese"
            suggestion = "Consult a healthcare professional."

        result_label.config(
            text=f"BMI: {round(bmi, 2)}\n\nCategory: {category}\n\nSuggestion:\n{suggestion}"
        )

        with open("bmi_history.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([round(bmi, 2)])

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers"
        )


def view_history():
    try:
        history_window = tk.Toplevel(window)
        history_window.title("BMI History")
        history_window.geometry("300x300")

        text_box = tk.Text(history_window)
        text_box.pack(fill="both", expand=True)

        with open("bmi_history.csv", "r") as file:
            text_box.insert("end", file.read())

    except:
        messagebox.showerror(
            "Error",
            "No history available"
        )


def show_graph():
    try:
        bmi_values = []

        with open("bmi_history.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                bmi_values.append(float(row[0]))

        plt.plot(bmi_values, marker="o")
        plt.title("BMI Trend Analysis")
        plt.xlabel("Record Number")
        plt.ylabel("BMI")
        plt.grid(True)
        plt.show()

    except:
        messagebox.showerror(
            "Error",
            "No graph data available"
        )


window = tk.Tk()

window.title("Advanced BMI Calculator")
window.geometry("500x550")

title_label = tk.Label(
    window,
    text="Advanced BMI Calculator",
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
    text="Enter Height (meters):",
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
calculate_button.pack(pady=10)

history_button = tk.Button(
    window,
    text="View History",
    font=("Arial", 11),
    command=view_history
)
history_button.pack(pady=5)

graph_button = tk.Button(
    window,
    text="Show BMI Graph",
    font=("Arial", 11),
    command=show_graph
)
graph_button.pack(pady=5)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 11),
    wraplength=400,
    justify="center"
)
result_label.pack(pady=15)

window.mainloop()
