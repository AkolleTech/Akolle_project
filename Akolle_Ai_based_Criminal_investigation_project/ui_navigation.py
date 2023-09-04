# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'navigationNxnfPK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(852, 555)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"color: #000;\n"
"border: none;\n"
"}\n"
"#frame_1{background-color:#2596be;\n"
"	\n"
"}\n"
"#centralwidget\n"
"{\n"
"	background-color: rgb(175, 175, 175);\n"
"}\n"
"QLineEdit{\n"
"background-color: transparent;\n"
"}\n"
"#search{\n"
"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"}\n"
"#appname{\n"
"color:#2596be;\n"
"}\n"
"#home_btn{\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"#adimnster_btn{\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"#Help{\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"#language_btn{\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"#help_btn{\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 35))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icon2/icon_white/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(221, 221, 221);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon2/icon_white/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(221, 221, 221);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon2/icon_white/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(20, 16))

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(204, 0, 0);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icon2/icon_white/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.left = QCustomSlideMenu(self.widget_2)
        self.left.setObjectName(u"left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy1)
        self.left.setMinimumSize(QSize(0, 489))
        self.left.setMaximumSize(QSize(0, 16777215))
        self.left.setAutoFillBackground(False)
        self.left.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.left)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_1 = QFrame(self.left)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(9, 9, 0, 0)
        self.frame_3 = QFrame(self.frame_1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 20)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_6)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.frame_1)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(6, 0, 0, 250)
        self.home_btn = QPushButton(self.frame_5)
        self.home_btn.setObjectName(u"home_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_btn.sizePolicy().hasHeightForWidth())
        self.home_btn.setSizePolicy(sizePolicy2)
        self.home_btn.setMinimumSize(QSize(170, 25))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.home_btn.setFont(font3)
        self.home_btn.setStyleSheet(u"QPushButton:hover{background-color: rgb(223, 223, 223);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon2/icon_white/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon4)
        self.home_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.home_btn, 0, Qt.AlignLeft)

        self.adimnster_btn = QPushButton(self.frame_5)
        self.adimnster_btn.setObjectName(u"adimnster_btn")
        self.adimnster_btn.setMinimumSize(QSize(170, 25))
        self.adimnster_btn.setFont(font3)
        self.adimnster_btn.setStyleSheet(u"QPushButton:hover{background-color: rgb(223, 223, 223);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon2/icon_white/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.adimnster_btn.setIcon(icon5)
        self.adimnster_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.adimnster_btn, 0, Qt.AlignLeft)

        self.Help = QPushButton(self.frame_5)
        self.Help.setObjectName(u"Help")
        self.Help.setMinimumSize(QSize(170, 25))
        self.Help.setFont(font3)
        self.Help.setStyleSheet(u"QPushButton:hover{background-color: rgb(223, 223, 223);\n"
"}")
        self.Help.setIcon(icon)
        self.Help.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Help, 0, Qt.AlignLeft)

        self.language_btn = QPushButton(self.frame_5)
        self.language_btn.setObjectName(u"language_btn")
        self.language_btn.setMinimumSize(QSize(170, 25))
        self.language_btn.setFont(font3)
        self.language_btn.setStyleSheet(u"QPushButton:hover{background-color: rgb(223, 223, 223);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icon2/icon_white/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.language_btn.setIcon(icon6)
        self.language_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.language_btn, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_5, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_1)


        self.horizontalLayout_11.addWidget(self.left, 0, Qt.AlignLeft)

        self.body = QWidget(self.widget_2)
        self.body.setObjectName(u"body")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy3)
        self.body.setStyleSheet(u"QWidget#body{\n"
"background-color: qlineargradient(spread:pad, x1:0.159, y1:0.170455, x2:1, y2:1, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.body)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.body)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.header)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.widget_3)
        self.menu_btn.setObjectName(u"menu_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icon2/icon_white/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon7)
        self.menu_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.menu_btn, 0, Qt.AlignLeft)


        self.horizontalLayout_4.addWidget(self.widget_3)

        self.widget_15 = QWidget(self.header)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy3.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy3)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.widget_15)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(70, 70))
        self.label_23.setPixmap(QPixmap(u":/polic/PicsArt_02-27-12.33.46.png"))
        self.label_23.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_23)

        self.label_2 = QLabel(self.widget_15)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_2, 0, Qt.AlignLeft)


        self.horizontalLayout_4.addWidget(self.widget_15)

        self.widget_5 = QWidget(self.header)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.account_btn = QPushButton(self.widget_5)
        self.account_btn.setObjectName(u"account_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icon2/icon_white/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.account_btn.setIcon(icon8)
        self.account_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.account_btn, 0, Qt.AlignRight)


        self.horizontalLayout_4.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.header, 0, Qt.AlignTop)

        self.main = QWidget(self.body)
        self.main.setObjectName(u"main")
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.main)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.stackedWidget = QCustomStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(800, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"QWidget#body{\n"
"background-color: qlineargradient(spread:pad, x1:0.159, y1:0.170455, x2:1, y2:1, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_10 = QVBoxLayout(self.page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_12 = QWidget(self.page)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy4)
        self.widget_12.setMinimumSize(QSize(0, 316))
        self.widget_12.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_39 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_39.setSpacing(10)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_12)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy)
        self.widget_16.setMinimumSize(QSize(300, 0))
        self.verticalLayout_12 = QVBoxLayout(self.widget_16)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_16)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(408, 300))
        self.label_7.setMaximumSize(QSize(600, 16777215))
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_7)

        self.lineEdit = QLineEdit(self.widget_16)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.verticalLayout_12.addWidget(self.lineEdit, 0, Qt.AlignBottom)


        self.horizontalLayout_39.addWidget(self.widget_16)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy3.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy3)
        self.widget_14.setMaximumSize(QSize(800, 16777215))
        self.widget_14.setStyleSheet(u"background-color: rgb(56, 56, 84);")
        self.verticalLayout_11 = QVBoxLayout(self.widget_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_25 = QFrame(self.widget_14)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, 0, 0, 0)
        self.label_22 = QLabel(self.frame_25)
        self.label_22.setObjectName(u"label_22")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_38.addWidget(self.label_22, 0, Qt.AlignLeft)

        self.lineEdit_13 = QLineEdit(self.frame_25)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(200, 30))
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.lineEdit_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_13.setReadOnly(True)

        self.horizontalLayout_38.addWidget(self.lineEdit_13, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_25)

        self.frame_17 = QFrame(self.widget_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 0, 0, 0)
        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_29.addWidget(self.label_9)

        self.lineEdit_11 = QLineEdit(self.frame_17)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(200, 30))
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.lineEdit_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_11.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.lineEdit_11, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.widget_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 0, 0, 0)
        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_33.addWidget(self.label_20, 0, Qt.AlignLeft)

        self.lineEdit_17 = QLineEdit(self.frame_18)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(200, 30))
        self.lineEdit_17.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.lineEdit_17.setReadOnly(True)

        self.horizontalLayout_33.addWidget(self.lineEdit_17, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.widget_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 0, 0, 0)
        self.label_15 = QLabel(self.frame_19)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.label_15, 0, Qt.AlignLeft)

        self.lineEdit_16 = QLineEdit(self.frame_19)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(200, 30))
        self.lineEdit_16.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.lineEdit_16.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.lineEdit_16, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.widget_14)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, 0, 0, 0)
        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_31.addWidget(self.label_18, 0, Qt.AlignLeft)

        self.lineEdit_14 = QLineEdit(self.frame_20)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(200, 30))
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.lineEdit_14.setReadOnly(True)

        self.horizontalLayout_31.addWidget(self.lineEdit_14, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.widget_14)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, 0, 0, 0)
        self.label_19 = QLabel(self.frame_21)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_32.addWidget(self.label_19, 0, Qt.AlignLeft)

        self.lineEdit_15 = QLineEdit(self.frame_21)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(200, 30))
        self.lineEdit_15.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.lineEdit_15.setReadOnly(True)

        self.horizontalLayout_32.addWidget(self.lineEdit_15, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.widget_14)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, 0, 0, 0)
        self.label_21 = QLabel(self.frame_22)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font4)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_34.addWidget(self.label_21, 0, Qt.AlignLeft)

        self.lineEdit_18 = QLineEdit(self.frame_22)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(200, 30))
        self.lineEdit_18.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.lineEdit_18.setReadOnly(True)

        self.horizontalLayout_34.addWidget(self.lineEdit_18, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_22)


        self.horizontalLayout_39.addWidget(self.widget_14)


        self.verticalLayout_10.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.page)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 80))
        self.horizontalLayout_27 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.widget_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 70))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_16)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setPointSize(12)
        self.pushButton_6.setFont(font5)
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(92, 138, 138);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 88, 132);\n"
"	\n"
"	\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icon2/icon_white/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon9)
        self.pushButton_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.pushButton_6, 0, Qt.AlignLeft)

        self.pushButton_7 = QPushButton(self.frame_16)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(80, 30))
        self.pushButton_7.setFont(font5)
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(92, 138, 138);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 88, 132);\n"
"	\n"
"	\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icon2/icon_white/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon10)
        self.pushButton_7.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.pushButton_7, 0, Qt.AlignHCenter)

        self.pushButton_14 = QPushButton(self.frame_16)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(80, 30))
        self.pushButton_14.setFont(font5)
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(92, 138, 138);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 88, 132);\n"
"	\n"
"	\n"
"}")
        self.pushButton_14.setIcon(icon10)
        self.pushButton_14.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.pushButton_14, 0, Qt.AlignRight)


        self.horizontalLayout_27.addWidget(self.frame_16, 0, Qt.AlignBottom)


        self.verticalLayout_10.addWidget(self.widget_13, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_4 = QWidget(self.page_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(56, 56, 84);")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_24 = QFrame(self.widget_8)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_14 = QLabel(self.frame_24)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_37.addWidget(self.label_14, 0, Qt.AlignLeft)

        self.lineEdit_12 = QLineEdit(self.frame_24)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(200, 30))
        self.lineEdit_12.setFont(font5)
        self.lineEdit_12.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")

        self.horizontalLayout_37.addWidget(self.lineEdit_12, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_24)

        self.frame_6 = QFrame(self.widget_8)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.label_8, 0, Qt.AlignLeft)

        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(200, 30))
        self.lineEdit_2.setFont(font5)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")

        self.horizontalLayout_14.addWidget(self.lineEdit_2, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.widget_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.label_11, 0, Qt.AlignLeft)

        self.lineEdit_3 = QLineEdit(self.frame_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(200, 30))
        self.lineEdit_3.setFont(font5)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")

        self.horizontalLayout_17.addWidget(self.lineEdit_3, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.widget_8)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.label_12, 0, Qt.AlignLeft)

        self.lineEdit_4 = QLineEdit(self.frame_8)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(200, 30))
        self.lineEdit_4.setFont(font5)
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")

        self.horizontalLayout_16.addWidget(self.lineEdit_4, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.widget_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_13, 0, Qt.AlignLeft)

        self.lineEdit_5 = QLineEdit(self.frame_9)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(200, 30))
        self.lineEdit_5.setFont(font5)
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")

        self.horizontalLayout_15.addWidget(self.lineEdit_5, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_9)


        self.horizontalLayout_13.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_8 = QVBoxLayout(self.widget_9)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.widget_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font4)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_21.addWidget(self.label_17, 0, Qt.AlignLeft)

        self.lineEdit_6 = QLineEdit(self.frame_12)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(200, 30))
        self.lineEdit_6.setFont(font5)
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")

        self.horizontalLayout_21.addWidget(self.lineEdit_6, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.widget_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_16 = QLabel(self.frame_13)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.label_16, 0, Qt.AlignLeft)

        self.lineEdit_9 = QLineEdit(self.frame_13)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(200, 30))
        self.lineEdit_9.setFont(font5)
        self.lineEdit_9.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")

        self.horizontalLayout_20.addWidget(self.lineEdit_9, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_13)

        self.frame_11 = QFrame(self.widget_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_11 = QPushButton(self.frame_11)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font4)
        self.pushButton_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_19.addWidget(self.pushButton_11, 0, Qt.AlignLeft)

        self.lineEdit_8 = QLineEdit(self.frame_11)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(200, 30))
        self.lineEdit_8.setFont(font5)
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.lineEdit_8.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.lineEdit_8, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.widget_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_10 = QPushButton(self.frame_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font4)
        self.pushButton_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.pushButton_10, 0, Qt.AlignLeft)

        self.lineEdit_7 = QLineEdit(self.frame_10)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(200, 30))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.lineEdit_7.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.lineEdit_7, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_10)


        self.horizontalLayout_13.addWidget(self.widget_9)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.widget_6 = QWidget(self.page_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.widget_7)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 20))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_23)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(175, 0))
        self.pushButton_9.setMaximumSize(QSize(175, 100))
        font6 = QFont()
        font6.setPointSize(18)
        font6.setBold(True)
        font6.setWeight(75)
        self.pushButton_9.setFont(font6)
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(92, 138, 138);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 88, 132);\n"
"	\n"
"	\n"
"}")
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QSize(25, 25))

        self.horizontalLayout_35.addWidget(self.pushButton_9, 0, Qt.AlignHCenter)


        self.horizontalLayout_12.addWidget(self.frame_23)


        self.horizontalLayout_36.addWidget(self.widget_7)


        self.verticalLayout_6.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_11 = QWidget(self.page_3)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 65))
        self.widget_11.setMaximumSize(QSize(16777215, 65))
        self.widget_11.setStyleSheet(u"")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.widget_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_24.setSpacing(20)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_10 = QLineEdit(self.frame_14)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(150, 40))
        self.lineEdit_10.setFont(font5)
        self.lineEdit_10.setStyleSheet(u"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_24.addWidget(self.lineEdit_10)

        self.pushButton_12 = QPushButton(self.frame_14)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 32))
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 88, 132);\n"
"	\n"
"	\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icon2/icon_white/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon11)
        self.pushButton_12.setIconSize(QSize(30, 30))

        self.horizontalLayout_24.addWidget(self.pushButton_12)


        self.horizontalLayout_23.addWidget(self.frame_14, 0, Qt.AlignLeft)

        self.frame_15 = QFrame(self.widget_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.frame_15)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(70, 35))
        self.pushButton_13.setFont(font4)
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.pushButton_13.setIconSize(QSize(25, 25))

        self.horizontalLayout_25.addWidget(self.pushButton_13, 0, Qt.AlignRight)


        self.horizontalLayout_23.addWidget(self.frame_15)


        self.verticalLayout_9.addWidget(self.widget_11)

        self.widget_10 = QWidget(self.page_3)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.widget_10)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 816, 343))
        self.horizontalLayout_26 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents_2)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_26.addWidget(self.tableWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_22.addWidget(self.scrollArea)


        self.verticalLayout_9.addWidget(self.widget_10)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(270, 140, 191, 51))
        font7 = QFont()
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_10.setFont(font7)
        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.main)


        self.horizontalLayout_11.addWidget(self.body)

        self.profile = QCustomSlideMenu(self.widget_2)
        self.profile.setObjectName(u"profile")
        self.profile.setMinimumSize(QSize(0, 200))
        self.profile.setMaximumSize(QSize(0, 230))
        self.horizontalLayout_8 = QHBoxLayout(self.profile)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.profile)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(100, 230))
        self.frame_4.setMaximumSize(QSize(0, 230))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 81, 21))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color: rgb(186, 186, 186);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 70, 47, 51))
        self.label_4.setPixmap(QPixmap(u":/images/picture/pexels-lukas-rychvalsky-670720.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 40, 71, 20))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 140, 75, 23))
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(True)
        font8.setWeight(75)
        self.pushButton_5.setFont(font8)
        self.pushButton_5.setStyleSheet(u"background-color: rgb(161, 161, 161);\n"
"border-radius: 20px;")
        icon12 = QIcon()
        icon12.addFile(u":/icon1/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon12)
        self.pushButton_5.setIconSize(QSize(25, 25))
        self.pushButton_8 = QPushButton(self.frame_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 190, 61, 31))
        self.pushButton_8.setFont(font5)
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(92, 138, 138);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icon2/icon_white/moon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon13)
        self.pushButton_8.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.horizontalLayout_11.addWidget(self.profile, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fedral Police DataBase System App", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.adimnster_btn.setText(QCoreApplication.translate("MainWindow", u"Registration", None))
        self.Help.setText(QCoreApplication.translate("MainWindow", u"Crime Records", None))
        self.language_btn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_btn.setText("")
        self.label_23.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Fedral Police Database System", None))
        self.account_btn.setText("")
        self.label_7.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Phone no", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Cases", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Adress", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Browse Images", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Check_by photo", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Check_by Finger_print", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Phone_No", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Cases", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Adress", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Finger_Print", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Photo", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search by name", None))
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Phone_no", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"cases", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Adress", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Photo", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fedral Police", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.pushButton_8.setText("")
    # retranslateUi

