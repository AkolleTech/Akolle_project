# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homessaJOuhW.ui'
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

class Ui_new_2(object):
    def setupUi(self, new_2):
        if not new_2.objectName():
            new_2.setObjectName(u"new_2")
        new_2.resize(830, 602)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        new_2.setFont(font)
        new_2.setStyleSheet(u"*{\n"
"color: #000;\n"
"border: none;\n"
"}\n"
"#frame_1{background-color:#2596be;\n"
"	\n"
"}\n"
"#centralwidget\n"
"{\n"
"\n"
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
        self.centralwidget = QWidget(new_2)
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
        self.horizontalLayout.setContentsMargins(0, 2, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 10)
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
        icon = QIcon()
        icon.addFile(u":/icon2/icon_white/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u":/icon2/icon_white/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u":/icon2/icon_white/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
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

        self.frame_4 = QFrame(self.frame_1)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setSpacing(40)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 20, -1, 20)
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(170, 25))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(223, 223, 223);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon2/icon_white/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.pushButton_5, 0, Qt.AlignLeft)

        self.pushButton_10 = QPushButton(self.frame_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(170, 25))
        self.pushButton_10.setFont(font3)
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(223, 223, 223);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon2/icon_white/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.pushButton_10, 0, Qt.AlignLeft)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(170, 25))
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"padding: 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(223, 223, 223);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon2/icon_white/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.pushButton_6, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame_1)


        self.horizontalLayout_11.addWidget(self.left, 0, Qt.AlignLeft)

        self.body = QWidget(self.widget_2)
        self.body.setObjectName(u"body")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy2)
        self.body.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.body)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.body)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 70))
        self.header.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.header)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.widget_3)
        self.menu_btn.setObjectName(u"menu_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icon2/icon_white/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon6)
        self.menu_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.menu_btn)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 70))
        self.label_2.setMaximumSize(QSize(70, 70))
        self.label_2.setPixmap(QPixmap(u":/polic/PicsArt_02-27-12.33.46.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.appname = QLabel(self.widget_3)
        self.appname.setObjectName(u"appname")
        self.appname.setMaximumSize(QSize(16777215, 60))
        self.appname.setFont(font2)
        self.appname.setStyleSheet(u"color: rgb(255, 255, 255);")

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
        self.account_btn.setFont(font3)
        self.account_btn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 88, 132);\n"
"	\n"
"	\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icon2/icon_white/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.account_btn.setIcon(icon7)
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
        self.widget_8 = QWidget(self.page)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.widget_8)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font3)
        self.tabss = QWidget()
        self.tabss.setObjectName(u"tabss")
        self.verticalLayout_7 = QVBoxLayout(self.tabss)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_17 = QWidget(self.tabss)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy)
        self.horizontalLayout_27 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.widget_32 = QWidget(self.widget_17)
        self.widget_32.setObjectName(u"widget_32")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_32.sizePolicy().hasHeightForWidth())
        self.widget_32.setSizePolicy(sizePolicy3)
        self.widget_32.setMaximumSize(QSize(16777215, 16777215))
        self.widget_32.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.widget_32)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_32)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(356, 341))
        self.label_4.setMaximumSize(QSize(600, 400))
        self.label_4.setStyleSheet(u"")
        self.label_4.setScaledContents(True)

        self.verticalLayout_21.addWidget(self.label_4)


        self.horizontalLayout_27.addWidget(self.widget_32)

        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_4)

        self.widget_33 = QWidget(self.widget_17)
        self.widget_33.setObjectName(u"widget_33")
        sizePolicy3.setHeightForWidth(self.widget_33.sizePolicy().hasHeightForWidth())
        self.widget_33.setSizePolicy(sizePolicy3)
        self.widget_33.setMinimumSize(QSize(0, 350))
        self.widget_33.setMaximumSize(QSize(16777215, 16777215))
        self.widget_33.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.widget_33)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_51 = QFrame(self.widget_33)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(-1, 0, 9, 0)
        self.label_30 = QLabel(self.frame_51)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_44.addWidget(self.label_30, 0, Qt.AlignLeft)

        self.lineEdit_36 = QLineEdit(self.frame_51)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setMinimumSize(QSize(200, 30))
        font4 = QFont()
        font4.setPointSize(10)
        self.lineEdit_36.setFont(font4)
        self.lineEdit_36.setTabletTracking(True)
        self.lineEdit_36.setFocusPolicy(Qt.WheelFocus)
        self.lineEdit_36.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}\n"
"")
        self.lineEdit_36.setReadOnly(False)

        self.horizontalLayout_44.addWidget(self.lineEdit_36, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.widget_33)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFocusPolicy(Qt.NoFocus)
        self.frame_52.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(-1, 0, 9, 0)
        self.label_18 = QLabel(self.frame_52)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_58.addWidget(self.label_18, 0, Qt.AlignLeft)

        self.lineEdit_34 = QLineEdit(self.frame_52)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setMinimumSize(QSize(200, 30))
        self.lineEdit_34.setFont(font4)
        self.lineEdit_34.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_34.setReadOnly(False)

        self.horizontalLayout_58.addWidget(self.lineEdit_34, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.widget_33)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_22 = QLabel(self.frame_53)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.label_22, 0, Qt.AlignLeft)

        self.lineEdit_56 = QLineEdit(self.frame_53)
        self.lineEdit_56.setObjectName(u"lineEdit_56")
        self.lineEdit_56.setMinimumSize(QSize(200, 30))
        self.lineEdit_56.setFont(font4)
        self.lineEdit_56.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_56.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.lineEdit_56, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.widget_33)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(9, 0, 9, 0)
        self.label_23 = QLabel(self.frame_54)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_59.addWidget(self.label_23, 0, Qt.AlignLeft)

        self.lineEdit_38 = QLineEdit(self.frame_54)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setMinimumSize(QSize(200, 30))
        self.lineEdit_38.setFont(font4)
        self.lineEdit_38.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_38.setReadOnly(False)

        self.horizontalLayout_59.addWidget(self.lineEdit_38, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_54)

        self.frame_57 = QFrame(self.widget_33)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(9, 0, 9, 0)
        self.label_24 = QLabel(self.frame_57)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_60.addWidget(self.label_24, 0, Qt.AlignLeft)

        self.lineEdit_40 = QLineEdit(self.frame_57)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setMinimumSize(QSize(200, 30))
        self.lineEdit_40.setFont(font4)
        self.lineEdit_40.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_40.setReadOnly(False)

        self.horizontalLayout_60.addWidget(self.lineEdit_40, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_57)

        self.frame_55 = QFrame(self.widget_33)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_31 = QLabel(self.frame_55)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.label_31, 0, Qt.AlignLeft)

        self.lineEdit_57 = QLineEdit(self.frame_55)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setMinimumSize(QSize(200, 30))
        self.lineEdit_57.setFont(font4)
        self.lineEdit_57.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_57.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.lineEdit_57, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.widget_33)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_32 = QLabel(self.frame_56)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_21.addWidget(self.label_32, 0, Qt.AlignLeft)

        self.lineEdit_58 = QLineEdit(self.frame_56)
        self.lineEdit_58.setObjectName(u"lineEdit_58")
        self.lineEdit_58.setMinimumSize(QSize(200, 30))
        self.lineEdit_58.setFont(font4)
        self.lineEdit_58.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_58.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.lineEdit_58, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_56)


        self.horizontalLayout_27.addWidget(self.widget_33)


        self.verticalLayout_7.addWidget(self.widget_17)

        self.lineEdit = QLineEdit(self.tabss)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 8))

        self.verticalLayout_7.addWidget(self.lineEdit, 0, Qt.AlignLeft)

        self.widget_13 = QWidget(self.tabss)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 50))
        self.widget_13.setStyleSheet(u"")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.widget_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 55))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_7 = QPushButton(self.frame_16)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(150, 40))
        self.pushButton_7.setMaximumSize(QSize(200, 50))
        font5 = QFont()
        font5.setPointSize(12)
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
        icon8 = QIcon()
        icon8.addFile(u":/icon2/icon_white/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(20, 20))

        self.horizontalLayout_19.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.frame_16)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(150, 40))
        self.pushButton_9.setMaximumSize(QSize(200, 50))
        self.pushButton_9.setFont(font5)
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
        icon9 = QIcon()
        icon9.addFile(u":/icon2/icon_white/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon9)
        self.pushButton_9.setIconSize(QSize(20, 20))

        self.horizontalLayout_19.addWidget(self.pushButton_9)


        self.horizontalLayout_18.addWidget(self.frame_16)


        self.verticalLayout_7.addWidget(self.widget_13)

        self.tabWidget.addTab(self.tabss, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_15 = QVBoxLayout(self.tab_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_16 = QWidget(self.tab_2)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy)
        self.horizontalLayout_22 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy3.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy3)
        self.widget_18.setMaximumSize(QSize(16777215, 16777215))
        self.widget_18.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.widget_18)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_18)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(356, 241))
        self.label_3.setMaximumSize(QSize(600, 400))
        self.label_3.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_3)


        self.horizontalLayout_22.addWidget(self.widget_18)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_2)

        self.widget_19 = QWidget(self.widget_16)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy3.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy3)
        self.widget_19.setMaximumSize(QSize(16777215, 16777215))
        self.widget_19.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.widget_19)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.widget_19)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(-1, 0, 9, 0)
        self.label_25 = QLabel(self.frame_29)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_40.addWidget(self.label_25, 0, Qt.AlignLeft)

        self.lineEdit_35 = QLineEdit(self.frame_29)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setMinimumSize(QSize(200, 30))
        self.lineEdit_35.setFont(font4)
        self.lineEdit_35.setTabletTracking(True)
        self.lineEdit_35.setFocusPolicy(Qt.WheelFocus)
        self.lineEdit_35.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}\n"
"")
        self.lineEdit_35.setReadOnly(False)

        self.horizontalLayout_40.addWidget(self.lineEdit_35, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.widget_19)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFocusPolicy(Qt.NoFocus)
        self.frame_30.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(-1, 0, 9, 0)
        self.label_15 = QLabel(self.frame_30)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_41.addWidget(self.label_15, 0, Qt.AlignLeft)

        self.lineEdit_30 = QLineEdit(self.frame_30)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setMinimumSize(QSize(200, 30))
        self.lineEdit_30.setFont(font4)
        self.lineEdit_30.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_30.setReadOnly(False)

        self.horizontalLayout_41.addWidget(self.lineEdit_30, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_30)

        self.frame_50 = QFrame(self.widget_19)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_19 = QLabel(self.frame_50)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.label_19, 0, Qt.AlignLeft)

        self.lineEdit_55 = QLineEdit(self.frame_50)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        self.lineEdit_55.setMinimumSize(QSize(200, 30))
        self.lineEdit_55.setFont(font4)
        self.lineEdit_55.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_55.setReadOnly(False)

        self.horizontalLayout_16.addWidget(self.lineEdit_55, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_50)

        self.frame_31 = QFrame(self.widget_19)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(9, 0, 9, 0)
        self.label_16 = QLabel(self.frame_31)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_42.addWidget(self.label_16, 0, Qt.AlignLeft)

        self.lineEdit_37 = QLineEdit(self.frame_31)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setMinimumSize(QSize(200, 30))
        self.lineEdit_37.setFont(font4)
        self.lineEdit_37.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_37.setReadOnly(False)

        self.horizontalLayout_42.addWidget(self.lineEdit_37, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.widget_19)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_33 = QLabel(self.frame_32)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_23.addWidget(self.label_33, 0, Qt.AlignLeft)

        self.lineEdit_39 = QLineEdit(self.frame_32)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setMinimumSize(QSize(200, 30))
        self.lineEdit_39.setFont(font4)
        self.lineEdit_39.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_39.setReadOnly(False)

        self.horizontalLayout_23.addWidget(self.lineEdit_39, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_32)

        self.frame_49 = QFrame(self.widget_19)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_34 = QLabel(self.frame_49)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.label_34, 0, Qt.AlignLeft)

        self.lineEdit_54 = QLineEdit(self.frame_49)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setMinimumSize(QSize(200, 30))
        self.lineEdit_54.setFont(font4)
        self.lineEdit_54.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_54.setReadOnly(False)

        self.horizontalLayout_25.addWidget(self.lineEdit_54, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_49)


        self.horizontalLayout_22.addWidget(self.widget_19)


        self.verticalLayout_15.addWidget(self.widget_16)

        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 10))

        self.verticalLayout_15.addWidget(self.lineEdit_2, 0, Qt.AlignLeft)

        self.widget_20 = QWidget(self.tab_2)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(0, 80))
        self.widget_20.setStyleSheet(u"")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.widget_20)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 55))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_16 = QPushButton(self.frame_33)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(150, 40))
        self.pushButton_16.setMaximumSize(QSize(200, 50))
        self.pushButton_16.setFont(font5)
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_16.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.pushButton_16)

        self.pushButton_14 = QPushButton(self.frame_33)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(150, 40))
        self.pushButton_14.setMaximumSize(QSize(200, 50))
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
        self.pushButton_14.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.pushButton_14)


        self.horizontalLayout_43.addWidget(self.frame_33)


        self.verticalLayout_15.addWidget(self.widget_20)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout_7.addWidget(self.tabWidget)


        self.verticalLayout_10.addWidget(self.widget_8)

        self.stackedWidget.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_6 = QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_9 = QWidget(self.page_4)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tabWidget_2 = QTabWidget(self.widget_9)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setFont(font3)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_16 = QVBoxLayout(self.tab)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_25 = QWidget(self.tab)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(0, 65))
        self.widget_25.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
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
        self.lineEdit_32.setFont(font5)
        self.lineEdit_32.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #2596be;\n"
"")

        self.horizontalLayout_63.addWidget(self.lineEdit_32, 0, Qt.AlignLeft)

        self.pushButton_22 = QPushButton(self.frame_42)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 32))
        icon10 = QIcon()
        icon10.addFile(u":/icon2/icon_white/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_22.setIcon(icon10)
        self.pushButton_22.setIconSize(QSize(30, 30))

        self.horizontalLayout_63.addWidget(self.pushButton_22, 0, Qt.AlignLeft)


        self.horizontalLayout_12.addWidget(self.frame_42)

        self.pushButton_25 = QPushButton(self.widget_25)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(70, 35))
        self.pushButton_25.setFont(font3)
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
        icon11 = QIcon()
        icon11.addFile(u":/icon2/icon_white/edit-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_25.setIcon(icon11)
        self.pushButton_25.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.pushButton_25, 0, Qt.AlignRight)

        self.pushButton_26 = QPushButton(self.widget_25)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(70, 35))
        self.pushButton_26.setFont(font3)
        self.pushButton_26.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_26.setIcon(icon11)
        self.pushButton_26.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.pushButton_26, 0, Qt.AlignRight)

        self.pushButton = QPushButton(self.widget_25)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_12.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.tab)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.scrollArea_3 = QScrollArea(self.widget_26)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 756, 335))
        self.horizontalLayout_24 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_3 = QTableWidget(self.scrollAreaWidgetContents_4)
        if (self.tableWidget_3.columnCount() < 9):
            self.tableWidget_3.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        font6.setWeight(75)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6);
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font6);
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_24.addWidget(self.tableWidget_3)

        self.widget_15 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 300))
        self.widget_15.setMaximumSize(QSize(0, 350))
        self.widget_15.setStyleSheet(u"background-color: rgb(0, 55, 80);")
        self.lineEdit_23 = QLineEdit(self.widget_15)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setGeometry(QRect(10, 20, 150, 40))
        self.lineEdit_23.setMinimumSize(QSize(150, 40))
        self.lineEdit_23.setMaximumSize(QSize(150, 40))
        self.lineEdit_23.setFont(font4)
        self.lineEdit_23.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_13 = QLineEdit(self.widget_15)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(10, 90, 150, 40))
        self.lineEdit_13.setMinimumSize(QSize(150, 40))
        self.lineEdit_13.setMaximumSize(QSize(150, 40))
        self.lineEdit_13.setFont(font4)
        self.lineEdit_13.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_20 = QLineEdit(self.widget_15)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(10, 160, 150, 40))
        self.lineEdit_20.setMinimumSize(QSize(150, 40))
        self.lineEdit_20.setMaximumSize(QSize(150, 40))
        self.lineEdit_20.setFont(font4)
        self.lineEdit_20.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_21 = QLineEdit(self.widget_15)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(230, 90, 150, 40))
        self.lineEdit_21.setMinimumSize(QSize(150, 40))
        self.lineEdit_21.setMaximumSize(QSize(150, 40))
        self.lineEdit_21.setFont(font4)
        self.lineEdit_21.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_22 = QLineEdit(self.widget_15)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(QRect(230, 20, 150, 40))
        self.lineEdit_22.setMinimumSize(QSize(150, 40))
        self.lineEdit_22.setMaximumSize(QSize(150, 40))
        self.lineEdit_22.setFont(font4)
        self.lineEdit_22.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_17 = QPushButton(self.widget_15)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(270, 300, 75, 23))
        self.pushButton_17.setFont(font3)
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
        self.pushButton_18.setGeometry(QRect(10, 290, 150, 40))
        self.pushButton_18.setFont(font3)
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
        self.lineEdit_25.setGeometry(QRect(230, 160, 150, 40))
        self.lineEdit_25.setMinimumSize(QSize(150, 40))
        self.lineEdit_25.setMaximumSize(QSize(150, 40))
        self.lineEdit_25.setFont(font4)
        self.lineEdit_25.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_27 = QLineEdit(self.widget_15)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setGeometry(QRect(10, 230, 150, 40))
        self.lineEdit_27.setMinimumSize(QSize(150, 40))
        self.lineEdit_27.setMaximumSize(QSize(150, 40))
        self.lineEdit_27.setFont(font4)
        self.lineEdit_27.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_28 = QLineEdit(self.widget_15)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setGeometry(QRect(230, 230, 150, 40))
        self.lineEdit_28.setMinimumSize(QSize(150, 40))
        self.lineEdit_28.setMaximumSize(QSize(150, 40))
        self.lineEdit_28.setFont(font4)
        self.lineEdit_28.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_24.addWidget(self.widget_15)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_14.addWidget(self.scrollArea_3)


        self.verticalLayout_16.addWidget(self.widget_26)

        self.tabWidget_2.addTab(self.tab, "")

        self.horizontalLayout_8.addWidget(self.tabWidget_2)


        self.verticalLayout_6.addWidget(self.widget_9)

        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_13 = QHBoxLayout(self.page_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_4 = QWidget(self.page_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_20 = QVBoxLayout(self.widget_4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_22 = QWidget(self.widget_4)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy)
        self.horizontalLayout_47 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy3.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy3)
        self.widget_23.setMaximumSize(QSize(16777215, 16777215))
        self.widget_23.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.widget_23)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.frame_34 = QFrame(self.widget_23)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(-1, 0, 9, 0)
        self.label_26 = QLabel(self.frame_34)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_48.addWidget(self.label_26, 0, Qt.AlignLeft)

        self.lineEdit_24 = QLineEdit(self.frame_34)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMinimumSize(QSize(200, 30))
        self.lineEdit_24.setFont(font4)
        self.lineEdit_24.setTabletTracking(True)
        self.lineEdit_24.setFocusPolicy(Qt.WheelFocus)
        self.lineEdit_24.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}\n"
"")
        self.lineEdit_24.setReadOnly(False)

        self.horizontalLayout_48.addWidget(self.lineEdit_24, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.widget_23)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFocusPolicy(Qt.NoFocus)
        self.frame_35.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(-1, 0, 9, 0)
        self.label_17 = QLabel(self.frame_35)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_49.addWidget(self.label_17, 0, Qt.AlignLeft)

        self.lineEdit_26 = QLineEdit(self.frame_35)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMinimumSize(QSize(200, 30))
        self.lineEdit_26.setFont(font4)
        self.lineEdit_26.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_26.setReadOnly(False)

        self.horizontalLayout_49.addWidget(self.lineEdit_26, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.widget_23)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(-1, 0, 9, 0)
        self.label_20 = QLabel(self.frame_36)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_50.addWidget(self.label_20, 0, Qt.AlignLeft)

        self.lineEdit_47 = QLineEdit(self.frame_36)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setMinimumSize(QSize(200, 30))
        self.lineEdit_47.setFont(font4)
        self.lineEdit_47.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_47.setReadOnly(False)

        self.horizontalLayout_50.addWidget(self.lineEdit_47, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.widget_23)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(-1, 0, 9, 0)
        self.label_21 = QLabel(self.frame_37)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_51.addWidget(self.label_21, 0, Qt.AlignLeft)

        self.lineEdit_48 = QLineEdit(self.frame_37)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setMinimumSize(QSize(200, 30))
        self.lineEdit_48.setFont(font4)
        self.lineEdit_48.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_48.setReadOnly(False)

        self.horizontalLayout_51.addWidget(self.lineEdit_48, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.frame_37)


        self.horizontalLayout_47.addWidget(self.widget_23)

        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_3)

        self.widget_24 = QWidget(self.widget_22)
        self.widget_24.setObjectName(u"widget_24")
        sizePolicy3.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy3)
        self.widget_24.setMaximumSize(QSize(16777215, 16777215))
        self.widget_24.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.widget_24)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 9, 0, 9)
        self.frame_38 = QFrame(self.widget_24)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(-1, 0, 9, 0)
        self.label_27 = QLabel(self.frame_38)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_52.addWidget(self.label_27, 0, Qt.AlignLeft)

        self.lineEdit_50 = QLineEdit(self.frame_38)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setMinimumSize(QSize(200, 30))
        self.lineEdit_50.setFont(font4)
        self.lineEdit_50.setTabletTracking(True)
        self.lineEdit_50.setFocusPolicy(Qt.WheelFocus)
        self.lineEdit_50.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}\n"
"")
        self.lineEdit_50.setReadOnly(False)

        self.horizontalLayout_52.addWidget(self.lineEdit_50, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.widget_24)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFocusPolicy(Qt.NoFocus)
        self.frame_39.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(-1, 0, 9, 0)
        self.label_28 = QLabel(self.frame_39)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_53.addWidget(self.label_28, 0, Qt.AlignLeft)

        self.lineEdit_51 = QLineEdit(self.frame_39)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setMinimumSize(QSize(200, 30))
        self.lineEdit_51.setFont(font4)
        self.lineEdit_51.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_51.setReadOnly(False)

        self.horizontalLayout_53.addWidget(self.lineEdit_51, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.widget_24)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(9, 0, 9, 0)
        self.label_29 = QLabel(self.frame_40)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_54.addWidget(self.label_29, 0, Qt.AlignLeft)

        self.lineEdit_52 = QLineEdit(self.frame_40)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setMinimumSize(QSize(200, 30))
        self.lineEdit_52.setFont(font4)
        self.lineEdit_52.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_52.setReadOnly(False)

        self.horizontalLayout_54.addWidget(self.lineEdit_52, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.widget_24)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"background-color: rgb(154, 154, 154);\n"
"border-radius: 10px")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.pushButton_8 = QPushButton(self.frame_41)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font3)
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 137, 206);\n"
"	\n"
"}\n"
"")

        self.horizontalLayout_55.addWidget(self.pushButton_8, 0, Qt.AlignLeft)

        self.lineEdit_53 = QLineEdit(self.frame_41)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setMinimumSize(QSize(200, 30))
        self.lineEdit_53.setFont(font4)
        self.lineEdit_53.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus{\n"
"border: 3px solid #FBAD25;\n"
"}")
        self.lineEdit_53.setReadOnly(True)

        self.horizontalLayout_55.addWidget(self.lineEdit_53, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_41)


        self.horizontalLayout_47.addWidget(self.widget_24)


        self.verticalLayout_20.addWidget(self.widget_22)

        self.widget_31 = QWidget(self.widget_4)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMinimumSize(QSize(0, 80))
        self.widget_31.setStyleSheet(u"")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.widget_31)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 55))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.pushButton_15 = QPushButton(self.frame_48)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(150, 40))
        self.pushButton_15.setMaximumSize(QSize(200, 50))
        self.pushButton_15.setFont(font5)
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_15.setIcon(icon5)
        self.pushButton_15.setIconSize(QSize(20, 20))

        self.horizontalLayout_57.addWidget(self.pushButton_15, 0, Qt.AlignHCenter)


        self.horizontalLayout_56.addWidget(self.frame_48)


        self.verticalLayout_20.addWidget(self.widget_31)


        self.horizontalLayout_13.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.main)


        self.horizontalLayout_11.addWidget(self.body)


        self.verticalLayout.addWidget(self.widget_2)

        new_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(new_2)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(new_2)
    # setupUi

    def retranslateUi(self, new_2):
        new_2.setWindowTitle(QCoreApplication.translate("new_2", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("new_2", u"Automated Federal Police Database Management System", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.label_6.setText(QCoreApplication.translate("new_2", u"Fedral Police", None))
        self.pushButton_5.setText(QCoreApplication.translate("new_2", u"Home", None))
        self.pushButton_10.setText(QCoreApplication.translate("new_2", u"Register", None))
        self.pushButton_6.setText(QCoreApplication.translate("new_2", u"Records", None))
        self.menu_btn.setText("")
        self.label_2.setText("")
        self.appname.setText(QCoreApplication.translate("new_2", u"Automated Federal Police Database Management System", None))
        self.account_btn.setText(QCoreApplication.translate("new_2", u"Log out", None))
        self.label_4.setText("")
        self.label_30.setText(QCoreApplication.translate("new_2", u"ID", None))
        self.label_18.setText(QCoreApplication.translate("new_2", u"Name", None))
        self.label_22.setText(QCoreApplication.translate("new_2", u"Phone no", None))
        self.label_23.setText(QCoreApplication.translate("new_2", u"Case", None))
        self.label_24.setText(QCoreApplication.translate("new_2", u"Address", None))
        self.label_31.setText(QCoreApplication.translate("new_2", u"Age", None))
        self.label_32.setText(QCoreApplication.translate("new_2", u"Gender", None))
        self.pushButton_7.setText(QCoreApplication.translate("new_2", u"Browse", None))
        self.pushButton_9.setText(QCoreApplication.translate("new_2", u"check", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabss), QCoreApplication.translate("new_2", u"Face Recognation", None))
        self.label_3.setText("")
        self.label_25.setText(QCoreApplication.translate("new_2", u"ID", None))
        self.label_15.setText(QCoreApplication.translate("new_2", u"Name", None))
        self.label_19.setText(QCoreApplication.translate("new_2", u"Phone no", None))
        self.label_16.setText(QCoreApplication.translate("new_2", u"Address", None))
        self.label_33.setText(QCoreApplication.translate("new_2", u"Case", None))
        self.label_34.setText(QCoreApplication.translate("new_2", u"Gender", None))
        self.pushButton_16.setText(QCoreApplication.translate("new_2", u"Browse", None))
        self.pushButton_14.setText(QCoreApplication.translate("new_2", u"check", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("new_2", u"Fingerprint", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("new_2", u"Camera and Video", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("new_2", u"Specific Person", None))
        self.lineEdit_32.setPlaceholderText(QCoreApplication.translate("new_2", u"search by name", None))
        self.pushButton_22.setText("")
        self.pushButton_25.setText(QCoreApplication.translate("new_2", u"Update", None))
        self.pushButton_26.setText(QCoreApplication.translate("new_2", u"Delete", None))
        self.pushButton.setText("")
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("new_2", u"Address", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("new_2", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("new_2", u"Name", None));
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("new_2", u"Phone No", None));
        ___qtablewidgetitem4 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("new_2", u"Case", None));
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("new_2", u"Age", None));
        ___qtablewidgetitem6 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("new_2", u"Gender", None));
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("new_2", u"Fingerprint", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("new_2", u"Photo", None));
        self.pushButton_17.setText(QCoreApplication.translate("new_2", u"Done", None))
        self.pushButton_18.setText(QCoreApplication.translate("new_2", u"Take Photo", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("new_2", u"Crime Records", None))
        self.label_26.setText(QCoreApplication.translate("new_2", u"Crimnal ID", None))
        self.label_17.setText(QCoreApplication.translate("new_2", u"Name", None))
        self.label_20.setText(QCoreApplication.translate("new_2", u"Phone No", None))
        self.label_21.setText(QCoreApplication.translate("new_2", u"Case", None))
        self.label_27.setText(QCoreApplication.translate("new_2", u"Address", None))
        self.label_28.setText(QCoreApplication.translate("new_2", u"Age", None))
        self.label_29.setText(QCoreApplication.translate("new_2", u"Gender", None))
        self.pushButton_8.setText(QCoreApplication.translate("new_2", u"Photo", None))
        self.pushButton_15.setText(QCoreApplication.translate("new_2", u"Register", None))
    # retranslateUi

