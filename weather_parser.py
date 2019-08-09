#  Copyright (c) 2019. Steven Taylor. All rights reserved.
import json
import time
from datetime import datetime

import requests


class WeatherParser:
    api_key = '4991dc8c09ba4024625dcce99ce8e881'
    api_call_five_day = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key + '&q='
    api_call_current = 'https://api.openweathermap.org/data/2.5/weather?appid=' + api_key + '&q='

    def __init__(self, city=None):
        self.city = 'Leicester, GB' if city is None else city

    def change_city(self, new_city):
        self.city = new_city

    def get_five_day(self):
        forecasts = None
        # Get data from weather org as json
        data = requests.get(self.api_call_five_day + self.city).json()

        if data['cod'] != '404':
            forecasts = []
            forecast_list = data['list']
            for f in forecast_list:
                forecast = CurrentWeather(f['weather'][0]['description'], f['main']['temp'],
                                          f['main']['temp_min'], f['main']['temp_max'],
                                          f['main']['humidity'], 0,
                                          f['main']['pressure'], f['wind']['speed'],
                                          f['wind']['deg'],
                                          f['clouds']['all'],
                                          0, 0, f['dt_txt'],
                                          rain_amount=f['rain']['3h'] if 'rain' in f and '3h' in
                                          f['rain'] else 0)
                forecasts.append(forecast)

            return forecasts

        else:
            return forecasts

    def get_current(self):
        forecast = None
        # Get data from weather org as json and convert to python objects
        data = requests.get(self.api_call_current + self.city).json()

        if data['cod'] != '404':
            forecast = CurrentWeather(data['weather'][0]['description'], data['main']['temp'],
                                      data['main']['temp_min'], data['main']['temp_max'],
                                      data['main']['humidity'], data['visibility'],
                                      data['main']['pressure'], data['wind']['speed'],
                                      data['wind']['deg'] if 'deg' in data['wind'] else 0,
                                      data['clouds']['all'],
                                      data['sys']['sunrise'], data['sys']['sunset'])

            return forecast

        else:
            return forecast

    @staticmethod
    def get_attribute(data, attribute, default_value):
        return data.get(attribute) or default_value

    @staticmethod
    def save_json(json_data):
        # Save data to disk as json
        with open('data_file.json', 'w') as write_file:
            json.dump(json_data, write_file, indent=4)


class CurrentWeather:
    def __init__(self, description='', temp=0, min_temp=0, max_temp=0, humidity=0, visibility=0,
                 pressure=0, wind_speed=0, wind_direction=0, clouds=0, sunrise=0, sunset=0,
                 date_time=None, rain_amount=0):

        self.description = description
        self.temp = str(int(temp - 273.15))
        self.min_temp = str(int(min_temp - 273.15))
        self.max_temp = str(int(max_temp - 273.15))
        self.humidity = humidity
        self.visibility = visibility
        self.pressure = pressure
        self.wind_speed = wind_speed
        self.wind_direction = CurrentWeather.degrees_to_cardinal(wind_direction)
        self.clouds = clouds
        self.date_time = date_time
        self.rain_amount = rain_amount

        # Add one hour if British summer time
        if time.localtime().tm_isdst == 1:
            sunrise += 3600
            sunset += 3600

        self.sunrise = datetime.utcfromtimestamp(sunrise)
        self.sunrise = self.sunrise.strftime('%H:%M')
        self.sunset = datetime.utcfromtimestamp(sunset)
        self.sunset = self.sunset.strftime('%H:%M')

    @staticmethod
    def degrees_to_cardinal(d):
        dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        ix = int((d + 11.25) / 22.5 - 0.02)
        return dirs[ix % 16]

    def __str__(self):
        return self.date_time
