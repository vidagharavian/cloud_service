from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class ResponseTicketUi(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None, ticket_id:int=None ):
        super(ResponseTicketUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('response_ticket.ui', self) # Load the .ui file
        self.user_id = user_id

        self.title = self.findChild(QtWidgets.QTextBrowser,'title')
        self.message = self.findChild(QtWidgets.QTextBrowser,'message')
        self.reply = self.findChild(QtWidgets.QTextEdit,'response')
from admin import response_ticket
from cloud_management import get_ticket


class ResponseTicketUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None, ticket_id: int = None,is_manager=False):
        super(ResponseTicketUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('response_ticket.ui', self)  # Load the .ui file
        self.user_id = user_id
        self.ticket_id = ticket_id
        self.is_manager=is_manager
        self.title = self.findChild(QtWidgets.QTextBrowser, 'title')
        self.message = self.findChild(QtWidgets.QTextBrowser, 'message')
        self.reply_m = self.findChild(QtWidgets.QTextEdit, 'response')
        ticket = get_ticket(self.ticket_id)[0]
        self.message.setText(ticket['ticket_body'])
        try:
            self.reply_m.setText(ticket['response_body'])
        except AttributeError:
            self.is_edit = False
        self.back = self.findChild(QtWidgets.QPushButton, 'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.reply = self.findChild(QtWidgets.QPushButton, 'reply')
        self.reply.clicked.connect(self.replyButtonPressed)

    # todo if press back button back to dashboard.ui(or ticket_list.ui)
    def backButtonPressed(self):
        from ui.ticket_list_admin import AdminTicketListUi
        self.OtherWindow = AdminTicketListUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    # todo if press send button go to dashboard page and save it in ticket table and set 'pasokh dade shod'
    def replyButtonPressed(self):
        #save response and back to dashboard
        from ui.ticket_list_admin import AdminTicketListUi
        self.OtherWindow = AdminTicketListUi(user_id = self.user_id)
        # save response and back to dashboard
        response_ticket(ticket_id=self.ticket_id, body=self.get_value(self.reply_m), user_id=self.user_id)
        from ui.admin_dashboard import AdminDashboardUi
        self.OtherWindow = AdminDashboardUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    @staticmethod
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
    window = ResponseTicketUi(1, 1)  # Create an instance of our class
    window.show()
    app.exec_()  # Start the application


if __name__ == "__main__":
    main()
