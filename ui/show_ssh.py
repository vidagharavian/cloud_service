from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from PyQt5.QtWidgets import QTableWidgetItem

from cloud_management import get_user_ssh, delete_ssh

sshlist = {'Name': 'name', 'Public Key': 'public_key', 'Cloud': 'cloud_name', 'id': 'id', 'Action': 'cloud_id'}


class ShowSSHUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None):
        super(ShowSSHUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('show_ssh.ui', self)  # Load the .ui file
        self.user_id = user_id
        self.back = self.findChild(QtWidgets.QPushButton, 'bt_back')
        self.back.clicked.connect(self.backButtonPressed)

        self.delete = self.findChild(QtWidgets.QPushButton, 'delete_2')
        self.delete.clicked.connect(self.deleteButtonPressed)
        # todo maryam action titlesh pak nashode
        self.ssh_list = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.ssh_list.setColumnHidden(3, True)
        self.ssh_list.setColumnHidden(4, True)  # column 5 is id
        self.create_table()

    def create_table(self):
        sshs = get_user_ssh(user_id=self.user_id)
        self.ssh_list.setRowCount(len(sshs))
        count = 0
        for ssh in sshs:
            for key, value in ssh.items():
                headercount = self.ssh_list.columnCount()
                m = key
                for x in range(0, headercount, 1):
                    headertext = self.ssh_list.horizontalHeaderItem(x).text()
                    if m == sshlist[headertext]:
                        self.tableWidget.setItem(count, x, QTableWidgetItem(str(value)))
            count += 1

    def update_buttonPressed(self):
        row = self.ssh_list.currentItem().row()
        from ui.ssh_make import MakeSSHUi
        self.OtherWindow = MakeSSHUi(user_id=self.user_id,ssh_id=int(self.ssh_list.item(row, 4).text()))
        self.OtherWindow.show()
        self.close()
    def deleteButtonPressed(self):
        row = self.ssh_list.currentItem().row()
        delete_ssh(int(self.ssh_list.item(row, 4).text()))
        self.create_table()

    # todo if press back button back to dashboard
    def backButtonPressed(self):
        # if id=admin ->show all SSHs
        # from admin_dashboard import AdminDashboardUi
        # self.OtherWindow = AdminDashboardUi()
        # self.OtherWindow.show()
        # self.close()

        # if id=customer -> show just SSHs of customer
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    # todo if press one row go to edit_ssh.ui page
    def rowButtonPressed(self):
        pass

    def get_value(object):
        if isinstance(object, QtWidgets.QComboBox):
            value = object.itemData(object.currentIndex())
        if isinstance(object, QtWidgets.QTextEdit):
            value = object.toPlainText()
        if isinstance(object, QtWidgets.QTextBrowser):
            value = object.toPlainText()
        if isinstance(object, QtWidgets.QLabel):
            value = object.text()
        if isinstance(object, QtWidgets.QSpinBox):
            value = object.value()
        if isinstance(object, QtWidgets.QDoubleSpinBox):
            value = object.value()
        return value


def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = ShowSSHUi(19)  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()
# todo maryam oon id ro hide kon actiono bardar
# todo maryam safeyehaye  manage ro pak kon kolan
