from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class AdminTicketListUi(QtWidgets.QMainWindow):
    def __init__(self,user_id:int=None):
        super(AdminTicketListUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ticket_list_admin.ui', self) # Load the .ui file
        self.user_id = user_id

        self.back = self.findChild(QtWidgets.QPushButton,'pb_back')
        self.back.clicked.connect(self.backButtonPressed)

        self.ignore = self.findChild(QtWidgets.QPushButton,'ignore')
        self.ignore.clicked.connect(self.ignoreButtonPressed)

        self.response = self.findChild(QtWidgets.QPushButton,'response')
        self.response.clicked.connect(self.responseButtonPressed)

        self.ticketlist = self.findChild(QtWidgets.QTableWidget,'tableWidget')       
        self.ticketlist.setColumnHidden( 5 ,True) #column 5 is message_id
        self.ticketlist.setColumnHidden( 6 ,True) #column 6 is response_id

    #todo if press ignore button just remove from this list table not from db table and set status 'ignore'
    def ignoreButtonPressed(self):
        pass

    #todo if press back button back to dashboard.ui
    def backButtonPressed(self):
        pass

    #todo if press newTicket button go to response_ticket.ui
    def responseButtonPressed(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = AdminTicketListUi() # Create an instance of our class
    window.show()
    app.exec_() # Start the application

if __name__ == "__main__":
    main()
#todo maryam in message va responso pak kon