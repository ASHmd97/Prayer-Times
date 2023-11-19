import requests

def fetch_prayer_times(city, country):
    """
    Fetches prayer times for a given city and country using the Aladhan API.

    Args:
        city (str): The name of the city.
        country (str): The name of the country.

    Returns:
        dict: A dictionary containing prayer timings if successful, otherwise None.
        If an error occurs during the API request, a string with an error message is returned.
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

# Get user input for city and country
city = input('Enter city name: ')
country = input('Enter country name: ')

# Check if both city and country are provided
if city and country:
    # Fetch prayer times for the given city and country
    prayer_times = fetch_prayer_times(city, country)

    # List of prayer names to display
    prayer_names = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]
  
    # Display prayer times
    for name, time in prayer_times.items():
        if name in prayer_names:
            print(f"{name}: {time}")

else:
    print("Unable to fetch prayer times. Please provide both city and country.")

