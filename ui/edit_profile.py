from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys


class EditProfileUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None, is_admin: bool = False):
        super(EditProfileUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('edit_profile.ui', self)  # Load the .ui file
        self.user_id=user_id
        self.is_admin=is_admin
        self.first_name = self.findChild(QtWidgets.QTextEdit, 'te_fname')
        self.last_name = self.findChild(QtWidgets.QTextEdit, 'te_lname')
        self.email = self.findChild(QtWidgets.QTextEdit, 'te_email')
        self.password = self.findChild(QtWidgets.QTextEdit, 'te_password')
        self.national_num = self.findChild(QtWidgets.QTextEdit, 'te_national')

        self.back = self.findChild(QtWidgets.QPushButton, 'back')
        self.back.clicked.connect(self.backButtonPressed)
        self.edit = self.findChild(QtWidgets.QPushButton, 'edit')
        self.edit.clicked.connect(self.editButtonPressed)

    # todo if press back button back to login page
    def backButtonPressed(self):
        # from admin_dashboard import AdminDashboardUi
        from ui.dashboard import DashboardUi

        # if id= admin
        # self.OtherWindow = AdminDashboardUi()
        # self.OtherWindow.show()
        # self.close()

        # if id=costumer
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()

    # todo if press edit button go to dashboard page and update profile
    def editButtonPressed(self):
        # first update profile then go to dashboard
        # from admin_dashboard import AdminDashboardUi
        from ui.dashboard import DashboardUi
        # if id= admin
        # self.OtherWindow = AdminDashboardUi()
        # self.OtherWindow.show()
        # self.close()
        # if id=costumer

        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = EditProfileUi()  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()
