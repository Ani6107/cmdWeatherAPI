import argparse
from sys import argv

import pyfiglet
import requests
from simple_chalk import chalk

API_KEY = "64340192d5573d937101f3cff0869040"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

WEATHER_ICONS = {
    # day icons
    "01d": "🌞",
    "02d": "☁",
    "03d": "⛅",
    "04d": "⚡",
    "09d": "🌤",
    "010d": "🌧️",
    "011d": "🌧️",
    "013d": "🌤️",
    "050d": "⛱️",
   # night icons
    "01d": "🌙",
    "02d": "🌔",
    "03d": "🌓",
    "04d": "🌒",
    "09d": "🌑",
    "010d": "🌧️",
    "011d": "🌧️",
    "013d": "🌝",
    "050d": "🌜",
}

parser = argparse.ArgumentParser(description="Check the weather for a certain country/city")
parser.add_argument("country", help="The country/city to check the weather for")
args = parser.parse_args()

url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code != 200:
    print(chalk.read("Error: Unable to retrieve weather information"))
    exit()

data = response.json()

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
temp_max = data["main"]["temp_max"]
temp_min = data["main"]["temp_min"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Fell like: {feels_like}°C\n"
output += f"Humidity: {humidity}\n"
output += f"Max Temperature: {temp_max}°C\n"
output += f"Min Temperature: {temp_min}°C\n"

print(chalk.green(output))