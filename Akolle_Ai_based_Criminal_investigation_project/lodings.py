import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QLabel,QWidget
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QMovie

class Loading(QWidget):
    def __init__(self):
        super(Loading, self).__init__()
        self.setFixedSize(200,200)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.label_animation = QLabel(self)
        self.label_animation.setStyleSheet("background-color: rgb(0, 147, 220);")
        self.movie = QMovie("Loading_2.gif")
        self.label_animation.setMovie(self.movie)
        #timer = QTimer(self)
        self.animation()
        #timer.singleShot(3000,self.stop_animation)

    def animation(self):
        self.movie.start()

    #def stop_animation(self):
     #   self.movie.stop()
      #  self.close()

app = QApplication(sys.argv)
dialog = QtWidgets.QStackedWidget()
demo = Loading()
demo.show()
sys.exit(app.exec_())

