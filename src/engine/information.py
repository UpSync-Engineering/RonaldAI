import requests
import os
from dotenv import load_dotenv
load_dotenv()


def convert_kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


# Get weather information for a given city
def get_weather_info(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + os.getenv('OPEN_WEATHER_MAP_API_KEY')
    response = requests.get(url)
    data = response.json()
    return str(data['weather'][0]['main']).upper() + ': ' + data['weather'][0]['description'] + ', (' + str(convert_kelvin_to_fahrenheit(data['main']['temp'])) + '°F)'
