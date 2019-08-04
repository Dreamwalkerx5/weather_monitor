#  Copyright (c) 2019. Steven Taylor. All rights reserved.
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from clock import Clock

from weather_monitor_gui import Ui_MainWindow


class Gui(QtWidgets.QMainWindow):
    api = '4991dc8c09ba4024625dcce99ce8e881'
    clock_kill_signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        super(Gui, self).__init__()

        # Create main window gui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create slots
        self.ui.quit_button.clicked.connect(self.quit)

        # Create clock thread
        self.clock = Clock(self.clock_kill_signal)
        self.clock.time_signal.connect(self.update_time_label)

    def update_time_label(self, time):
        pass

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
