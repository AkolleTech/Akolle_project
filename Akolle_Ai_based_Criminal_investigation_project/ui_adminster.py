# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminsterOMHdnp.ui'
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

class Ui_adminster(object):
    def setupUi(self, adminster):
        if not adminster.objectName():
            adminster.setObjectName(u"adminster")
        adminster.resize(824, 555)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        adminster.setFont(font)
        adminster.setStyleSheet(u"*{\n"
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
"border: 2px solid #000;\n"
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
"#record_btn{\n"
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
        self.centralwidget = QWidget(adminster)
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
        self.pushButton_3.setIconSize(QSize(20, 20))

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


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet(u"")
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
        self.Create_Account = QPushButton(self.frame_5)
        self.Create_Account.setObjectName(u"Create_Account")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Create_Account.sizePolicy().hasHeightForWidth())
        self.Create_Account.setSizePolicy(sizePolicy2)
        self.Create_Account.setMinimumSize(QSize(170, 25))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.Create_Account.setFont(font3)
        self.Create_Account.setStyleSheet(u"QPushButton{\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(223, 223, 223);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon2/icon_white/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Create_Account.setIcon(icon4)
        self.Create_Account.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Create_Account, 0, Qt.AlignLeft)

        self.Police_Records = QPushButton(self.frame_5)
        self.Police_Records.setObjectName(u"Police_Records")
        self.Police_Records.setMinimumSize(QSize(170, 25))
        self.Police_Records.setFont(font3)
        self.Police_Records.setStyleSheet(u"QPushButton{\n"
"\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(223, 223, 223);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon2/icon_white/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Police_Records.setIcon(icon5)
        self.Police_Records.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Police_Records, 0, Qt.AlignLeft)

        self.Criminal_Records = QPushButton(self.frame_5)
        self.Criminal_Records.setObjectName(u"Criminal_Records")
        self.Criminal_Records.setMinimumSize(QSize(170, 25))
        self.Criminal_Records.setFont(font3)
        self.Criminal_Records.setStyleSheet(u"QPushButton{\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(223, 223, 223);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icon2/icon_white/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Criminal_Records.setIcon(icon6)
        self.Criminal_Records.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Criminal_Records, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_5)


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
        self.header.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.header)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.widget_3)
        self.menu_btn.setObjectName(u"menu_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icon2/icon_white/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon7)
        self.menu_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.menu_btn, 0, Qt.AlignLeft)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 70))
        self.label_2.setMaximumSize(QSize(70, 70))
        self.label_2.setPixmap(QPixmap(u":/polic/PicsArt_02-27-12.33.46.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_2, 0, Qt.AlignTop)

        self.appname = QLabel(self.widget_3)
        self.appname.setObjectName(u"appname")
        self.appname.setMaximumSize(QSize(16777215, 60))
        self.appname.setFont(font2)
        self.appname.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.appname)


        self.horizontalLayout_4.addWidget(self.widget_3, 0, Qt.AlignLeft)

        self.widget_5 = QWidget(self.header)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 10, 0)
        self.account_btn = QPushButton(self.widget_5)
        self.account_btn.setObjectName(u"account_btn")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.account_btn.setFont(font4)
        self.account_btn.setStyleSheet(u"QPushButton{\n"
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
        icon8 = QIcon()
        icon8.addFile(u":/icon2/icon_white/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.account_btn.setIcon(icon8)
        self.account_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.account_btn)


        self.horizontalLayout_4.addWidget(self.widget_5, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.header, 0, Qt.AlignTop)

        self.main = QWidget(self.body)
        self.main.setObjectName(u"main")
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.main)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QCustomStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_10 = QVBoxLayout(self.page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_12 = QWidget(self.page)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget_12)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_12)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(400, 300))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7.setPixmap(QPixmap(u":/polic/th.jpg"))
        self.label_7.setScaledContents(True)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy4)
        self.widget_14.setStyleSheet(u"background-color: rgb(56, 56, 84);")
        self.verticalLayout_7 = QVBoxLayout(self.widget_14)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_23 = QFrame(self.widget_14)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(-1, 0, 0, 0)
        self.label_22 = QLabel(self.frame_23)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_35.addWidget(self.label_22, 0, Qt.AlignLeft)

        self.lineEdit_19 = QLineEdit(self.frame_23)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(200, 30))
        font5 = QFont()
        font5.setPointSize(10)
        self.lineEdit_19.setFont(font5)
        self.lineEdit_19.setTabletTracking(True)
        self.lineEdit_19.setFocusPolicy(Qt.WheelFocus)
        self.lineEdit_19.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}\n"
"")
        self.lineEdit_19.setReadOnly(False)

        self.horizontalLayout_35.addWidget(self.lineEdit_19, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_23)

        self.frame_17 = QFrame(self.widget_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFocusPolicy(Qt.NoFocus)
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

        self.horizontalLayout_29.addWidget(self.label_9, 0, Qt.AlignLeft)

        self.lineEdit_11 = QLineEdit(self.frame_17)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(200, 30))
        self.lineEdit_11.setFont(font5)
        self.lineEdit_11.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_11.setReadOnly(False)

        self.horizontalLayout_29.addWidget(self.lineEdit_11, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.widget_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 0, 0, 0)
        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.label_11, 0, Qt.AlignLeft)

        self.lineEdit_16 = QLineEdit(self.frame_19)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(200, 30))
        self.lineEdit_16.setFont(font5)
        self.lineEdit_16.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_16.setReadOnly(False)

        self.horizontalLayout_30.addWidget(self.lineEdit_16, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_19)

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
        self.lineEdit_17.setFont(font5)
        self.lineEdit_17.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_17.setReadOnly(False)

        self.horizontalLayout_33.addWidget(self.lineEdit_17, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_18)

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
        self.lineEdit_14.setFont(font5)
        self.lineEdit_14.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_14.setReadOnly(False)

        self.horizontalLayout_31.addWidget(self.lineEdit_14, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_20)

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
        self.lineEdit_15.setFont(font5)
        self.lineEdit_15.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_15.setReadOnly(False)

        self.horizontalLayout_32.addWidget(self.lineEdit_15, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_21)

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
        self.lineEdit_18.setFont(font5)
        self.lineEdit_18.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_18.setReadOnly(False)

        self.horizontalLayout_34.addWidget(self.lineEdit_18, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_22)


        self.gridLayout.addWidget(self.widget_14, 0, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.page)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 80))
        self.widget_13.setStyleSheet(u"QWidget#widget_13{\n"
"background-color: qlineargradient(spread:pad, x1:0.159, y1:0.170455, x2:1, y2:1, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
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
        self.pushButton_7 = QPushButton(self.frame_16)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(150, 40))
        self.pushButton_7.setMaximumSize(QSize(200, 50))
        font6 = QFont()
        font6.setPointSize(12)
        self.pushButton_7.setFont(font6)
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
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(20, 20))

        self.horizontalLayout_28.addWidget(self.pushButton_7, 0, Qt.AlignHCenter)


        self.horizontalLayout_27.addWidget(self.frame_16, 0, Qt.AlignBottom)


        self.verticalLayout_10.addWidget(self.widget_13, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_11 = QWidget(self.page_3)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 65))
        self.widget_11.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_14 = QFrame(self.widget_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_10 = QLineEdit(self.frame_14)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(150, 40))
        self.lineEdit_10.setFont(font6)
        self.lineEdit_10.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #2596be;\n"
"")

        self.horizontalLayout_24.addWidget(self.lineEdit_10)

        self.pushButton_12 = QPushButton(self.frame_14)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 32))
        icon9 = QIcon()
        icon9.addFile(u":/icon2/icon_white/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon9)
        self.pushButton_12.setIconSize(QSize(30, 30))

        self.horizontalLayout_24.addWidget(self.pushButton_12)


        self.horizontalLayout_13.addWidget(self.frame_14, 0, Qt.AlignLeft)

        self.pushButton_30 = QPushButton(self.widget_11)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(70, 35))
        self.pushButton_30.setFont(font4)
        self.pushButton_30.setStyleSheet(u"QPushButton{\n"
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
        icon10.addFile(u":/icon2/icon_white/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_30.setIcon(icon10)
        self.pushButton_30.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.pushButton_30, 0, Qt.AlignHCenter)

        self.pushButton_31 = QPushButton(self.widget_11)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(70, 35))
        self.pushButton_31.setFont(font4)
        self.pushButton_31.setStyleSheet(u"QPushButton{\n"
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
        icon11 = QIcon()
        icon11.addFile(u":/icon2/icon_white/edit-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_31.setIcon(icon11)
        self.pushButton_31.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.pushButton_31, 0, Qt.AlignHCenter)

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
"	background-color: rgb(92, 138, 138);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 88, 132);\n"
"	\n"
"	\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icon2/icon_white/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon12)
        self.pushButton_13.setIconSize(QSize(25, 25))

        self.horizontalLayout_25.addWidget(self.pushButton_13, 0, Qt.AlignRight)


        self.horizontalLayout_13.addWidget(self.frame_15)


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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 806, 361))
        self.horizontalLayout_14 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents_2)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.tableWidget)

        self.widget_16 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 300))
        self.widget_16.setMaximumSize(QSize(0, 350))
        self.widget_16.setStyleSheet(u"background-color: rgb(0, 55, 80);")
        self.lineEdit_27 = QLineEdit(self.widget_16)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setGeometry(QRect(10, 90, 150, 40))
        self.lineEdit_27.setMinimumSize(QSize(150, 40))
        self.lineEdit_27.setMaximumSize(QSize(150, 40))
        self.lineEdit_27.setFont(font5)
        self.lineEdit_27.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_28 = QLineEdit(self.widget_16)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setGeometry(QRect(10, 160, 150, 40))
        self.lineEdit_28.setMinimumSize(QSize(150, 40))
        self.lineEdit_28.setMaximumSize(QSize(150, 40))
        self.lineEdit_28.setFont(font5)
        self.lineEdit_28.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_29 = QLineEdit(self.widget_16)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setGeometry(QRect(10, 230, 150, 40))
        self.lineEdit_29.setMinimumSize(QSize(150, 40))
        self.lineEdit_29.setMaximumSize(QSize(150, 40))
        self.lineEdit_29.setFont(font5)
        self.lineEdit_29.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_30 = QLineEdit(self.widget_16)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setGeometry(QRect(230, 160, 150, 40))
        self.lineEdit_30.setMinimumSize(QSize(150, 40))
        self.lineEdit_30.setMaximumSize(QSize(150, 40))
        self.lineEdit_30.setFont(font5)
        self.lineEdit_30.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_31 = QLineEdit(self.widget_16)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setGeometry(QRect(230, 90, 150, 40))
        self.lineEdit_31.setMinimumSize(QSize(150, 40))
        self.lineEdit_31.setMaximumSize(QSize(150, 40))
        self.lineEdit_31.setFont(font5)
        self.lineEdit_31.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_33 = QLineEdit(self.widget_16)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setGeometry(QRect(230, 20, 150, 40))
        self.lineEdit_33.setMinimumSize(QSize(150, 0))
        self.lineEdit_33.setMaximumSize(QSize(150, 40))
        self.lineEdit_33.setFont(font5)
        self.lineEdit_33.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_19 = QPushButton(self.widget_16)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(280, 250, 75, 23))
        self.pushButton_19.setFont(font4)
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
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
        self.lineEdit_35 = QLineEdit(self.widget_16)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setGeometry(QRect(10, 20, 150, 40))
        self.lineEdit_35.setMinimumSize(QSize(150, 40))
        self.lineEdit_35.setMaximumSize(QSize(150, 40))
        self.lineEdit_35.setFont(font5)
        self.lineEdit_35.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.widget_16, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_22.addWidget(self.scrollArea)


        self.verticalLayout_9.addWidget(self.widget_10)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_6 = QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_25 = QWidget(self.page_4)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(0, 65))
        self.widget_25.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_42 = QFrame(self.widget_25)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_32 = QLineEdit(self.frame_42)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setMinimumSize(QSize(150, 40))
        self.lineEdit_32.setFont(font6)
        self.lineEdit_32.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #2596be;\n"
"")

        self.horizontalLayout_63.addWidget(self.lineEdit_32)

        self.pushButton_22 = QPushButton(self.frame_42)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 32))
        self.pushButton_22.setIcon(icon9)
        self.pushButton_22.setIconSize(QSize(30, 30))

        self.horizontalLayout_63.addWidget(self.pushButton_22)


        self.horizontalLayout_8.addWidget(self.frame_42, 0, Qt.AlignLeft)

        self.pushButton_24 = QPushButton(self.widget_25)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(70, 35))
        self.pushButton_24.setFont(font4)
        self.pushButton_24.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_24.setIcon(icon10)
        self.pushButton_24.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.pushButton_24, 0, Qt.AlignHCenter)

        self.pushButton_25 = QPushButton(self.widget_25)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(70, 35))
        self.pushButton_25.setFont(font4)
        self.pushButton_25.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_25.setIcon(icon11)
        self.pushButton_25.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.pushButton_25, 0, Qt.AlignHCenter)

        self.frame_43 = QFrame(self.widget_25)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.pushButton_23 = QPushButton(self.frame_43)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(70, 35))
        self.pushButton_23.setFont(font4)
        self.pushButton_23.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_23.setIcon(icon12)
        self.pushButton_23.setIconSize(QSize(25, 25))

        self.horizontalLayout_64.addWidget(self.pushButton_23, 0, Qt.AlignRight)


        self.horizontalLayout_8.addWidget(self.frame_43)


        self.verticalLayout_6.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.page_4)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_65 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.widget_26)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 806, 361))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_3 = QTableWidget(self.scrollAreaWidgetContents_4)
        if (self.tableWidget_3.columnCount() < 8):
            self.tableWidget_3.setColumnCount(8)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.tableWidget_3)

        self.widget_15 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 350))
        self.widget_15.setMaximumSize(QSize(0, 350))
        self.widget_15.setStyleSheet(u"background-color: rgb(0, 55, 80);")
        self.lineEdit_23 = QLineEdit(self.widget_15)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setGeometry(QRect(10, 90, 150, 40))
        self.lineEdit_23.setMinimumSize(QSize(150, 40))
        self.lineEdit_23.setMaximumSize(QSize(150, 40))
        self.lineEdit_23.setFont(font5)
        self.lineEdit_23.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_13 = QLineEdit(self.widget_15)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(10, 160, 150, 40))
        self.lineEdit_13.setMinimumSize(QSize(150, 40))
        self.lineEdit_13.setMaximumSize(QSize(150, 40))
        self.lineEdit_13.setFont(font5)
        self.lineEdit_13.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_20 = QLineEdit(self.widget_15)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(10, 230, 150, 40))
        self.lineEdit_20.setMinimumSize(QSize(150, 40))
        self.lineEdit_20.setMaximumSize(QSize(150, 40))
        self.lineEdit_20.setFont(font5)
        self.lineEdit_20.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_21 = QLineEdit(self.widget_15)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(230, 160, 150, 40))
        self.lineEdit_21.setMinimumSize(QSize(150, 40))
        self.lineEdit_21.setMaximumSize(QSize(150, 40))
        self.lineEdit_21.setFont(font5)
        self.lineEdit_21.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_22 = QLineEdit(self.widget_15)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(QRect(230, 90, 150, 40))
        self.lineEdit_22.setMinimumSize(QSize(150, 40))
        self.lineEdit_22.setMaximumSize(QSize(150, 40))
        self.lineEdit_22.setFont(font5)
        self.lineEdit_22.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_24 = QLineEdit(self.widget_15)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setGeometry(QRect(230, 20, 150, 40))
        self.lineEdit_24.setMinimumSize(QSize(150, 0))
        self.lineEdit_24.setMaximumSize(QSize(150, 40))
        self.lineEdit_24.setFont(font5)
        self.lineEdit_24.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_17 = QPushButton(self.widget_15)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(260, 310, 75, 23))
        self.pushButton_17.setFont(font4)
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_18 = QPushButton(self.widget_15)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(10, 300, 150, 40))
        self.pushButton_18.setFont(font4)
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255);\n"
"	\n"
"	\n"
"}")
        self.lineEdit_25 = QLineEdit(self.widget_15)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setGeometry(QRect(230, 230, 150, 40))
        self.lineEdit_25.setMinimumSize(QSize(150, 40))
        self.lineEdit_25.setMaximumSize(QSize(150, 40))
        self.lineEdit_25.setFont(font5)
        self.lineEdit_25.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_26 = QLineEdit(self.widget_15)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setGeometry(QRect(10, 20, 150, 40))
        self.lineEdit_26.setMinimumSize(QSize(150, 40))
        self.lineEdit_26.setMaximumSize(QSize(150, 40))
        self.lineEdit_26.setFont(font5)
        self.lineEdit_26.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.widget_15, 0, Qt.AlignTop)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_65.addWidget(self.scrollArea_3)


        self.verticalLayout_6.addWidget(self.widget_26)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.main)


        self.horizontalLayout_11.addWidget(self.body)


        self.verticalLayout.addWidget(self.widget_2)

        adminster.setCentralWidget(self.centralwidget)

        self.retranslateUi(adminster)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(adminster)
    # setupUi

    def retranslateUi(self, adminster):
        adminster.setWindowTitle(QCoreApplication.translate("adminster", u"MainWindow", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("adminster", u"Fedral Police DataBase System App", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.label_6.setText(QCoreApplication.translate("adminster", u"Fedral Police", None))
        self.Create_Account.setText(QCoreApplication.translate("adminster", u"Creat Account", None))
        self.Police_Records.setText(QCoreApplication.translate("adminster", u"Police Records", None))
        self.Criminal_Records.setText(QCoreApplication.translate("adminster", u"Crimnal Records", None))
        self.menu_btn.setText("")
        self.label_2.setText("")
        self.appname.setText(QCoreApplication.translate("adminster", u"Fedral Police Database System App", None))
        self.account_btn.setText(QCoreApplication.translate("adminster", u"Log out", None))
        self.label_7.setText("")
        self.label_22.setText(QCoreApplication.translate("adminster", u"ID", None))
        self.label_9.setText(QCoreApplication.translate("adminster", u"Name", None))
        self.label_11.setText(QCoreApplication.translate("adminster", u"Password", None))
        self.label_20.setText(QCoreApplication.translate("adminster", u"Phone no", None))
        self.label_18.setText(QCoreApplication.translate("adminster", u"Adress", None))
        self.label_19.setText(QCoreApplication.translate("adminster", u"Age", None))
        self.label_21.setText(QCoreApplication.translate("adminster", u"Gender", None))
        self.pushButton_7.setText(QCoreApplication.translate("adminster", u"Register", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("adminster", u"search by name", None))
        self.pushButton_12.setText("")
        self.pushButton_30.setText(QCoreApplication.translate("adminster", u"Delete", None))
        self.pushButton_31.setText(QCoreApplication.translate("adminster", u"Update", None))
        self.pushButton_13.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("adminster", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("adminster", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("adminster", u"Password", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("adminster", u"Phone_no", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("adminster", u"Adress", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("adminster", u"Age", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("adminster", u"Gender", None));
        self.pushButton_19.setText(QCoreApplication.translate("adminster", u"Done", None))
        self.lineEdit_32.setPlaceholderText(QCoreApplication.translate("adminster", u"search by name", None))
        self.pushButton_22.setText("")
        self.pushButton_24.setText(QCoreApplication.translate("adminster", u"Delete", None))
        self.pushButton_25.setText(QCoreApplication.translate("adminster", u"Update", None))
        self.pushButton_23.setText("")
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("adminster", u"Id", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("adminster", u"Name", None));
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("adminster", u"Phone_no", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("adminster", u"cases", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("adminster", u"Adress", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("adminster", u"Age", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("adminster", u"Gender", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("adminster", u"Photo", None));
        self.pushButton_17.setText(QCoreApplication.translate("adminster", u"Done", None))
        self.pushButton_18.setText(QCoreApplication.translate("adminster", u"Take Photo", None))
    # retranslateUi

