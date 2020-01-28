from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from admin import get_customers
from athentication import sign_in


class LoginUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('login.ui', self)  # Load the .ui file

        self.loginButton = self.findChild(QtWidgets.QPushButton, 'login')  # Find the button
        self.loginButton.clicked.connect(
            self.loginButtonPressed)  # Remember to pass the definition/method, not the return value!

        self.signupButton = self.findChild(QtWidgets.QPushButton, 'signin')  # Find the button
        self.signupButton.clicked.connect(
            self.signupButtonPressed)  # Remember to pass the definition/method, not the return value!
        self.email = self.findChild(QtWidgets.QTextEdit, 'te_username')  # Find the textEdit
        self.password = self.findChild(QtWidgets.QTextEdit, 'te_password')  # Find the textEdit

        self.show()  # Show the GUI

    # todo get email and password and ckeck it then login to dashboard
    def loginButtonPressed(self):
        # This is executed when the button is pressed
        print('loginButtonPressed')
        user =sign_in(self.email.toPlainText(), self.password.toPlainText())
        from ui.dashboard import DashboardUi
        if user is not None:
            self.OtherWindow = DashboardUi(user['customer_id'])
            self.OtherWindow.show()
            self.close()

    # todo if press signup button go to signup page
    def signupButtonPressed(self):
        from ui.signUp import SignUpUi
        self.OtherWindow = SignUpUi()
        self.OtherWindow.show()
        self.close()
        # This is executed when the button is pressed
        print('signiupButtonPressed')

    def get_value(object):
        if isinstance(object, QtGui.QtWidgets.QComboBox):
            value = object.itemData(object.currentIndex())
        if isinstance( object, QtGui.QtWidgets.QTextEdit):
            value = object.toPlainText()
        if isinstance(object,QtGui.QtWidgets.QTextBrowser):
            value = object.toPlainText()
        if isinstance(object, QtGui.QtWidgets.QLabel):
            value = object.text()
        if isinstance(object, QtGui.QtWidgets.QSpinBox):
            value = object.value()
        if isinstance (object,QtGui.QtWidgets.QDoubleSpinBox):
            value = object.value()
        return value

def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = LoginUi()  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()
