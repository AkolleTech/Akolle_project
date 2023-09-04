# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginsUniZIo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rc

class Ui_LOGIN(object):
    def setupUi(self, LOGIN):
        if not LOGIN.objectName():
            LOGIN.setObjectName(u"LOGIN")
        LOGIN.resize(400, 602)
        LOGIN.setMaximumSize(QSize(400, 602))
        self.LOG = QWidget(LOGIN)
        self.LOG.setObjectName(u"LOG")
        self.login = QWidget(self.LOG)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(0, 0, 400, 602))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setStyleSheet(u"#login{background-color: rgb(0, 64, 94);\n"
"\n"
"}")
        self.label_14 = QLabel(self.login)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(170, 70, 91, 51))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15 = QLabel(self.login)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(80, 50, 71, 61))
        self.label_15.setPixmap(QPixmap(u":/icon2/icon_white/unlock.svg"))
        self.label_15.setScaledContents(True)
        self.lineEdit_2 = QLineEdit(self.login)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 190, 281, 41))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_3 = QLineEdit(self.login)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(50, 320, 281, 41))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 3px solid #FBAD25\n"
"}")
        self.pushButton_8 = QPushButton(self.login)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(50, 500, 281, 41))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(93, 138, 69);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(92, 138, 138);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon2/icon_white/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QSize(25, 25))
        self.pushButton = QPushButton(self.login)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 330, 41, 23))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon2/icon_white/eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.label = QLabel(self.login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 470, 241, 21))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setUnderline(True)
        font3.setWeight(50)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.pushButton_2 = QPushButton(self.login)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 20, 75, 23))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        LOGIN.setCentralWidget(self.LOG)

        self.retranslateUi(LOGIN)

        QMetaObject.connectSlotsByName(LOGIN)
    # setupUi

    def retranslateUi(self, LOGIN):
        LOGIN.setWindowTitle(QCoreApplication.translate("LOGIN", u"MainWindow", None))
        self.label_14.setText(QCoreApplication.translate("LOGIN", u"Log In", None))
        self.label_15.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("LOGIN", u"Enter User Name", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("LOGIN", u"Enter Password", None))
        self.pushButton_8.setText(QCoreApplication.translate("LOGIN", u"Login", None))
        self.pushButton.setText("")
        self.label.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

