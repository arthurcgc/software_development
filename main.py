# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from pytube import *
from pydub import AudioSegment

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def showsuccess():
    msg = QtGui.QMessageBox()
    msg.setIcon(QtGui.QMessageBox.Information)
    msg.setText("File Downloaded!")
    msg.exec_()

def dir_failure():
    msg = QtGui.QMessageBox()
    msg.setIcon(QtGui.QMessageBox.Information)
    msg.setText("Invalid directory path")
    msg.exec_()

def no_audio():
    msg = QtGui.QMessageBox()
    msg.setIcon(QtGui.QMessageBox.Information)
    msg.setText("No audio-only avaible in this video")
    msg.exec_()

def showfailed():
    msg = QtGui.QMessageBox()
    msg.setIcon(QtGui.QMessageBox.Information)
    msg.setText("URL is not valid, file could not be downloaded")
    msg.exec_()

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        QtGui.QApplication.setStyle("cleanlooks")
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Youtube Scraper"))
        Form.resize(450, 230)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("cleanlooks"))
        Form.setWindowIcon(icon)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 190, 100, 35))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setIcon(QtGui.QIcon("download.png"))

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(5, 100, 100, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setIcon(QtGui.QIcon("dir_icon.ico"))

        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 100, 335, 25))
        self.lineEdit_2.setInputMask(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.locationText = QtGui.QTextEdit()

        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 160, 435, 25))
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(20, 130, 61, 23))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 130, 61, 23))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 300, 70))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))



        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("pressed()")), self.getfile)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("pressed()")), self.download_script)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("released()")), self.pushButton.update)


        QtCore.QMetaObject.connectSlotsByName(Form)



    def getfile(self):
      dlg = QtGui.QFileDialog()
      dlg.setFileMode(QtGui.QFileDialog.Directory)

      if dlg.exec_():
         dirName = dlg.selectedFiles()
         f = dirName[0]
         self.lineEdit_2.setText(f)

    def download_script(self):
        url = self.lineEdit.text()
        try:
            file = YouTube(url)
        except:
            showfailed()
            raise ValueError

        directory = self.lineEdit_2.text()

        if self.radioButton.isChecked():
            try:
                file.streams.first().download(directory)
            except FileNotFoundError:
                dir_failure()
                raise FileNotFoundError

        elif self.radioButton_2.isChecked():
            audio = file.streams.filter(only_audio=True).first()
            try:
                audio.download(directory)
            except FileNotFoundError:
                dir_failure()
                raise FileNotFoundError
            except AttributeError:
                no_audio()
                raise AttributeError

        showsuccess()


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Youtube Scraper", "Youtube Scraper", None))
        Form.setWindowIcon(QtGui.QIcon("icon.png"))
        self.pushButton.setText(_translate("Form", "Download", None))
        # edit
        self.pushButton_2.setText(_translate("Form", "Directory", None))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Dir Location", None))
        # edit
        self.lineEdit.setPlaceholderText(_translate("Form", "url", None))
        self.radioButton.setText(_translate("Form", "video", None))
        self.radioButton_2.setText(_translate("Form", "audio", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose file type then hit download.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The best avaible resolution will be downloaded.</p></body></html>", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
