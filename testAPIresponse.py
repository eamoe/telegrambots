import datetime as dt
import requests
import json

import constants as keys

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
WEATHER_API_KEY = keys.WEATHER_API_KEY
city = "Moscow"


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

url = BASE_URL + "appid=" + WEATHER_API_KEY + "&q=" + city
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

weather_str = f"Temperature in {city}: {temp_celsius:.2f}C." + \
                "\n" + f"Temperature in {city} feels like: {feels_like_celsius:.2f}C." + \
                "\n" + f"Humidity in {city}: {humidity}%." + \
                "\n" + f"Wind speed in {city}: {wind_speed}m/s." + \
                "\n" + f"General weather in {city}: {description}." + \
                "\n" + f"Sun rises in {city} at {sunrise_time} local time." + \
                "\n" + f"Sun sets in {city} at {sunset_time} local time."

print(response)

file = open('api_response.json', 'w')
json.dump(response, file)
file.close()

# print(f"Temperature in {city}: {temp_celsius:.2f}C")
# print(f"Temperature in {city} feels like: {feels_like_celsius:.2f}C")
# print(f"Humidity in {city}: {humidity}%")
# print(f"Wind speed in {city}: {wind_speed}m/s")
# print(f"General weather in {city}: {description}")
# print(f"Sun rises in {city} at {sunrise_time} local time.")
# print(f"Sun sets in {city} at {sunset_time} local time.")
