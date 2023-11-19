"""
Prayer Times App

This script uses the Aladhan API to fetch and display prayer times based on the user's input of city and country.
The GUI application is built using the tkinter library.

API Documentation: http://aladhan.com/prayer-times-api

Requirements:
- Python 3.x
- requests library (install using: pip install requests)

"""

import requests
import tkinter as tk
from tkinter import ttk, messagebox

# Function to fetch prayer times using the Aladhan API
def fetch_prayer_times(city, country):
    """
    Fetches prayer times using the Aladhan API.

    Args:
        city (str): The name of the city.
        country (str): The name of the country.

    Returns:
        dict: A dictionary containing prayer timings.
    """
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=5"

    try:
        response = requests.get(url)
        info = response.json()

        if "data" in info:
            timings = info["data"]["timings"]
            return timings
        else:
            return None

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Function to handle GUI-based prayer times fetching
def gui_fetch_prayer_times():
    """
    Retrieves user-entered city and country, and fetches prayer times using the Aladhan API.
    Displays the results in the GUI.
    """
    city = city_entry.get()
    country = country_entry.get()

    if city and country:
        prayer_times = fetch_prayer_times(city, country)
        prayer_names = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]
        for name, time in prayer_times.items():
            if name in prayer_names:
                result.insert(tk.END, f"{name}: {time}")

    else:
        messagebox.showerror("Error", "Unable to fetch prayer times. Please enter correct city and country names!")

# Create the main GUI application
app = tk.Tk()
app.title("Prayer Times")
frame = ttk.Frame(app)
frame['padding'] = 20
frame.grid(row=0, column=0)

# Widgets for entering city and country information
city_label = ttk.Label(frame, text="City: ")
city_label.grid(row=0, column=0, pady=10)
country_label = ttk.Label(frame, text="Country: ")
country_label.grid(row=1, column=0, pady=10)

city_entry = ttk.Entry(frame)
city_entry.grid(row=0, column=1, padx=20, pady=10)
country_entry = ttk.Entry(frame)
country_entry.grid(row=1, column=1, padx=20, pady=10)

# Button to fetch prayer times
fetch_button = ttk.Button(frame, text="Get Prayer Times", command=gui_fetch_prayer_times)
fetch_button.grid(row=2, column=1, columnspan=2, padx=20, pady=5)

# Listbox to display the results
result = tk.Listbox(frame, height=15, width=30)
result.grid(row=3, columnspan=3, padx=20, pady=5)

# Run the application
app.mainloop()
