from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from cloud_management import get_wallet


class DashboardUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None):
        super(DashboardUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('dashboard.ui', self)  # Load the .ui file
        self.user_id = user_id

        self.edit_prof = self.findChild(QtWidgets.QPushButton, 'edit_prof')
        self.edit_prof.clicked.connect(self.editProfButtonPressed)
        self.user_id = user_id
        print(user_id)
        self.clouds = self.findChild(QtWidgets.QPushButton, 'bt_cloud')
        self.clouds.clicked.connect(self.cloudsButtonPressed)

        self.snapshot = self.findChild(QtWidgets.QPushButton, 'bt_snapshot')
        self.snapshot.clicked.connect(self.snapshotButtonPressed)

        self.ssh_keys = self.findChild(QtWidgets.QPushButton, 'bt_ssh')
        self.ssh_keys.clicked.connect(self.sshButtonPressed)

        self.make_ssh = self.findChild(QtWidgets.QPushButton, 'make_ssh')
        self.make_ssh.clicked.connect(self.makeSSHButtonPressed)

        self.ticket = self.findChild(QtWidgets.QPushButton, 'bt_tickets')
        self.ticket.clicked.connect(self.ticketsButtonPressed)

        self.increase_wallet = self.findChild(QtWidgets.QPushButton, 'inc_wallet')
        self.increase_wallet.clicked.connect(self.increaseButtonPressed)

        self.exit = self.findChild(QtWidgets.QPushButton, 'bt_exit')
        self.exit.clicked.connect(self.exitButtonPressed)

        self.username = self.findChild(QtWidgets.QTextBrowser, 'userName')
        self.notif = self.findChild(QtWidgets.QTextBrowser, 'notification')
        self.remain = self.findChild(QtWidgets.QTextBrowser, 'tb_masraf')
        self.wallet = get_wallet(user_id)[0]
        self.remain.setText(str(self.wallet['amount']))
        if self.wallet['amount'] <0:
            self.notif.setText("موجودی شما منفی می باشد. ")
        self.consume = self.findChild(QtWidgets.QTextBrowser, 'tb_remainConsume')

    # todo if editProf pressed then go to edit_prof.ui
    def editProfButtonPressed(self):
        from ui.edit_profile import EditProfileUi
        self.OtherWindow = EditProfileUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    # todo if clouds pressed then go to cloud_list.ui
    def cloudsButtonPressed(self):
        from ui.cloudList import CloudlistUi
        self.OtherWindow = CloudlistUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    # todo if snapshot pressed then go to show_image.ui
    def snapshotButtonPressed(self):
        from ui.show_snapshot import ShowSnapshotUi
        self.OtherWindow = ShowSnapshotUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    # todo if ssh pressed then go to ssh (create or show ?)
    def sshButtonPressed(self):
        from ui.show_ssh import ShowSSHUi
        self.OtherWindow = ShowSSHUi()
        self.OtherWindow.show()
        self.close()

    def makeSSHButtonPressed(self):
        from ui.ssh_make import MakeSSHUi
        self.OtherWindow = MakeSSHUi()
        self.OtherWindow.show()
        self.close()

    # todo if tickets pressed then go to make_ticket.ui
    def ticketsButtonPressed(self):
        from ui.ticket_list import TicketListUi
        self.OtherWindow = TicketListUi()
        self.OtherWindow.show()
        self.close()

    # todo if increase pressed then go to inc_wallet.ui
    def increaseButtonPressed(self):
        from ui.increase_wallet import IncreaseCreditUi
        self.OtherWindow = IncreaseCreditUi()
        self.OtherWindow.show()
        self.close()

    # todo not used :)
    def exitButtonPressed(self):
        from ui.loginui import LoginUi
        self.OtherWindow = LoginUi()
        self.OtherWindow.show()
        self.close()

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
    window = DashboardUi()  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()
