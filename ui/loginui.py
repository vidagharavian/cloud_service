from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys
from athentication import sign_in

user = None


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('login.ui', self)  # Load the .ui file

        self.loginButton = self.findChild(QtWidgets.QPushButton, 'login')  # Find the button
        self.loginButton.clicked.connect(self.loginButtonPressed)  # Remember to pass the definition/method, not the return value!

        self.signinButton = self.findChild(QtWidgets.QPushButton, 'signin')  # Find the button
        self.signinButton.clicked.connect(self.signinButtonPressed)  # Remember to pass the definition/method, not the return value!
        self.username = self.findChild(QtWidgets.QTextEdit, 'te_username')  # Find the textEdit
        self.password = self.findChild(QtWidgets.QTextEdit, 'te_password')  # Find the textEdit

        self.show()  # Show the GUI

    def loginButtonPressed(self):
        global user
        # This is executed when the button is pressed
        print('loginButtonPressed')
        user = sign_in(self.username.toPlainText(), self.password.toPlainText())



    def signinButtonPressed(self):
        # This is executed when the button is pressed
        print('signinButtonPressed')


app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
window = Ui()  # Create an instance of our class
app.exec_()  # Start the application
