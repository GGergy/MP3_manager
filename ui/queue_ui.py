# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'que_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class QueueWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("player")
        MainWindow.resize(401, 394)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outw = QtWidgets.QScrollArea(self.centralwidget)
        self.outw.setGeometry(QtCore.QRect(0, 0, 391, 281))
        self.outw.setWidgetResizable(True)
        self.outw.setObjectName("outw")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 389, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.outw.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 290, 77, 83))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.play_b = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.play_b.setObjectName("play_b")
        self.verticalLayout.addWidget(self.play_b)
        self.prew_b = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.prew_b.setObjectName("prew_b")
        self.verticalLayout.addWidget(self.prew_b)
        self.rem_b = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.rem_b.setObjectName("rem_b")
        self.verticalLayout.addWidget(self.rem_b)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(320, 290, 81, 83))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.load_b = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.load_b.setObjectName("load_b")
        self.verticalLayout_2.addWidget(self.load_b)
        self.next_b = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.next_b.setObjectName("next_b")
        self.verticalLayout_2.addWidget(self.next_b)
        self.change_b = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.change_b.setObjectName("change_b")
        self.verticalLayout_2.addWidget(self.change_b)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 290, 221, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.prew_l = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.prew_l.setFont(font)
        self.prew_l.setObjectName("prew_l")
        self.verticalLayout_3.addWidget(self.prew_l)
        self.this_l = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.this_l.setFont(font)
        self.this_l.setObjectName("this_l")
        self.verticalLayout_3.addWidget(self.this_l)
        self.next_l = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.next_l.setFont(font)
        self.next_l.setObjectName("next_l")
        self.verticalLayout_3.addWidget(self.next_l)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("player", "player"))
        self.play_b.setText(_translate("MainWindow", "play"))
        self.prew_b.setText(_translate("MainWindow", "prewious"))
        self.rem_b.setText(_translate("MainWindow", "remove_bg"))
        self.load_b.setText(_translate("MainWindow", "load tracks"))
        self.next_b.setText(_translate("MainWindow", "next"))
        self.change_b.setText(_translate("MainWindow", "change_bg"))
        self.prew_l.setText(_translate("MainWindow", ""))
        self.this_l.setText(_translate("MainWindow", ""))
        self.next_l.setText(_translate("MainWindow", ""))
