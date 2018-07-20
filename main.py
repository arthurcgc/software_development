# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstWindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        QtGui.QApplication.setStyle("cleanlooks")
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Youtube Scraper"))
        Form.resize(400, 300)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("cleanlooks"))
        Form.setWindowIcon(icon)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 190, 89, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        #testing shit
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 100, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 100, 271, 25))
        self.lineEdit_2.setInputMask(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.locationText = QtGui.QTextEdit()
        #testing shit

        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 160, 271, 25))
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
        self.textBrowser.setGeometry(QtCore.QRect(60, 20, 256, 71))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 220, 381, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))


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
        file = YouTube(url)
        directory = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            file.streams.first().download(directory)

        elif self.radioButton_2.isChecked():
            audio = file.streams.filter(only_audio=True).first()
            audio.download(directory)
            mp3 = directory + "/" + audio.default_filename
            sound = AudioSegment.from_file(mp3)
            sound.export(directory + "/" + file.title)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Youtube Scraper", "Youtube Scraper", None))
        Form.setWindowIcon(QtGui.QIcon("icon.png"))
        self.pushButton.setText(_translate("Form", "Download", None))
        # edit
        self.pushButton_2.setText(_translate("Form", "File Directory", None))
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
