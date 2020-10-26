import sys
import random
import string
import time
from gui import Ui_MainWindow
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator

class kinwriter(QMainWindow, Ui_MainWindow): 
    
    def __init__(self):

        super().__init__()

        self.setupUi(self)
        self.show()
        self.setFixedSize(248, 177)
        self.pushButton_generate.setEnabled(False)
        self.onlyInt = QIntValidator()
        self.lineEdit_length.setValidator(self.onlyInt)

    def setting(self):
        if self.checkBox_ascii.isChecked()==True and self.checkBox_digits.isChecked()==False and self.checkBox_punctuation.isChecked()==False:
            self.method = string.ascii_letters
        elif self.checkBox_ascii.isChecked()==False and self.checkBox_digits.isChecked()==True and self.checkBox_punctuation.isChecked()==False:
            self.method = string.digits
        elif self.checkBox_ascii.isChecked()==False and self.checkBox_digits.isChecked()==False and self.checkBox_punctuation.isChecked()==True:
            self.method = string.punctuation
        elif self.checkBox_ascii.isChecked()==True and self.checkBox_digits.isChecked()==True and self.checkBox_punctuation.isChecked()==False:
            self.method = string.ascii_letters + string.digits
        elif self.checkBox_ascii.isChecked()==False and self.checkBox_digits.isChecked()==True and self.checkBox_punctuation.isChecked()==True:
            self.method = string.digits + string.punctuation
        elif self.checkBox_ascii.isChecked()==True and self.checkBox_digits.isChecked()==False and self.checkBox_punctuation.isChecked()==True:
            self.method = string.ascii_letters + string.punctuation
        elif self.checkBox_ascii.isChecked()==True and self.checkBox_digits.isChecked()==True and self.checkBox_punctuation.isChecked()==True:
            self.method = string.ascii_letters + string.digits + string.punctuation
        else:
            pass
    
    def generate(self):
        self.history = open("history.txt", 'a')
        self.textBrowser_output.clear()
        self.length = self.lineEdit_length.text()
        self.pw = "".join([random.choice(self.method) for _ in range(int(self.length))])
        self.history.write(self.pw)
        self.history.write("\n", )
        self.history.close()
        self.textBrowser_output.append(self.pw)

    def on_text_changed(self):
        self.pushButton_generate.setEnabled(bool(self.lineEdit_length.text()) and bool(self.checkBox_ascii.isChecked()))

app = QApplication([])
sn = kinwriter()
QApplication.processEvents()
sys.exit(app.exec_())