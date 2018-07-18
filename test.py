# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
import pyperclip

def youtube_download():

    link = pyperclip.paste()

    video = YouTube(link)
    download = video.streams.first().download(
        '/home/gonkaos/Documents/youtube_downloads'
    )

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(400, 300)
        Form.setWindowOpacity(0.8)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(100, 180, 261, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 20, 231, 101))
        self.label.setStyleSheet("font: 75 oblique 11pt \"Waree\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 140, 261, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 91, 21))
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.lineEdit.selectAll)
        self.pushButton.clicked.connect(self.lineEdit.copy)
        self.pushButton.clicked.connect(self.lineEdit.paste)
        self.pushButton.released.connect(youtube_download)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MyFIrstWidget"))
        self.label.setText(_translate("Form", "<html><head/><body><p>This is a simple program that</p><p>allows you to download </p><p>videos from youtube</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
