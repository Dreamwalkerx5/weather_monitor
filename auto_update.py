#  Copyright (c) 2019. Steven Taylor. All rights reserved.

import time
from datetime import datetime

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot


class AutoUpdate(QThread):
    current_weather_signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, kill_signal):
        QThread.__init__(self)

        self.stop_request = False
        self.kill_signal = kill_signal
        self.kill_signal.connect(self.kill)

    def run(self):
        while not self.stop_request:
            self.current_weather_signal.emit('update')
            time.sleep(900)

    @pyqtSlot()
    def kill(self):
        print('Clock thread dying...')
        self.stop_request = True
