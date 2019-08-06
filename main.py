#  Copyright (c) 2019. Steven Taylor. All rights reserved.
import sys

import pyowm
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtWidgets import QTableWidgetItem

from clock import Clock
from weather_monitor_gui import Ui_MainWindow
from weather_parser import WeatherParser

# Some constants
DAY = 1
WEEK = 2


class Gui(QtWidgets.QMainWindow):
    api_key = '4991dc8c09ba4024625dcce99ce8e881'
    five_day = 'api.openweathermap.org/data/2.5/forecast?q=Leicester,UK'

    clock_kill_signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        super(Gui, self).__init__()

        # Create main window gui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tableWidget.setHorizontalHeaderLabels(['Date & Time', 'Temp', 'Wind speed', 'Humidity',
                                                       'Sky'])
        self.ui.tableWidget.setColumnWidth(0, 130)
        self.ui.tableWidget.setColumnWidth(1, 50)
        self.ui.tableWidget
        self.ui.tableWidget.setColumnWidth(2, 90)
        self.ui.tableWidget.setColumnWidth(3, 75)
        self.ui.tableWidget.setColumnWidth(4, 150)

        # Create slots
        self.ui.quit_button.clicked.connect(self.quit)
        self.ui.day_radiobutton.clicked.connect(self.change_view)
        self.ui.week_radiobutton.clicked.connect(self.change_view)

        # Create clock thread
        self.clock = Clock(self.clock_kill_signal)
        self.clock.time_signal.connect(self.update_time_label)
        self.clock.start()

        # Authenticate api key
        self.owm = pyowm.OWM(self.api_key)

        # Set display with current weather
        self.get_current_weather()

        # Schedule current weather update
        self.current_weather_timer = QTimer()
        self.current_weather_timer.timeout.connect(self.get_current_weather)
        self.current_weather_timer.start(900000)

        # Set some variables
        self.current_view = WEEK
        self.location = 'Leicester, GB'

        # Set up forecast display
        self.get_forecast()

    def get_current_weather(self):
        # Get weather observation
        leicester = self.owm.weather_at_place('Leicester, GB')
        # Get weather object
        weather = leicester.get_weather()

        current_temp = str(int(weather.get_temperature('celsius')['temp']))
        current_wind = weather.get_wind()
        current_humidity = str(weather.get_humidity()) + '%'
        current_status = str(weather.get_detailed_status())

        self.ui.lineEdit.setText(f'Current temp is {current_temp}C with {current_humidity} humidity and'
                                 f' {current_wind["speed"]} mph winds with {current_status}')

        parser = WeatherParser()
        current_weather = parser.get_current()

    def get_forecast(self):
        forecaster = self.owm.three_hours_forecast(self.location)
        forecast = forecaster.get_forecast()
        weather_list = forecast.get_weathers()

        if self.current_view == WEEK:
            forecast_string = ''

            row = 0
            for weather in weather_list:
                day = weather.get_reference_time('iso')
                temp = str(int(weather.get_temperature(unit="celsius")["temp"]))
                wind = str(weather.get_wind()['speed'])
                humidity = str(weather.get_humidity()) + '%'
                sky = weather.get_detailed_status()

                date = day[:10]
                time = day[11:-6]
                # Reverse date
                date = date[8:] + '-' + date[5:7] + '-' + date[:4]

                self.ui.tableWidget.setRowCount(row + 1)
                day = QTableWidgetItem(date + ' ' + time)
                day.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row, 0, day)
                temp = QTableWidgetItem(temp)
                temp.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row, 1, temp)
                wind = QTableWidgetItem(wind)
                wind.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row, 2, wind)
                humidity = QTableWidgetItem(humidity)
                humidity.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row, 3, humidity)
                sky = QTableWidgetItem(sky)
                sky.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row, 4, sky)

                row += 1
                forecast_string += f'Temp: {weather.get_temperature(unit="celsius")["temp"]}C  ' \
                                   f'Humidity: {weather.get_humidity()}  ' \
                                   f'Winds: {weather.get_wind()["speed"]}mph  ' \
                                   f'Sky: {weather.get_detailed_status()}\n'

        else:
            pass




    def update_time_label(self, time):
        self.ui.time_hours.display(time[:2])
        self.ui.time_minutes.display(time[3:5])

    def change_view(self):
        if self.current_view == DAY:
            self.current_view = WEEK
        else:
            self.current_view = DAY
        print(self.current_view)

    def quit(self):
        self.clock_kill_signal.emit(0)
        self.clock.wait()
        app.quit()


app = QtWidgets.QApplication([])

# Create my GUI
gui = Gui()
gui.show()

# Run main loop
app.exec()

print('Quit...')
sys.exit()
