#  Copyright (c) 2019. Steven Taylor. All rights reserved.
import requests


class WeatherParser:
    api_key = '4991dc8c09ba4024625dcce99ce8e881'
    api_call_five_day = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key + '&q='
    api_call_current = 'https://api.openweathermap.org/data/2.5/weather?appid=' + api_key + '&q='

    def __init__(self, city=None):
        self.city = 'Leicester, GB' if city is None else city

    def get_five_day(self):
        # Get data from weather org as json
        data = requests.get(self.api_call_five_day + self.city).json()

    def get_current(self):
        forecast = []
        # Get data from weather org as json and convert to python objects
        data = requests.get(self.api_call_current + self.city).json()

        if data['cod'] != '404':
            forecast = data['main']
            print(forecast)
            return forecast

        else:
            return forecast


class CurrentWeather:
    def __init__(self, description='', temp=0, min_temp=0, max_temp=0, humidity=0, visibility=0,
                 pressure=0, wind_speed=0, wind_direction=0, clouds=0, sunrise=0, sunset=0):
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
        self.sunrise = sunrise
        self.sunset = sunset

    @staticmethod
    def degrees_to_cardinal(d):
        dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        ix = int((d + 11.25) / 22.5 - 0.02)
        return dirs[ix % 16]
