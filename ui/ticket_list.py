from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class TicketListUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(TicketListUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ticket_list.ui', self) # Load the .ui file
        
        self.back = self.findChild(QtWidgets.QPushButton,'pb_back')
        self.back.clicked.connect(self.backButtonPressed)

        self.newTicket = self.findChild(QtWidgets.QPushButton,'pb_newTicket')
        self.newTicket.clicked.connect(self.newTicketButtonPressed)

        self.ticketlist = self.findChild(QtWidgets.QTableWidget,'tableWidget')       
        self.ticketlist.setColumnHidden( 5 ,True) #column 5 is message_id
        self.ticketlist.setColumnHidden( 6 ,True) #column 6 is response_id

    #todo if press back button back to dashboard.ui
    def backButtonPressed(self):
        from dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()

    #todo if press newTicket button go to create_ticket.ui and send ids
    def newTicketButtonPressed(self):
        from create_ticket import CreateTicketUi
        self.OtherWindow = CreateTicketUi()
        self.OtherWindow.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = TicketListUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()