from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class CreateTicketUi(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None):
        super(CreateTicketUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('create_ticket.ui', self) # Load the .ui file
        self.user_id = user_id

        self.selected_cloud = self.findChild(QtWidgets.QTextEdit,'cloud_list')
        self.title = self.findChild(QtWidgets.QTextEdit,'title')
        self.message = self.findChild(QtWidgets.QTextEdit,'message')
        
        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.send = self.findChild(QtWidgets.QPushButton,'send')
        self.send.clicked.connect(self.sendButtonPressed)

        
    #todo if press back button back to dashboard.ui and pass ids
    def backButtonPressed(self):
        from dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()

    #todo if press send button go to dashboard page and save it in ticket table
    def sendButtonPressed(self):
        #first save ticket then go to dashboard
        from dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()
def main():
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = CreateTicketUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application
