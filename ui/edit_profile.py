from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from cloud_management import edit_profile
from models import Model


class EditProfileUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None, is_admin: bool = False):
        super(EditProfileUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('edit_profile.ui', self)  # Load the .ui file
        self.user_id = user_id
        self.is_admin = is_admin
        
        self.first_name = self.findChild(QtWidgets.QTextEdit, 'te_fname')
        self.last_name = self.findChild(QtWidgets.QTextEdit, 'te_lname')
        self.email = self.findChild(QtWidgets.QTextEdit, 'te_email')
        self.password = self.findChild(QtWidgets.QTextEdit, 'te_password')
        self.national_num = self.findChild(QtWidgets.QTextEdit, 'te_national')
        user = Model.select_query(model_name='Customer', condition=f'where id={user_id}')[0]
        self.first_name.setText(user['name'])
        self.last_name.setText(user['f_name'])
        self.email.setText(user['email'])
        self.national_num.setText(str(user['national_num']))
        self.back = self.findChild(QtWidgets.QPushButton, 'back')
        self.back.clicked.connect(self.backButtonPressed)
        self.edit = self.findChild(QtWidgets.QPushButton, 'edit')
        self.edit.clicked.connect(self.editButtonPressed)

    # todo if press back button back to login page
    def backButtonPressed(self):
        # from admin_dashboard import AdminDashboardUi
        if self.is_admin:
            from ui.admin_dashboard import AdminDashboardUi
            self.OtherWindow = AdminDashboardUi(user_id=self.user_id)
            self.OtherWindow.show()
            self.close()
        else:
            from ui.dashboard import DashboardUi
            self.OtherWindow = DashboardUi(user_id=self.user_id)
            self.OtherWindow.show()
            self.close()

    # todo if press edit button go to dashboard page and update profile
    def editButtonPressed(self):
        # first update profile then go to dashboard
        # from admin_dashboard import AdminDashboardUi
        edit_profile(self.first_name.toPlainText(), self.last_name.toPlainText(), self.email.toPlainText(),
                     int(self.national_num.toPlainText()), self.user_id, self.password.toPlainText())

        if self.is_admin:
            from ui.admin_dashboard import AdminDashboardUi
            self.OtherWindow = AdminDashboardUi(user_id=self.user_id)
            self.OtherWindow.show()
            self.close()
        else:
            from ui.dashboard import DashboardUi
            self.OtherWindow = DashboardUi(user_id=self.user_id)
            self.OtherWindow.show()
            self.close()

    def get_value(object):
        if isinstance(object,QtWidgets.QComboBox):
            value = object.itemData(object.currentIndex())
        if isinstance( object,QtWidgets.QTextEdit):
            value = object.toPlainText()
        if isinstance(object,QtWidgets.QTextBrowser):
            value = object.toPlainText()
        if isinstance(object,QtWidgets.QLabel):
            value = object.text()
        if isinstance(object,QtWidgets.QSpinBox):
            value = object.value()
        if isinstance (object,QtWidgets.QDoubleSpinBox):
            value = object.value()
        return value

def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = EditProfileUi()  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()
