from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys
from athentication import sign_up


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('signup.ui', self)  # Load the .ui file

        self.first_name = self.findChild(QtWidgets.QTextEdit, 'te_fname')
        self.last_name = self.findChild(QtWidgets.QTextEdit, 'te_lname')
        self.email = self.findChild(QtWidgets.QTextEdit, 'te_email')
        self.password = self.findChild(QtWidgets.QTextEdit, 'te_password')
        self.national_num = self.findChild(QtWidgets.QTextEdit, 'te_national')

        self.back = self.findChild(QtWidgets.QPushButton, 'pb_back')
        self.signup = self.findChild(QtWidgets.QPushButton, 'pb_signup')

        self.signup.clicked.connect(self.signup_action)
        self.back.clicked.connect(self.back_action)
        self.show()

    def back_action(self):
        pass

    def signup_action(self):
        user = sign_up(first_name=self.first_name.toPlainText(), last_name=self.last_name.toPlainText(),
                       national_num=self.national_num.toPlainText(), email=self.email.toPlainText(),
                       password=self.password.toPlainText())
        print(user)


app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
window = Ui()  # Create an instance of our class
app.exec_()  # Start the application
