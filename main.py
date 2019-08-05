#  Copyright (c) 2019. Steven Taylor. All rights reserved.
import sys

import pyowm
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QTimer

from clock import Clock
from weather_monitor_gui import Ui_MainWindow

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
        self.current_view = DAY

    def get_current_weather(self):
        # Get weather observation
        leicester = self.owm.weather_at_place('Leicester, GB')
        # Get weather object
        weather = leicester.get_weather()

        current_temp = str(weather.get_temperature('celsius')['temp'])
        current_wind = weather.get_wind()
        current_humidity = str(weather.get_humidity())
        current_status = str(weather.get_detailed_status())

        self.ui.lineEdit.setText(f'Current temp is {current_temp}c with {current_humidity} humidity and'
                                 f' {current_wind["speed"]} mph winds and {current_status}')

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
