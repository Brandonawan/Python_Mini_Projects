import requests
from pprint import pprint

apiKey = 'fe78a462226b37d644590b1b26c3480f'
unit = "metric"

city = input("Enter your city name: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=" + unit +"&&appid=" + apiKey +""

weather_data = requests.get(base_url).json()

# print(weather_data)
pprint(weather_data)
