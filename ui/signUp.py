from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from athentication import sign_up


class SignUpUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignUpUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('signup.ui', self) # Load the .ui file
        
        self.first_name = self.findChild(QtWidgets.QTextEdit,'te_fname')
        self.last_name = self.findChild(QtWidgets.QTextEdit,'te_lname')
        self.email = self.findChild(QtWidgets.QTextEdit,'te_email')
        self.password = self.findChild(QtWidgets.QTextEdit,'te_password')
        self.national_num = self.findChild(QtWidgets.QTextEdit,'te_national')
        
        self.back = self.findChild(QtWidgets.QPushButton,'pb_back')
        self.back.clicked.connect(self.backButtonPressed)

        self.signup = self.findChild(QtWidgets.QPushButton,'pb_signup')
        self.signup.clicked.connect(self.signupButtonPressed)

        self.show()

    #todo if press back button back to login page
    def backButtonPressed(self):
        pass

    #todo if press signup button go to dashboard page
    def signupButtonPressed(self):
        sign_up(self.first_name.toPlainText(),self.last_name.toPlainText(),self.national_num.toPlainText(),self.email.toPlainText(),self.password.toPlainText())

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = SignUpUi() # Create an instance of our class
app.exec_() # Start the application