import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QMovie
from ui_welcom import *
from ui_logins import *
from PyQt5.QtWidgets import QFileDialog
from PySide2.QtCore import *
from PySide2 import QtCore
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import *
from ui_navigation import *
from ui_adminster import *
import sqlite3
from PyQt5.QtGui import QPixmap
import os
from datetime import datetime
import cv2
import face_recognition
import numpy as np
import PySide2
from ui_homess import *
import iconify as ico
from ui_login_ad import *

class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.wl = Ui_WeLLC()
        self.wl.setupUi(self)
        self.show()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.wl.log_in.clicked.connect(lambda :self.loging())
        self.wl.log_in_2.clicked.connect(lambda : self.adminsters())
        self.wl.log_in_3.clicked.connect(lambda : self.window().close())

    def loging(self):
        self.log = Log()
        self.log.show()
        self.window().close()

    def adminsters(self):
        self.adminster = Admlog()
        self.adminster.show()
        self.window().close()

class Log(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.lg = Ui_LOGIN()
        self.lg.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.lg.pushButton_2.clicked.connect(lambda: self.back())
        icona1 = ico.Icon('dash:arrow-left-alt')
        self.lg.pushButton_2.setIcon(icona1)
        self.lg.pushButton_2.setIconSize(QSize(32, 32))

        self.lg.pushButton_8.clicked.connect(lambda: self.loged())
        self.lg.pushButton.clicked.connect(lambda: self.hidde())
        self.lg.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lg.lineEdit_3.returnPressed.connect(self.loged)

    def hidde(self):
        if self.lg.lineEdit_3.echoMode() == PySide2.QtWidgets.QLineEdit.EchoMode.Password:

             self.lg.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
             self.lg.pushButton.setIcon(QtGui.QIcon(u":/icon2/icon_white/eye-off.svg"))

        elif self.lg.lineEdit_3.echoMode() == PySide2.QtWidgets.QLineEdit.EchoMode.Normal:
            self.lg.pushButton.setIcon(QtGui.QIcon(u":/icon2/icon_white/eye.svg"))
            self.lg.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)

    def loged(self):
        user = self.lg.lineEdit_2.text()
        code = self.lg.lineEdit_3.text()

        if len(user) == 0 or len(code) == 0:
            self.lg.label.setText("please insert all fields!")

        else:
            try:
                conn = sqlite3.connect("Polices.db")
                cur = conn.cursor()
                query = 'SELECT Name,Password FROM police_records WHERE Name = ? AND Password = ?'
                cur.execute(query, (user, code))
                result_pass = cur.fetchall()[0]
                print(result_pass[0])

                if result_pass[0] == user and result_pass[1] == code:
                    self.home = New()
                    self.home.show()
                    self.window().close()
            except:
                self.lg.label.setText("Invalid Username or Password")

    def back(self):
        self.back = Main()
        self.back.show()
        self.window().close()

class Admlog(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.gl = Ui_LOGINS()
        self.gl.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.gl.pushButton_8.clicked.connect(lambda: self.loged())
        self.gl.pushButton.clicked.connect(lambda: self.hidde())
        self.gl.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gl.lineEdit_3.returnPressed.connect(self.loged)
        self.gl.pushButton_2.clicked.connect(lambda: self.back())

        icona1 = ico.Icon('dash:arrow-left-alt')
        icona = ico.Icon('feather:eye')

        self.gl.pushButton.setIcon(icona)
        self.gl.pushButton_2.setIcon(icona1)
        self.gl.pushButton_2.setIconSize(QSize(32, 32))

    def hidde(self):
        icona = ico.Icon('feather:eye')
        iconab = ico.Icon('feather:eye-off')
        if self.gl.lineEdit_3.echoMode() == PySide2.QtWidgets.QLineEdit.EchoMode.Password:

            self.gl.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.gl.pushButton.setIcon(iconab)

        elif self.gl.lineEdit_3.echoMode() == PySide2.QtWidgets.QLineEdit.EchoMode.Normal:
            self.gl.pushButton.setIcon(icona)
            self.gl.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)

    def loged(self):
        user = self.gl.lineEdit_2.text()
        code = self.gl.lineEdit_3.text()

        if len(user) == 0 or len(code) == 0:
            self.gl.label.setText("please insert all fields!")
        else:
            try:
                conn = sqlite3.connect("admin.db")
                cur = conn.cursor()
                query = 'SELECT username,password FROM admin WHERE username = ? AND password = ?'
                cur.execute(query, (user, code))
                result_pass = cur.fetchall()[0]
                print(result_pass[0])

                if result_pass[0] == user and result_pass[1] == code:
                    self.admin = Adminster()
                    self.admin.show()
                    self.window().close()
            except:
                self.gl.label.setText("Invalid Username or Password")

    def back(self):
        self.backs = Main()
        self.backs.show()
        self.window().close()

class Adminster(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ad = Ui_adminster()
        self.ad.setupUi(self)
        self.show()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.dragPos = QtCore.QPoint()

        self.ad.Create_Account.clicked.connect(lambda: self.ad.stackedWidget.setCurrentWidget(self.ad.page))
        self.ad.Police_Records.clicked.connect(lambda: self.ad.stackedWidget.setCurrentWidget(self.ad.page_3))
        self.ad.Criminal_Records.clicked.connect(lambda: self.ad.stackedWidget.setCurrentWidget(self.ad.page_4))

        self.ad.pushButton_4.clicked.connect(lambda: self.window().close())
        self.ad.pushButton_2.clicked.connect(lambda: self.window().showMinimized())
        self.ad.pushButton_3.clicked.connect(lambda: self.res_max())

        self.ad.menu_btn.clicked.connect(lambda : self.menu())
        self.ad.pushButton_7.clicked.connect(lambda : self.create_account())
        self.ad.pushButton_13.clicked.connect(lambda : self.police_reco())
        self.ad.pushButton_23.clicked.connect(lambda: self.crime_record())
        self.ad.account_btn.clicked.connect(lambda : self.logout())
        self.ad.pushButton_18.clicked.connect(lambda : self.update_imagepath())
        self.ad.pushButton_24.clicked.connect(lambda : self.delete())
        self.ad.pushButton_25.clicked.connect(lambda : self.update())
        self.ad.pushButton_17.clicked.connect(lambda: self.done())

        self.ad.pushButton_30.clicked.connect(lambda : self.delete_police())
        self.ad.pushButton_31.clicked.connect(lambda : self.update_police())
        self.ad.pushButton_19.clicked.connect(lambda: self.done_police())
        self.ad.lineEdit_19.setFocus()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def res_max(self):
        if self.isMaximized():
            icon41 = ico.Icon('feather:square')
            self.ad.pushButton_3.setIcon(icon41)
            self.ad.pushButton_3.setIconSize(QSize(20, 20))
            self.showNormal()
        else:
            icon31 = ico.Icon('feather:minimize-2')
            self.ad.pushButton_3.setIcon(icon31)
            self.ad.pushButton_3.setIconSize(QSize(20, 20))
            self.showMaximized()

    def menu(self):
        width = self.ad.left.width()

        if width == 0:
            new_width = 200

        else:
            new_width = 0

        self.animation = QPropertyAnimation(self.ad.left,b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()

    def create_account(self):
        id = self.ad.lineEdit_19.text()
        user = self.ad.lineEdit_11.text()
        code = self.ad.lineEdit_16.text()
        phone_no = self.ad.lineEdit_17.text()
        adress = self.ad.lineEdit_14.text()
        age = self.ad.lineEdit_15.text()
        gender = self.ad.lineEdit_18.text()

        if id == "" or user == "" or code == "" or phone_no == "" or adress == "" or age == "" or gender == "":
            QMessageBox.information(None,"Warning","enter all the element")
        else:
            user_info = [id,user,code,phone_no,adress,age,gender]

            conn = sqlite3.connect("Polices.db")
            cur = conn.cursor()

            cur.execute("INSERT INTO police_records(Id,Name,Password,Phone_no,Adress,Age,Gender) VALUES(?,?,?,?,?,?,?)",user_info)

            conn.commit()
            conn.close()
            self.ad.lineEdit_19.setText("")
            self.ad.lineEdit_11.setText("")
            self.ad.lineEdit_16.setText("")
            self.ad.lineEdit_17.setText("")
            self.ad.lineEdit_14.setText("")
            self.ad.lineEdit_15.setText("")
            self.ad.lineEdit_18.setText("")

    def police_reco(self):

        db = sqlite3.connect("Polices.db")
        cur = db.cursor()
        qurey = "select * from police_records"
        result = cur.execute(qurey)

        self.ad.tableWidget.setRowCount(0)
        for row,row_data in enumerate(result):
            self.ad.tableWidget.insertRow(row)
            for colum_no,data in enumerate(row_data):
                self.ad.tableWidget.setItem(row,colum_no,QTableWidgetItem(str(data)))

    def crime_record(self):
        db = sqlite3.connect("registration_form.db")
        cur = db.cursor()
        qurey = "select * from registration"
        result = cur.execute(qurey)

        self.ad.tableWidget_3.setRowCount(0)
        for row, row_data in enumerate(result):
            self.ad.tableWidget_3.insertRow(row)
            for colum_no, data in enumerate(row_data):
                if colum_no == 7:
                    item = self.setlabels(data)
                    self.ad.tableWidget_3.setCellWidget(row, colum_no, item)
                else:
                    self.ad.tableWidget_3.setItem(row, colum_no, QTableWidgetItem(str(data)))
        self.ad.tableWidget_3.verticalHeader().setDefaultSectionSize(80)

    def setlabels(self,img):
        image_labels = QtWidgets.QLabel(self.ad.centralwidget)
        image_labels.setText("")
        image_labels.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.load(img,'jpg')
        image_labels.setPixmap(pixmap)
        return image_labels

    def logout(self):
        self.logout = Main()
        self.logout.show()
        self.window().close()

    def update_imagepath(self):
        self.ad.lineEdit_25.setText("")
        frames = QFileDialog.getOpenFileName(self, 'update image file', 'C:/', 'Images File (*.png *.jpg *.svg )')
        self.ad.lineEdit_25.setText(frames[0])

    def delete(self):
        db = sqlite3.connect("registration_form.db")
        cur = db.cursor()
        name = self.ad.lineEdit_32.text()

        delete = 'DELETE FROM registration WHERE Id = \'' + name + "\'"

        cur.execute(delete)
        db.commit()
        self.ad.lineEdit_32.setText("")

    def update(self):
        db = sqlite3.connect("registration_form.db")
        cur = db.cursor()
        name = self.ad.lineEdit_32.text()

        width = self.ad.widget_15.width()

        if width == 0:
            new_width = 400

        else:
            new_width = 0

        self.animation = QPropertyAnimation(self.ad.widget_15, b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InSine)
        self.animation.start()

        cur.execute('select * FROM registration WHERE Id = \'' + name + "\'")
        re = cur.fetchall()
        for i in re:
            self.ad.lineEdit_26.setText(str(i[0]))
            self.ad.lineEdit_23.setText(str(i[1]))
            self.ad.lineEdit_13.setText(str(i[2]))
            self.ad.lineEdit_20.setText(str(i[3]))
            self.ad.lineEdit_24.setText(str(i[4]))
            self.ad.lineEdit_22.setText(str(i[5]))
            self.ad.lineEdit_21.setText(str(i[6]))
            self.ad.lineEdit_25.setText(str(i[7]))

    def done(self):
        db = sqlite3.connect("registration_form.db")
        cur = db.cursor()

        codes = self.ad.lineEdit_32.text()
        id = self.ad.lineEdit_26.text()
        name = self.ad.lineEdit_23.text()
        phone_no = self.ad.lineEdit_13.text()
        cases = self.ad.lineEdit_20.text()
        Adress = self.ad.lineEdit_24.text()
        age = self.ad.lineEdit_22.text()
        gender = self.ad.lineEdit_21.text()
        phto_path = self.ad.lineEdit_25.text()

        update = [id,name,phone_no,cases,Adress,age,gender,phto_path]

        queary = ("UPDATE registration SET Id = ? ,Name = ? ,Phone_no = ? ,cases = ?,Adress = ?,Age = ?,Gender = ?,Photo = ? WHERE Id = ?")
        cur.execute(queary,(id,name,phone_no,cases,Adress,age,gender,phto_path,codes))
        db.commit()
        db.close()

        width = self.ad.widget_15.width()

        if width != 0:
            new_width = 0
        self.animation = QPropertyAnimation(self.ad.widget_15, b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()

        self.ad.lineEdit_32.setText("")
        QMessageBox.information(None, "Message", "Successfully Updated")

    def delete_police(self):
        db = sqlite3.connect("Polices.db")
        cur = db.cursor()
        name = self.ad.lineEdit_10.text()

        delete = 'DELETE FROM police_records WHERE Id = \'' + name + "\'"

        cur.execute(delete)
        db.commit()
        self.ad.lineEdit_10.setText("")

    def update_police(self):
        db = sqlite3.connect("Polices.db")
        cur = db.cursor()
        name = self.ad.lineEdit_10.text()

        width = self.ad.widget_16.width()
        height = self.ad.widget_16.height()
        geo = self.ad.widget_16.geometry()

        if width == 0:
            new_width = 400

        else:
            new_width = 0

        self.animation = QPropertyAnimation(self.ad.widget_16, b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(QRect(458,15,new_width,height))
        self.animation.setEndValue(QRect(458,15,new_width,height))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InBack)
        self.animation.setDirection()
        self.animation.start()

        cur.execute('select * FROM police_records WHERE Id = \'' + name + "\'")
        re = cur.fetchall()

        for i in re:
            self.ad.lineEdit_27.setText(str(i[1]))
            self.ad.lineEdit_28.setText(str(i[2]))
            self.ad.lineEdit_29.setText(str(i[3]))
            self.ad.lineEdit_30.setText(str(i[6]))
            self.ad.lineEdit_31.setText(str(i[5]))
            self.ad.lineEdit_33.setText(str(i[4]))
            self.ad.lineEdit_35.setText(str(i[0]))

    def done_police(self):
        db = sqlite3.connect("Polices.db")
        cur = db.cursor()

        codes = self.ad.lineEdit_10.text()

        id = self.ad.lineEdit_35.text()
        name = self.ad.lineEdit_27.text()
        password = self.ad.lineEdit_28.text()
        phone_no = self.ad.lineEdit_29.text()
        Adress = self.ad.lineEdit_33.text()
        age = self.ad.lineEdit_31.text()
        gender = self.ad.lineEdit_30.text()


        queary = ("UPDATE police_records SET Id = ? ,Name = ? ,Password = ?, Phone_no = ?,Adress = ?,Age = ?,Gender = ? WHERE Id = ?")
        cur.execute(queary,(id,name,password,phone_no,Adress,age,gender,codes))
        db.commit()
        db.close()

        width = self.ad.widget_16.width()

        if width != 0:
            new_width = 0
        self.animation = QPropertyAnimation(self.ad.widget_16, b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()
        #self.animation.setDirection()

        self.ad.lineEdit_10.setText("")

class New(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.nw = Ui_new_2()
        self.nw.setupUi(self)
        self.show()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        icon1 = ico.Icon('feather:menu', color=QtGui.QColor('white'))
        self.nw.menu_btn.setIcon(icon1)
        self.nw.pushButton_5.setIconSize(QSize(30, 30))

        self.nw.menu_btn.clicked.connect(lambda: self.slidemenu())

        self.nw.pushButton_5.clicked.connect(lambda: self.nw.stackedWidget.setCurrentWidget(self.nw.page))
        self.nw.pushButton_10.clicked.connect(lambda: self.nw.stackedWidget.setCurrentWidget(self.nw.page_2))
        self.nw.pushButton_6.clicked.connect(lambda: self.nw.stackedWidget.setCurrentWidget(self.nw.page_4))

        self.nw.pushButton_7.clicked.connect(lambda : self.browse_image())
        #self.nw.pushButton_8.clicked.connect(lambda: self.change_color())

        self.nw.pushButton_15.clicked.connect(lambda: self.registration())
        self.nw.pushButton_8.clicked.connect(lambda: self.take_photo())

        self.nw.pushButton_4.clicked.connect(lambda: self.window().close())
        self.nw.pushButton_2.clicked.connect(lambda: self.window().showMinimized())
        self.nw.pushButton_3.clicked.connect(lambda: self.res_max())
        self.nw.pushButton.clicked.connect(lambda: self.refrash())
        self.nw.pushButton_9.clicked.connect(lambda: self.face_recations())
        self.nw.account_btn.clicked.connect(lambda: self.logout())
        self.nw.pushButton_16.clicked.connect(lambda: self.fingmatch())

        self.dragPos = QtCore.QPoint()
        self.show()

        self.anim_spin = ico.anim.Spin()
        self.icon_refrash = ico.Icon(
            'material-design:refresh-circle',
            color=QtGui.QColor('black'),
            anim=self.anim_spin,
            # mode = QtGui.QIcon.Active,
        )
        self.nw.pushButton.setIconSize(QSize(70, 70))
        self.icon_refrash.setAsButtonIcon(self.nw.pushButton)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def res_max(self):
        if self.isMaximized():
            icon41 = ico.Icon('feather:square')
            self.nw.pushButton_3.setIcon(icon41)
            self.nw.pushButton_3.setIconSize(QSize(20, 20))
            self.showNormal()
        else:
            icon31 = ico.Icon('feather:minimize-2')
            self.nw.pushButton_3.setIcon(icon31)
            self.nw.pushButton_3.setIconSize(QSize(20, 20))
            self.showMaximized()

    def change_color(self):

        self.ui.centralwidget.setStyleSheet("background-color: rgb(0, 64, 94);")

    def refrash(self):
        self.anim_spin.start()
        db = sqlite3.connect("registration_form.db")
        cur = db.cursor()
        qurey = "select * from registration"
        result = cur.execute(qurey)

        self.timer = QTimer()
        self.timer.singleShot(2000,self.anim_spin.stop)
        self.nw.tableWidget_3.setRowCount(0)
        for row,row_data in enumerate(result):
            self.nw.tableWidget_3.insertRow(row)
            for colum_no,data in enumerate(row_data):
                if colum_no ==  8:
                    item = self.setlabel(data)
                    self.nw.tableWidget_3.setCellWidget(row,colum_no,item)

                elif colum_no == 7:
                    items = self.setlabels(data)
                    self.nw.tableWidget_3.setCellWidget(row, colum_no, items)

                else:
                    self.nw.tableWidget_3.setItem(row,colum_no,QTableWidgetItem(str(data)))
        self.nw.tableWidget_3.verticalHeader().setDefaultSectionSize(80)

    def setlabel(self,img):
        image_label = QtWidgets.QLabel(self.nw.centralwidget)
        image_label.setText("")
        image_label.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.load(img)
        image_label.setPixmap(pixmap)
        return image_label

    def setlabels(self,im):
        image_label = QtWidgets.QLabel(self.nw.centralwidget)
        image_label.setText("")
        image_label.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.load(im)
        image_label.setPixmap(pixmap)
        return image_label

    def fingmatch(self):
        frame = QFileDialog.getOpenFileName(self, 'open file', 'C:/', 'Images File (*.BMP *.jpg *.svg )')
        self.nw.label_3.setPixmap(QtGui.QPixmap(frame[0]))

    def face_recations(self):
        QMessageBox.information(None, "Error", "Face Not Detected")
        conns = sqlite3.connect("registration_form.db")
        curs = conns.cursor()
        query = "SELECT Photo FROM registration"
        curs.execute(query)
        result_pass = curs.fetchall()  # it gives a list of tuples
        path_list = []
        for i in result_pass:
            for j in i:
                path_list.append(j)
        images = []
        for image in path_list:
            img = cv2.imread(image)
            images.append(img)

        def encoding(images):
            encod_list = []
            for img in images:
                encode_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encod = face_recognition.face_encodings(encode_image)[0]
                encod_list.append(encod)

            return encod_list

        known_encode = encoding(images)
        img_path = self.nw.lineEdit.text()
        def recognation(path):
            if not path == "":

                image_com = cv2.imread(path)

                imgc = cv2.cvtColor(image_com, cv2.COLOR_BGR2RGB)

                face_loc = face_recognition.face_locations(imgc)[0]
                face_encd = face_recognition.face_encodings(imgc)[0]

                if len(face_encd) == 0:
                    QMessageBox.information(None, "Error", "Face Not Detected")

                else:

                    result = face_recognition.compare_faces(known_encode,face_encd)
                    facedis = face_recognition.face_distance(known_encode, face_encd)
                    match_index = np.argmin(facedis)

                    return result, facedis, match_index
            else:
                QMessageBox.information(None,"Warning","First take image from Dirictory")

        res,fadi,maini = recognation(img_path)
        print(res,fadi,maini)

        if any(res) == True:

            connections = sqlite3.connect("registration_form.db")
            curs = connections.cursor()
            query = "SELECT * FROM registration"
            curs.execute(query)

            resltan = curs.fetchall()[maini][:]
            print(resltan)

            self.nw.lineEdit_36.setText(str(resltan[0]))
            self.nw.lineEdit_34.setText(str(resltan[1]))
            self.nw.lineEdit_56.setText(str(resltan[2]))
            self.nw.lineEdit_38.setText(str(resltan[3]))
            self.nw.lineEdit_40.setText(str(resltan[4]))
            self.nw.lineEdit_57.setText(str(resltan[5]))
            self.nw.lineEdit_58.setText(str(resltan[6]))

        else:
            QMessageBox.information(None,"Warning","Unknown Person")

    def browse_image(self):

        frame = QFileDialog.getOpenFileName(self, 'open file', 'C:/', 'Images File (*.png *.jpg *.svg )')
        self.nw.label_4.setPixmap(QtGui.QPixmap(frame[0]))
        self.nw.lineEdit.setText(frame[0])

        self.nw.lineEdit_36.setText("")
        self.nw.lineEdit_34.setText("")
        self.nw.lineEdit_56.setText("")
        self.nw.lineEdit_38.setText("")
        self.nw.lineEdit_57.setText("")
        self.nw.lineEdit_58.setText("")

    def take_photo(self):
        frame = QFileDialog.getOpenFileName(self,'open file','C:/','Images File (*.png *.jpg *.svg )')
        self.nw.lineEdit_53.setText(frame[0])

    def registration(self):
        id = self.nw.lineEdit_24.text()
        name = self.nw.lineEdit_26.text()
        phone_no = self.nw.lineEdit_47.text()
        Cases = self.nw.lineEdit_48.text()
        Adress = self.nw.lineEdit_50.text()
        Age = self.nw.lineEdit_51.text()
        Gender = self.nw.lineEdit_52.text()
        Photo = self.nw.lineEdit_53.text()

        if id == "" or name == "" or phone_no == "" or Cases == "" or Adress == "" or Age == "" or Gender == "" or Photo == "":
            QMessageBox.information(None,"Warning","please enter all fields!")

        else:
            conns = sqlite3.connect("registration_form.db")
            curs = conns.cursor()

            user_info = [id,name, phone_no,Cases,Adress,Age,Gender,Photo]
            curs.execute("INSERT INTO registration(ID,Name, Phone_no,cases,Adress,Age,Gender,Photo) VALUES(?,?,?,?,?,?,?,?)", user_info)

            conns.commit()
            conns.close()

            self.nw.lineEdit_24.setText("")
            self.nw.lineEdit_26.setText("")
            self.nw.lineEdit_47.setText("")
            self.nw.lineEdit_48.setText("")
            self.nw.lineEdit_50.setText("")
            self.nw.lineEdit_51.setText("")
            self.nw.lineEdit_52.setText("")
            self.nw.lineEdit_53.setText("")

    def slidemenu(self):
        width = self.nw.left.width()

        if width == 0:
            new_width = 200

        else:
            new_width = 0

        self.animation = QPropertyAnimation(self.nw.left,b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()

    def logout(self):
        self.logouts = Main()
        self.logouts.show()
        self.window().close()


app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec_())