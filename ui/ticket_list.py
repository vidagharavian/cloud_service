from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from PyQt5.QtWidgets import QTableWidgetItem

from cloud_management import get_tickets

ticket_list = {'title': 'ticket_title', 'message': 'ticket_body', 'response': 'response_body',
               'date created': 'date_created', 'message_id': 'ticket_id',
               'response_id': 'response_id','message status':'status'}


class TicketListUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None):
        super(TicketListUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('ticket_list.ui', self)  # Load the .ui file
        self.user_id = user_id
        self.back = self.findChild(QtWidgets.QPushButton, 'pb_back')
        self.back.clicked.connect(self.backButtonPressed)

        self.newTicket = self.findChild(QtWidgets.QPushButton, 'pb_newTicket')
        self.newTicket.clicked.connect(self.newTicketButtonPressed)

        self.ticketlist = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.ticketlist.setColumnHidden(5, True)  # column 5 is message_id
        self.ticketlist.setColumnHidden(6, True)  # column 6 is response_id
        self.set_table()
    # todo if press back button back to dashboard.ui
    def set_table(self):
        tickets = get_tickets(user_id=self.user_id)
        self.ticketlist.setRowCount(len(tickets))
        count = 0
        for ticket in tickets:
            for key, value in ticket.items():
                headercount = self.ticketlist.columnCount()
                m = key
                for x in range(0, headercount, 1):
                    headertext = self.ticketlist.horizontalHeaderItem(x).text()
                    if m == ticket_list[headertext]:
                        self.tableWidget.setItem(count, x, QTableWidgetItem(str(value)))
            count += 1

    def backButtonPressed(self):
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    # todo if press newTicket button go to create_ticket.ui and send ids
    def newTicketButtonPressed(self):
        from ui.create_ticket import CreateTicketUi
        self.OtherWindow = CreateTicketUi(user_id=self.user_id)
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
    window = TicketListUi(19)  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()
