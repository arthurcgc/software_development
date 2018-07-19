from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Downloader(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()
        self.link = QLineEdit()
        progress = QProgressBar()
        download = QPushButton("Download")

        self.link.setPlaceholderText("Download Link")
        progress.setValue(24)

        layout.addWidget(self.link)
        layout.addWidget(download)
        layout.addWidget(progress)

        self.setWindowTitle("Youtube Scraper")
        self.setFocus()
        self.setLayout(layout)


        download.clicked.connect(self.script)

    def script(self,link):
        url = self.link.text()
        print(url)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    GUI = Downloader()
    GUI.show()
    sys.exit(app.exec_())
