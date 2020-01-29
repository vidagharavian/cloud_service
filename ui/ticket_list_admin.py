from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from PyQt5.QtWidgets import QTableWidgetItem

from cloud_management import get_tickets

admin_ticket_list = {'title': 'ticket_title', 'message': 'ticket_body', 'response': 'response_body',
                     'date created': 'date_created', 'message_id': 'ticket_id',
                     'response_id': 'response_id','message status':'status'}  # todo we have "message status" column in list


class AdminTicketListUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None,is_manager=False):
        super(AdminTicketListUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('ticket_list_admin.ui', self)  # Load the .ui file
        self.user_id = user_id
        self.is_manager=is_manager
        self.back = self.findChild(QtWidgets.QPushButton, 'pb_back')
        self.back.clicked.connect(self.backButtonPressed)

        self.ignore = self.findChild(QtWidgets.QPushButton, 'ignore')
        self.ignore.clicked.connect(self.ignoreButtonPressed)

        self.response = self.findChild(QtWidgets.QPushButton, 'response')
        self.response.clicked.connect(self.responseButtonPressed)

        self.ticketlist = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.ticketlist.setColumnHidden(5, True)  # column 5 is message_id
        self.ticketlist.setColumnHidden(6, True)  # column 6 is response_id
        self.set_table()
    # todo if press ignore button just remove from this list table not from db table and set status 'ignore'
    def ignoreButtonPressed(self):
        row = self.ticketlist.currentItem().row()
        self.ticketlist.item(row, 5).text()
    def set_table(self):
        tickets = get_tickets()
        self.ticketlist.setRowCount(len(tickets))
        count = 0
        for ticket in tickets:
            for key, value in ticket.items():
                headercount = self.ticketlist.columnCount()
                m = key
                for x in range(0, headercount, 1):
                    headertext = self.ticketlist.horizontalHeaderItem(x).text()
                    if m == admin_ticket_list[headertext]:
                        self.tableWidget.setItem(count, x, QTableWidgetItem(str(value)))
            count += 1

    def backButtonPressed(self):
        from ui.admin_dashboard import AdminDashboardUi
        self.OtherWindow = AdminDashboardUi(user_id=self.user_id,is_manager=self.is_manager)
        self.OtherWindow.show()
        self.close()

    # todo if press newTicket button go to response_ticket.ui
    def responseButtonPressed(self):
        from ui.response_ticket import ResponseTicketUi
        row = self.ticketlist.currentItem().row()
        self.OtherWindow = ResponseTicketUi(user_id=self.user_id,ticket_id=self.ticketlist.item(row, 5).text())
        self.OtherWindow.show()
        self.close()

        pass
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
    window = AdminTicketListUi()  # Create an instance of our class
    window.show()
    app.exec_()  # Start the application


if __name__ == "__main__":
    main()
# todo maryam in message va responso pak kon
