# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 431)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 180, 421, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_scroll = QtWidgets.QScrollBar(self.verticalLayoutWidget)
        self.start_scroll.setOrientation(QtCore.Qt.Horizontal)
        self.start_scroll.setObjectName("start_scroll")
        self.verticalLayout.addWidget(self.start_scroll)
        self.end_scroll = QtWidgets.QScrollBar(self.verticalLayoutWidget)
        self.end_scroll.setOrientation(QtCore.Qt.Horizontal)
        self.end_scroll.setObjectName("end_scroll")
        self.verticalLayout.addWidget(self.end_scroll)
        self.cut_b = QtWidgets.QPushButton(Form)
        self.cut_b.setGeometry(QtCore.QRect(410, 260, 93, 28))
        self.cut_b.setObjectName("cut_b")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 300, 395, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rename_b = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.rename_b.setObjectName("rename_b")
        self.horizontalLayout.addWidget(self.rename_b)
        self.delete_b = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delete_b.setObjectName("delete_b")
        self.horizontalLayout.addWidget(self.delete_b)
        self.speed_b = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.speed_b.setObjectName("speed_b")
        self.horizontalLayout.addWidget(self.speed_b)
        self.copy_b = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.copy_b.setObjectName("copy_b")
        self.horizontalLayout.addWidget(self.copy_b)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 311, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_start = QtWidgets.QLabel(Form)
        self.label_start.setGeometry(QtCore.QRect(40, 187, 50, 20))
        self.label_end = QtWidgets.QLabel(Form)
        self.label_end.setGeometry(QtCore.QRect(505, 225, 50, 20))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cut_b.setText(_translate("Form", "cut"))
        self.rename_b.setText(_translate("Form", "rename"))
        self.delete_b.setText(_translate("Form", "delete"))
        self.copy_b.setText(_translate("Form", "copy"))
        self.speed_b.setText(_translate("Form", "speed"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Welcome to simple mp3 redactor!</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "Proj. mp3 manager by GGergy"))
        self.label_start.setText('0:00')
        self.label_end.setText('0:00')
