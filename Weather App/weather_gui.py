import tkinter as tk
from tkinter import messagebox
import requests
import re


def get_weather():

    city = city_entry.get().strip()

    # 1. Empty check
    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    # 2. Strict validation (ONLY letters and spaces allowed)
    if not re.fullmatch(r"[a-zA-Z ]+", city):
        messagebox.showerror("Error", "City name must contain only letters")
        return

    # 3. Length check
    if len(city.replace(" ", "")) < 3:
        messagebox.showerror("Error", "Enter a valid city name (at least 3 letters)")
        return

    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)

        data = response.json()

        if "current_condition" not in data:
            messagebox.showerror("Error", "City not found")
            return

        current = data["current_condition"][0]

        temperature = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        condition = current["weatherDesc"][0]["value"]
        wind_speed = current["windspeedKmph"]

        result_label.config(
            text=
            f"City: {city}\n\n"
            f"Temperature: {temperature} °C\n"
            f"Feels Like: {feels_like} °C\n"
            f"Humidity: {humidity}%\n"
            f"Condition: {condition}\n"
            f"Wind Speed: {wind_speed} km/h"
        )

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Network error")

    except:
        messagebox.showerror("Error", "Something went wrong")


# ---------------- UI ---------------- #

window = tk.Tk()
window.title("Weather App")
window.geometry("500x450")


tk.Label(
    window,
    text="Weather App",
    font=("Arial", 18, "bold")
).pack(pady=10)


city_entry = tk.Entry(window, font=("Arial", 12))
city_entry.pack(pady=10)


tk.Button(
    window,
    text="Get Weather",
    font=("Arial", 11, "bold"),
    command=get_weather
).pack(pady=10)


result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    justify="left"
)
result_label.pack(pady=20)


window.mainloop()
