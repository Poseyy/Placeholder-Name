# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Bens-Acer\Desktop\myui3.ui'
#
# Created: Tue Oct 30 21:04:11 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import random
import time
import sensors
class Ui_homeApp(object):
    def setupUi(self, homeApp):
        homeApp.setObjectName("homeApp")
        homeApp.resize(1117, 935)
        self.centralwidget = QtGui.QWidget(homeApp)
        self.centralwidget.setStyleSheet("background-color: rgb(35, 41, 44);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1131, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 51, 63);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.temp_sensor = QtGui.QLabel(self.centralwidget)
        self.temp_sensor.setGeometry(QtCore.QRect(-30, 160, 1151, 131))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.temp_sensor.setFont(font)
        self.temp_sensor.setStyleSheet("color: rgb(255, 255, 255);")
        self.temp_sensor.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_sensor.setObjectName("temp_sensor")
        self.label1 = QtGui.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(-10, 130, 1151, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label5 = QtGui.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(590, 210, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label5.setFont(font)
        self.label5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setObjectName("label5")
        self.label2 = QtGui.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(-10, 250, 1161, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setWeight(75)
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.humidity = QtGui.QLabel(self.centralwidget)
        self.humidity.setGeometry(QtCore.QRect(-30, 310, 1151, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.humidity.setFont(font)
        self.humidity.setStyleSheet("color: rgb(255, 255, 255);")
        self.humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity.setObjectName("humidity")
        self.label7 = QtGui.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(590, 330, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label7.setFont(font)
        self.label7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label7.setAlignment(QtCore.Qt.AlignCenter)
        self.label7.setObjectName("label7")
        self.label3 = QtGui.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(-20, 380, 1161, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setWeight(75)
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.light_sensor = QtGui.QLabel(self.centralwidget)
        self.light_sensor.setGeometry(QtCore.QRect(-20, 450, 1161, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.light_sensor.setFont(font)
        self.light_sensor.setStyleSheet("color: rgb(255, 255, 255);")
        self.light_sensor.setAlignment(QtCore.Qt.AlignCenter)
        self.light_sensor.setObjectName("light_sensor")
        self.label4 = QtGui.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(-20, 510, 1161, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setWeight(75)
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-20, 580, 1151, 381))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 510, 1071, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 380, 1071, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 250, 1071, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.eco2 = QtGui.QLabel(self.centralwidget)
        self.eco2.setGeometry(QtCore.QRect(660, 610, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.eco2.setFont(font)
        self.eco2.setStyleSheet("color: rgb(255, 255, 255);")
        self.eco2.setAlignment(QtCore.Qt.AlignCenter)
        self.eco2.setObjectName("eco2")
        self.on_button = QtGui.QPushButton(self.centralwidget)
        self.on_button.setGeometry(QtCore.QRect(570, 770, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.on_button.setFont(font)
        self.on_button.setStyleSheet("background-color: rgb(72, 173, 57);\n"
"color: rgb(255, 255, 255);")
        self.on_button.setObjectName("on_button")
        self.on_button.clicked.connect(self.turnOnLight)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(20, 670, 1071, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.off_button = QtGui.QPushButton(self.centralwidget)
        self.off_button.setGeometry(QtCore.QRect(430, 770, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.off_button.setFont(font)
        self.off_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 103, 89);")
        self.off_button.setObjectName("off_button")
        self.off_button.clicked.connect(self.turnOffLight)
        self.label4_2 = QtGui.QLabel(self.centralwidget)
        self.label4_2.setGeometry(QtCore.QRect(-20, 690, 1161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setWeight(75)
        font.setBold(True)
        self.label4_2.setFont(font)
        self.label4_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_2.setObjectName("label4_2")
        self.label11 = QtGui.QLabel(self.centralwidget)
        self.label11.setGeometry(QtCore.QRect(590, 610, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label11.setFont(font)
        self.label11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label11.setAlignment(QtCore.Qt.AlignCenter)
        self.label11.setObjectName("label11")
        self.label12 = QtGui.QLabel(self.centralwidget)
        self.label12.setGeometry(QtCore.QRect(420, 610, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label12.setFont(font)
        self.label12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label12.setAlignment(QtCore.Qt.AlignCenter)
        self.label12.setObjectName("label12")
        self.tvocs = QtGui.QLabel(self.centralwidget)
        self.tvocs.setGeometry(QtCore.QRect(500, 610, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.tvocs.setFont(font)
        self.tvocs.setStyleSheet("color: rgb(255, 255, 255);")
        self.tvocs.setAlignment(QtCore.Qt.AlignCenter)
        self.tvocs.setObjectName("tvocs")
        homeApp.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(homeApp)
        self.statusbar.setObjectName("statusbar")
        homeApp.setStatusBar(self.statusbar)

        self.retranslateUi(homeApp)
        QtCore.QMetaObject.connectSlotsByName(homeApp)

    def retranslateUi(self, homeApp):
        homeApp.setWindowTitle(QtGui.QApplication.translate("homeApp", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("homeApp", "Welcome to the Home Automation Project", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_sensor.setText(QtGui.QApplication.translate("homeApp", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("homeApp", "Temperature", None, QtGui.QApplication.UnicodeUTF8))
        self.label5.setText(QtGui.QApplication.translate("homeApp", "°F", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("homeApp", "Humidity", None, QtGui.QApplication.UnicodeUTF8))
        self.humidity.setText(QtGui.QApplication.translate("homeApp", "0.0%", None, QtGui.QApplication.UnicodeUTF8))
        self.label7.setText(QtGui.QApplication.translate("homeApp", "RH", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("homeApp", "Lighting", None, QtGui.QApplication.UnicodeUTF8))
        self.light_sensor.setText(QtGui.QApplication.translate("homeApp", "OFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label4.setText(QtGui.QApplication.translate("homeApp", "Air Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.eco2.setText(QtGui.QApplication.translate("homeApp", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.on_button.setText(QtGui.QApplication.translate("homeApp", "ON", None, QtGui.QApplication.UnicodeUTF8))
        self.off_button.setText(QtGui.QApplication.translate("homeApp", "OFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label4_2.setText(QtGui.QApplication.translate("homeApp", "Light Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label11.setText(QtGui.QApplication.translate("homeApp", "eCO₂:", None, QtGui.QApplication.UnicodeUTF8))
        self.label12.setText(QtGui.QApplication.translate("homeApp", "TVOCs:", None, QtGui.QApplication.UnicodeUTF8))
        self.tvocs.setText(QtGui.QApplication.translate("homeApp", "0.0", None, QtGui.QApplication.UnicodeUTF8))
    def turnOnLight(self):
        self.light_sensor.setText("ON")
        sensors.RedLight(1)
        print("Turned on red light")
    def turnOffLight(self):
        self.light_sensor.setText("OFF")
        sensors.RedLight(0)
        print("Turned off red light")
    def refreshText(self):

        time = QtCore.QTime.currentTime().toString()
        print("Time: " + time)

        temp_sensor = "%.2f " % sensors.readTemperature()
        humidity_sensor = "%.2f " % sensors.readHumidity()

        self.temp_sensor.setText(str(temp_sensor))
        self.humidity.setText(str(humidity_sensor)+"%")


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_homeApp()
    ui.setupUi(MainWindow)
    MainWindow.show()


    timer=QtCore.QTimer()
    timer.timeout.connect(ui.refreshText)
    timer.start(1000)

    sys.exit(app.exec_())

def generateRandowNumber():
    return random.randint(1,101)

if __name__ == '__main__':
    # App.main()
    main()
