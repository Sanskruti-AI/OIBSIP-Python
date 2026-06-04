import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():

    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror(
            "Error",
            "Please enter a city name"
        )
        return

    try:
        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]
        humidity = current["humidity"]
        condition = current["weatherDesc"][0]["value"]
        wind_speed = current["windspeedKmph"]
        feels_like = current["FeelsLikeC"]

        result_label.config(
            text=
            f"City: {city}\n\n"
            f"Temperature: {temperature} °C\n"
            f"Feels Like: {feels_like} °C\n"
            f"Humidity: {humidity}%\n"
            f"Condition: {condition}\n"
            f"Wind Speed: {wind_speed} km/h"
        )

    except:
        messagebox.showerror(
            "Error",
            "Unable to retrieve weather information"
        )

window = tk.Tk()

window.title("Weather App")
window.geometry("550x500")

title_label = tk.Label(
    window,
    text="Weather App",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)

city_label = tk.Label(
    window,
    text="Enter City Name",
    font=("Arial", 11)
)
city_label.pack()

city_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 11)
)
city_entry.pack(pady=10)

get_weather_button = tk.Button(
    window,
    text="Get Weather",
    font=("Arial", 11, "bold"),
    command=get_weather
)
get_weather_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    justify="left",
    wraplength=450
)
result_label.pack(pady=20)

window.mainloop()