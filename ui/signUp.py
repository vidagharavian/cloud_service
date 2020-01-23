from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('signup.ui', self) # Load the .ui file
        
        self.first_name = self.findChild(QtWidgets.QTextEdit,'te_fname')
        self.last_name = self.findChild(QtWidgets.QTextEdit,'te_lname')
        self.email = self.findChild(QtWidgets.QTextEdit,'te_email')
        self.password = self.findChild(QtWidgets.QTextEdit,'te_password')
        self.national_num = self.findChild(QtWidgets.QTextEdit,'te_national')
        
        self.back = self.findChild(QtWidgets.QPushButton,'pb_back')
        self.signup = self.findChild(QtWidgets.QPushButton,'pb_signup')
        
        self.show()
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application