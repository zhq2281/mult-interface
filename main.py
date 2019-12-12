import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ui_main import Ui_MainWindow

import ui_Dialog
import ui_Dialog2
import ui_form


class Ui_Main(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Ui_Main, self).__init__()
        self.setupUi(self)
        self.another = 5
        self.pushButton.clicked.connect(Dialog_win)
        self.pushButton_2.clicked.connect(Dialog_win2)

class Dialog_win(QtWidgets.QDialog,ui_Dialog.Ui_Dialog):
    def __init__(self):
        super(Dialog_win,self).__init__()
        self.setupUi(self)
        self.exec_()

class Dialog_win2(QtWidgets.QDialog,ui_Dialog2.Ui_Dialog):
    def __init__(self):
        super(Dialog_win2,self).__init__()
        self.setupUi(self)
        self.exec_()

class Form_win(QtWidgets.QWidget,ui_form.Ui_Form):
    def __init__(self):
        super(Form_win,self).__init__()
        self.setupUi(self)
        print('form')
        self.show()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Main()
    window.show()
    sys.exit(app.exec_())