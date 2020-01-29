from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class ManageTicketListUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(ManageTicketListUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('manag_ticket_list.ui', self) # Load the .ui file

        self.status = self.findChild(QtWidgets.QComboBox,'status')

        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.showTickets = self.findChild(QtWidgets.QPushButton,'bt_show')
        self.showTickets.clicked.connect(self.showButtonPressed)

        self.cloudlist = self.findChild(QtWidgets.QTableWidget,'tableWidget')       
        #self.cloudlist.setColumnHidden(1 ,True) #column 1 is user id
        #self.cloudlist.setColumnHidden( 0 ,True) #column 0 is cloud id

    #todo if press back button back to manag_dashboard.ui
    def backButtonPressed(self):
        from manag_dashboard import ManageDashboardUi
        self.OtherWindow = ManageDashboardUi()
        self.OtherWindow.show()
        self.close()

    #todo if press show button then show all tickets in selected status
    def showButtonPressed(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = ManageTicketListUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()