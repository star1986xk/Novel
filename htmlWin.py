from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

import sys
from UI.Ui_mainWin import Ui_Form
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QApplication, QHeaderView, QFileDialog

class htmlWin(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Browser')
        self.resize(1400,900)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        self.webview = QWebEngineView()
        self.webview.load(QUrl("http://127.0.0.1:8888/"))
        self.verticalLayout_2.addWidget(self.webview)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = htmlWin()
    win.show()
    sys.exit(app.exec_())