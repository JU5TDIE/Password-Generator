# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(248, 177)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_length = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_length.setGeometry(QtCore.QRect(50, 16, 51, 21))
        self.lineEdit_length.setText("")
        self.lineEdit_length.setObjectName("lineEdit_length")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 19, 41, 16))
        self.label.setObjectName("label")
        self.checkBox_punctuation = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_punctuation.setGeometry(QtCore.QRect(170, 50, 71, 16))
        self.checkBox_punctuation.setObjectName("checkBox_punctuation")
        self.checkBox_ascii = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_ascii.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.checkBox_ascii.setObjectName("checkBox_ascii")
        self.checkBox_digits = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_digits.setGeometry(QtCore.QRect(120, 50, 51, 16))
        self.checkBox_digits.setObjectName("checkBox_digits")
        self.textBrowser_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_output.setGeometry(QtCore.QRect(20, 120, 201, 31))
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.pushButton_generate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_generate.setGeometry(QtCore.QRect(60, 80, 121, 31))
        self.pushButton_generate.setObjectName("pushButton_generate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_generate.clicked.connect(MainWindow.generate)
        self.checkBox_ascii.clicked.connect(MainWindow.setting)
        self.checkBox_digits.clicked.connect(MainWindow.setting)
        self.checkBox_punctuation.clicked.connect(MainWindow.setting)
        self.lineEdit_length.textChanged['QString'].connect(MainWindow.on_text_changed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PassGen"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>길이:</p></body></html>"))
        self.checkBox_punctuation.setText(_translate("MainWindow", "특수문자"))
        self.checkBox_ascii.setText(_translate("MainWindow", "대문자 + 소문자"))
        self.checkBox_digits.setText(_translate("MainWindow", "숫자"))
        self.pushButton_generate.setText(_translate("MainWindow", "생성"))
import images
