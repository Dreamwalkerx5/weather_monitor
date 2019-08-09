#  Copyright (c) 2019. Steven Taylor. All rights reserved.
import sys
from datetime import datetime
from time import strftime

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
                                                       'Description', 'Rain fall'])
        self.ui.tableWidget.setColumnWidth(0, 135)
        self.ui.tableWidget.setColumnWidth(1, 50)
        self.ui.tableWidget
        self.ui.tableWidget.setColumnWidth(2, 90)
        self.ui.tableWidget.setColumnWidth(3, 75)
        self.ui.tableWidget.setColumnWidth(4, 150)
        self.ui.tableWidget.setColumnWidth(5, 150)

        # Create slots
        self.ui.quit_button.clicked.connect(self.quit)
        self.ui.day_radiobutton.clicked.connect(self.change_view)
        self.ui.week_radiobutton.clicked.connect(self.change_view)
        

        # Create clock thread
        self.clock = Clock(self.clock_kill_signal)
        self.clock.time_signal.connect(self.update_time_label)
        self.clock.start()

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

    def update_city(self, result):
        # city = self.ui.lineEdit.getText()
        print('lineEdit...')

    def get_current_weather(self):
        parser = WeatherParser()
        w = parser.get_current()

        if w is not None:
            self.ui.lineEdit.setText(f'Current temp is {w.temp}C with {w.humidity}% humidity and'
                                     f' {w.wind_speed} mph winds from the {w.wind_direction}'
                                     f' with {w.description}. Sunset {w.sunset}')

        else:
            self.ui.lineEdit.setText('Sorry, that city was not found.')

    def get_forecast(self):
        today = datetime.today()
        # today = today.strftime("%d")

        if self.current_view == WEEK:
            parser = WeatherParser(self.location)
            w = parser.get_five_day()

            if w is not None:
                row = 0
                for f in w:
                    day = f.date_time
                    temp = f.temp
                    wind = str(int(f.wind_speed)) + ' mph'
                    humidity = str(f.humidity) + '%'
                    sky = f.description
                    rain_fall = str(f.rain_amount) + ' inches'

                    date = day[:10]
                    time = day[11:-3]
                    # Convert date string to datetime object
                    date = datetime.strptime(date, '%Y-%m-%d')
                    # Convert time string to datetime object
                    time = datetime.strptime(time, '%H:%M')
                    # Convert datetime object new string in 12h format
                    time = time.strftime('%I:%M %p')

                    # Convert date to day of week
                    if date.day == today.day:
                        date = "Today"
                    else:
                        # Convert date to week day
                        date = date.strftime('%A')

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
                    rain_fall = QTableWidgetItem(rain_fall)
                    rain_fall.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.ui.tableWidget.setItem(row, 5, rain_fall)

                    row += 1

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
sys.exit(0)
