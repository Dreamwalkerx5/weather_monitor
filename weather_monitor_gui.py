# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\steve\PycharmProjects\weather_monitor2\weather_monitor_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 799)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setGeometry(QtCore.QRect(970, 700, 93, 28))
        self.quit_button.setObjectName("quit_button")
        self.time_hours = QtWidgets.QLCDNumber(self.centralwidget)
        self.time_hours.setGeometry(QtCore.QRect(890, 20, 71, 61))
        self.time_hours.setDigitCount(2)
        self.time_hours.setMode(QtWidgets.QLCDNumber.Dec)
        self.time_hours.setProperty("intValue", 55)
        self.time_hours.setObjectName("time_hours")
        self.time_minutes = QtWidgets.QLCDNumber(self.centralwidget)
        self.time_minutes.setGeometry(QtCore.QRect(960, 20, 71, 61))
        self.time_minutes.setDigitCount(2)
        self.time_minutes.setMode(QtWidgets.QLCDNumber.Dec)
        self.time_minutes.setProperty("intValue", 55)
        self.time_minutes.setObjectName("time_minutes")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 10, 101, 21))
        self.label.setObjectName("label")
        self.day_radiobutton = QtWidgets.QRadioButton(self.centralwidget)
        self.day_radiobutton.setGeometry(QtCore.QRect(880, 150, 95, 20))
        self.day_radiobutton.setChecked(False)
        self.day_radiobutton.setObjectName("day_radiobutton")
        self.week_radiobutton = QtWidgets.QRadioButton(self.centralwidget)
        self.week_radiobutton.setGeometry(QtCore.QRect(880, 190, 95, 20))
        self.week_radiobutton.setChecked(True)
        self.week_radiobutton.setObjectName("week_radiobutton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 831, 471))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.city_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.city_edit.setGeometry(QtCore.QRect(60, 610, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.city_edit.setFont(font)
        self.city_edit.setObjectName("city_edit")
        self.city_button = QtWidgets.QPushButton(self.centralwidget)
        self.city_button.setGeometry(QtCore.QRect(320, 610, 93, 31))
        self.city_button.setObjectName("city_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather Monitor v1.0"))
        self.quit_button.setText(_translate("MainWindow", "Quit"))
        self.lineEdit.setText(_translate("MainWindow", "test"))
        self.label.setText(_translate("MainWindow", "Current weather"))
        self.day_radiobutton.setText(_translate("MainWindow", "Day"))
        self.week_radiobutton.setText(_translate("MainWindow", "Week"))
        self.city_edit.setToolTip(_translate("MainWindow", "City"))
        self.city_button.setText(_translate("MainWindow", "Update city"))
