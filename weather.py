import requests
import json

# The city that you live in
city = "Markham"
state = "Ontario"
# API Key
api_key = "036655339f34ad88bc99eb184996a326"
# Base address for OpenWeatherMap
base_address = "https://api.openweathermap.org/data/2.5/weather"


# Returns the current temperature in degrees Celsius
def getWeather():
    payload = {
        "q": city,
        "appid": api_key
    }
    r = requests.get(base_address, params=payload)
    json_data = json.loads(r.text)
    description = json_data['weather'][0]['main']
    temperature = int(float(json_data['main']['temp']) - 273.15)
    print([temperature, description])
    return [temperature, description]

# Returns the current location
def getLocation():
    return city + ", " + state

getWeather()