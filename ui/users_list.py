from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys


class UsersListUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(UsersListUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('users_list.ui', self)  # Load the .ui file

        self.back = self.findChild(QtWidgets.QPushButton, 'pb_back')
        self.back.clicked.connect(self.backButtonPressed)

        self.editUser = self.findChild(QtWidgets.QPushButton, 'edit')
        self.editUser.clicked.connect(self.EditButtonPressed)

        self.deleteUser = self.findChild(QtWidgets.QPushButton, 'delete_2')
        self.deleteUser.clicked.connect(self.deleteButtonPressed)

        self.userlist = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.userlist.setColumnHidden(5, True)  # column 4 is id

    # todo if press edit button then save edit of selected row
    def EditButtonPressed(self):
        # ->> no need to edit_profile.ui because it can edit in widgettable just save changes in table

        pass

    # todo if press back button back to admin_dashboard.ui
    def backButtonPressed(self):
        from ui.admin_dashboard import AdminDashboardUi
        self.OtherWindow = AdminDashboardUi()
        self.OtherWindow.show()
        self.close()

    # todo if press delete button then delete row and update table
    def deleteButtonPressed(self):
        pass


def insert_in_rows():
    pass


def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = UsersListUi()  # Create an instance of our class
    window.show()
    app.exec_()  # Start the application


if __name__ == "__main__":
    main()
# todo maryam passwordo pak kon
