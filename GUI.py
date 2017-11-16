# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 299)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setEnabled(True)
        self.Play.setObjectName("Play")
        self.gridLayout.addWidget(self.Play, 1, 2, 1, 1)
        self.randomVolume = QtWidgets.QPushButton(self.centralwidget)
        self.randomVolume.setObjectName("randomVolume")
        self.gridLayout.addWidget(self.randomVolume, 3, 2, 1, 1)
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setObjectName("Stop")
        self.gridLayout.addWidget(self.Stop, 2, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.listWidget, self.Play)
        MainWindow.setTabOrder(self.Play, self.Stop)
        MainWindow.setTabOrder(self.Stop, self.randomVolume)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Play.setText(_translate("MainWindow", "Play"))
        self.randomVolume.setText(_translate("MainWindow", "Random Volume"))
        self.Stop.setText(_translate("MainWindow", "Stop"))

