# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcombgSJHS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rc

class Ui_WeLLC(object):
    def setupUi(self, WeLLC):
        if not WeLLC.objectName():
            WeLLC.setObjectName(u"WeLLC")
        WeLLC.resize(761, 561)
        WeLLC.setMaximumSize(QSize(761, 561))
        self.Wells = QWidget(WeLLC)
        self.Wells.setObjectName(u"Wells")
        self.horizontalLayout = QHBoxLayout(self.Wells)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.welcom = QWidget(self.Wells)
        self.welcom.setObjectName(u"welcom")
        self.welcom.setMinimumSize(QSize(761, 555))
        self.welcom.setMaximumSize(QSize(761, 561))
        self.welcom.setStyleSheet(u"\n"
"background-color: rgb(0, 39, 59);")
        self.label_11 = QLabel(self.welcom)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(270, 30, 191, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(138, 138, 103);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.welcom)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(210, 330, 351, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: rgb(138, 138, 103);")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.welcom)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 70, 741, 101))
        self.label_13.setStyleSheet(u"")
        self.label_13.setPixmap(QPixmap(u":/polic/picture/PicsArt_02-15-10.50.55.jpg"))
        self.label_13.setScaledContents(True)
        self.log_in = QPushButton(self.welcom)
        self.log_in.setObjectName(u"log_in")
        self.log_in.setGeometry(QRect(270, 380, 211, 31))
        font2 = QFont()
        font2.setPointSize(15)
        self.log_in.setFont(font2)
        self.log_in.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(92, 138, 138);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon1/icons/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.log_in.setIcon(icon)
        self.log_in.setIconSize(QSize(30, 30))
        self.log_in_2 = QPushButton(self.welcom)
        self.log_in_2.setObjectName(u"log_in_2")
        self.log_in_2.setGeometry(QRect(200, 460, 341, 31))
        self.log_in_2.setFont(font2)
        self.log_in_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(92, 138, 138);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon2/icon_white/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.log_in_2.setIcon(icon1)
        self.log_in_2.setIconSize(QSize(30, 30))
        self.log_in_3 = QPushButton(self.welcom)
        self.log_in_3.setObjectName(u"log_in_3")
        self.log_in_3.setGeometry(QRect(670, 520, 81, 31))
        self.log_in_3.setFont(font2)
        self.log_in_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(92, 138, 138);\n"
"}")
        self.log_in_3.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.welcom)

        WeLLC.setCentralWidget(self.Wells)

        self.retranslateUi(WeLLC)

        QMetaObject.connectSlotsByName(WeLLC)
    # setupUi

    def retranslateUi(self, WeLLC):
        WeLLC.setWindowTitle(QCoreApplication.translate("WeLLC", u"MainWindow", None))
        self.label_11.setText(QCoreApplication.translate("WeLLC", u"Welcome To", None))
        self.label_12.setText(QCoreApplication.translate("WeLLC", u"Press Login Button To Sign In Your Accounts", None))
        self.label_13.setText("")
        self.log_in.setText(QCoreApplication.translate("WeLLC", u"Log In", None))
        self.log_in_2.setText(QCoreApplication.translate("WeLLC", u"Log In to Adminster Account", None))
        self.log_in_3.setText(QCoreApplication.translate("WeLLC", u"Close", None))
    # retranslateUi

