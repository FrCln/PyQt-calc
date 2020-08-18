# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import typing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDockWidget


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        super().__init__(*args)
        self.setObjectName("MainWindow")
        self.setFixedSize(490, 455)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet(open('style.qss').read())
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 78, 390, 372))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.Button0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button0.setObjectName("digit")
        self.gridLayout.addWidget(self.Button0, 4, 0, 1, 2)
        self.Button1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button1.setObjectName("digit")
        self.gridLayout.addWidget(self.Button1, 1, 0, 1, 1)
        self.Button2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button2.setObjectName("digit")
        self.gridLayout.addWidget(self.Button2, 1, 1, 1, 1)
        self.Button3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button3.setObjectName("digit")
        self.gridLayout.addWidget(self.Button3, 1, 2, 1, 1)
        self.Button4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button4.setObjectName("digit")
        self.gridLayout.addWidget(self.Button4, 2, 0, 1, 1)
        self.Button5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button5.setObjectName("digit")
        self.gridLayout.addWidget(self.Button5, 2, 1, 1, 1)
        self.Button6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button6.setObjectName("digit")
        self.gridLayout.addWidget(self.Button6, 2, 2, 1, 1)
        self.Button7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button7.setObjectName("digit")
        self.gridLayout.addWidget(self.Button7, 3, 0, 1, 1)
        self.Button8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button8.setObjectName("digit")
        self.gridLayout.addWidget(self.Button8, 3, 1, 1, 1)
        self.Button9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button9.setObjectName("digit")
        self.gridLayout.addWidget(self.Button9, 3, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 0, 2, 1, 1)
        self.ButtonCE = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonCE.setObjectName("ButtonCE")
        self.gridLayout.addWidget(self.ButtonCE, 0, 0, 1, 1)
        self.ButtonPoint = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonPoint.setObjectName("ButtonPoint")
        self.gridLayout.addWidget(self.ButtonPoint, 4, 2, 1, 1)
        self.ButtonPM = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonPM.setStyleSheet("")
        self.ButtonPM.setObjectName("ButtonPM")
        self.gridLayout.addWidget(self.ButtonPM, 0, 1, 1, 1)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(405, 0, 80, 450))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ButtonBackspace = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButtonBackspace.setObjectName("ButtonBackspace")
        self.verticalLayout.addWidget(self.ButtonBackspace)
        self.pushButton_15 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_15.setObjectName("action")
        self.verticalLayout.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_16.setObjectName("action")
        self.verticalLayout.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_17.setObjectName("action")
        self.verticalLayout.addWidget(self.pushButton_17)
        self.pushButton_35 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_35.setObjectName("action")
        self.verticalLayout.addWidget(self.pushButton_35)
        self.EqualButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.EqualButton.setObjectName("action")
        self.verticalLayout.addWidget(self.EqualButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5, 0, 330, 70))
        self.label.setObjectName("label")

        self.actionLabel = QtWidgets.QLabel(self.centralwidget)
        self.actionLabel.setGeometry(QtCore.QRect(330, 0, 70, 70))
        self.actionLabel.setObjectName("actionLabel")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "КАЛЬКУЛRТОР"))
        MainWindow.setWindowIcon(QtGui.QIcon('calc.png'))
        self.Button0.setText(_translate("MainWindow", "0"))
        self.Button1.setText(_translate("MainWindow", "1"))
        self.Button2.setText(_translate("MainWindow", "2"))
        self.Button3.setText(_translate("MainWindow", "3"))
        self.Button4.setText(_translate("MainWindow", "4"))
        self.Button5.setText(_translate("MainWindow", "5"))
        self.Button7.setText(_translate("MainWindow", "7"))
        self.Button6.setText(_translate("MainWindow", "6"))
        self.Button8.setText(_translate("MainWindow", "8"))
        self.Button9.setText(_translate("MainWindow", "9"))
        self.ButtonBackspace.setText(_translate("MainWindow", "⌫"))
        self.ButtonCE.setText(_translate("MainWindow", "CE"))
        self.ButtonPoint.setText(_translate("MainWindow", "."))
        self.ButtonPM.setText(_translate("MainWindow", "±"))
        self.pushButton_14.setText(_translate("MainWindow", "%"))
        self.pushButton_15.setText(_translate("MainWindow", "÷"))
        self.pushButton_16.setText(_translate("MainWindow", "×"))
        self.pushButton_17.setText(_translate("MainWindow", "+"))
        self.pushButton_35.setText(_translate("MainWindow", "—"))
        self.EqualButton.setText(_translate("MainWindow", "="))
        self.label.setText(_translate("MainWindow", " 0"))
        self.actionLabel.setText(_translate("MainWindow", ""))

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        k = a0.key()
        if k in range(48, 59):
            for btn in self.findChildren(QtWidgets.QPushButton, 'digit'):
                if btn.text() == chr(k):
                    btn.click()
                    return
        actions = {
            46: self.ButtonPoint,
            43: self.pushButton_17,
            45: self.pushButton_35,
            42: self.pushButton_16,
            47: self.pushButton_15,
            37: self.pushButton_14,
            16777219: self.ButtonBackspace,
            16777220: self.EqualButton,
            16777221: self.EqualButton,
            16777216: self.ButtonCE
        }
        if k in actions:
            actions[k].click()
