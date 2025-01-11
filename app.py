import tkinter as tk
from tkinter import messagebox
import requests

def get_weather_data(location, api_key):
    """Fetches weather data for the given location from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", "Invalid city name or network issue.")
        return None

def display_weather_data():
    """Displays the weather data in the Tkinter window."""
    location = entry.get()
    if location:
        weather_data = get_weather_data(location, api_key)
        if weather_data:
            city = weather_data['name']
            country = weather_data['sys']['country']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            description = weather_data['weather'][0]['description']

            # Displaying the weather data on the GUI
            result_label.config(text=f"Weather in {city}, {country}:\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nCondition: {description.capitalize()}")
        else:
            result_label.config(text="")
    else:
        messagebox.showerror("Input Error", "Please enter a city name.")

def on_close():
    """Handles the window close event."""
    root.quit()

# API Key (replace with your actual key)
api_key = "4444209927481f9b89697511896f6e19"

# Setting up the Tkinter GUI
root = tk.Tk()
root.title("Weather App")

label = tk.Label(root, text="Enter City Name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

search_button = tk.Button(root, text="Get Weather", command=display_weather_data)
search_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
