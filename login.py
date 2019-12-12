import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *

from ui_login import Ui_MainWindow
import main

class login_window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(login_window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_login_fuc)

    def btn_login_fuc(self):
        account=self.lineEdit.text()
        password=self.lineEdit_2.text()
        if account== password:
            Ui.show()
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=login_window()
    Ui=main.Ui_Main()
    window.show()
    sys.exit(app.exec_())