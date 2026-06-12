import tkinter as tk
from tkinter import messagebox
import requests


def get_weather():

    city = city_entry.get().strip()

    # Step 1: Check empty input
    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    try:
        # Step 2: API call
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)

        data = response.json()

        # Step 3: Get weather data
        current = data["current_condition"][0]

        temperature = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        condition = current["weatherDesc"][0]["value"]
        wind_speed = current["windspeedKmph"]

        # Step 4: Show result
        result_label.config(
            text=
            "City: " + city + "\n\n" +
            "Temperature: " + temperature + " °C\n" +
            "Feels Like: " + feels_like + " °C\n" +
            "Humidity: " + humidity + "%\n" +
            "Condition: " + condition + "\n" +
            "Wind Speed: " + wind_speed + " km/h"
        )

    except:
        messagebox.showerror("Error", "Unable to fetch weather data")


# UI WINDOW
window = tk.Tk()
window.title("Weather App")
window.geometry("500x450")


# Title
tk.Label(
    window,
    text="Weather App",
    font=("Arial", 18, "bold")
).pack(pady=10)


# City input
city_entry = tk.Entry(window, font=("Arial", 12))
city_entry.pack(pady=10)


# Button
tk.Button(
    window,
    text="Get Weather",
    font=("Arial", 11, "bold"),
    command=get_weather
).pack(pady=10)


# Output label
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    justify="left"
)
result_label.pack(pady=20)


window.mainloop()
