from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class ManageDashboardUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(ManageDashboardUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('manag_dashboard.ui', self) # Load the .ui file

        self.users = self.findChild(QtWidgets.QPushButton,'users')
        self.users.clicked.connect(self.usersButtonPressed)

        self.clouds = self.findChild(QtWidgets.QPushButton,'clouds')
        self.clouds.clicked.connect(self.cloudsButtonPressed)

        self.ticket = self.findChild(QtWidgets.QPushButton,'tickets') 
        self.ticket.clicked.connect(self.ticketsButtonPressed)

        self.exit = self.findChild(QtWidgets.QPushButton,'bt_exit')
        self.exit.clicked.connect(self.exitButtonPressed)

        self.username = self.findChild(QtWidgets.QTextBrowser,'userName')
        self.notif = self.findChild(QtWidgets.QTextBrowser,'notification')
   
    #todo if clouds pressed then go to manag_cloud_list.ui and show all clouds
    def cloudsButtonPressed(self):
        print("fdms,ydbfdkfvdfc")
        from ui.manag_cloud_list import ManageCloudListUi
        self.OtherWindow = ManageCloudListUi()
        self.OtherWindow.show()
        self.close()

    #todo if users pressed then go to all_users.ui
    def usersButtonPressed(self):
        from ui.manag_users_list import ManageUserListUi
        self.OtherWindow = ManageUserListUi()
        self.OtherWindow.show()
        self.close()
    

    #todo go to ticket_list_status.ui
    def ticketsButtonPressed(self):
        from manag_ticket_list import ManageTicketListUi
        self.OtherWindow = ManageTicketListUi()
        self.OtherWindow.show()
        self.close()
    #todo not used :)
    def exitButtonPressed(self):
        from loginui import LoginUi
        self.OtherWindow = LoginUi()
        self.OtherWindow.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv) #Create an instance of QtWidgets.QApplication
    window = ManageDashboardUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()