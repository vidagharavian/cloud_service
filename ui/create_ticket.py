from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from cloud_management import get_user_clouds, create_ticket


class CreateTicketUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None):
        super(CreateTicketUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('create_ticket.ui', self)  # Load the .ui file
        self.user_id = user_id

        self.selected_cloud = self.findChild(QtWidgets.QComboBox, 'cloud_list')
        self.title = self.findChild(QtWidgets.QTextEdit, 'title')
        self.message = self.findChild(QtWidgets.QTextEdit, 'message')

        self.back = self.findChild(QtWidgets.QPushButton, 'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.send = self.findChild(QtWidgets.QPushButton, 'send')
        self.send.clicked.connect(self.sendButtonPressed)
        self.set_clouds()

    def set_clouds(self):

        self.selected_cloud.addItem('--')

        for cloud in get_user_clouds(user_id=self.user_id):
            self.selected_cloud.addItem(cloud['host_name'], [str(cloud['id'])])

    # todo if press back button back to dashboard.ui and pass ids
    def backButtonPressed(self):
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    # todo if press send button go to dashboard page and save it in ticket table
    def sendButtonPressed(self):
        # first save ticket then go to dashboard
        cloud_id = self.selected_cloud.itemData(self.selected_cloud.currentIndex())[0]
        create_ticket(self.get_value(self.title), self.get_value(self.message), cloud_id)
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    def get_value(self, object):
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
    window = CreateTicketUi(19)  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()
