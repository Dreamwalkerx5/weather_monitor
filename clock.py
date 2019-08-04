#  Copyright (c) 2019. Steven Taylor All rights reserved

import time
from datetime import datetime

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot


class Clock(QThread):
    time_signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, clock_kill_signal):
        QThread.__init__(self)

        self.stop_request = False
        self.kill_signal = clock_kill_signal
        self.kill_signal.connect(self.kill)

    def run(self):
        while not self.stop_request:
            current_time = str(datetime.now())
            self.time_signal.emit(current_time[11:19])
            time.sleep(1)

    @pyqtSlot()
    def kill(self):
        print('Clock thread dying...')
        self.stop_request = True
