import os
from dotenv import load_dotenv
import requests

def get_weather_data(location):
    """
    Fetch weather data for a location using a weather API (AQICN or similar).
    """
    load_dotenv()

    # Fetch the API key from the environment
    api_key = os.getenv('WEATHER_API_KEY')
    url = f"https://api.waqi.info/feed/geo:{location[0]};{location[1]}/?token={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Weather API Error: {response.status_code}")
        return None
