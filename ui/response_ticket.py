from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class ResponseTicketUi(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None):
        super(ResponseTicketUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('response_ticket.ui', self) # Load the .ui file
        
        self.title = self.findChild(QtWidgets.QTextBrowser,'title')
        self.message = self.findChild(QtWidgets.QTextBrowser,'message')
        self.reply = self.findChild(QtWidgets.QTextEdit,'reply')

        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.reply = self.findChild(QtWidgets.QPushButton,'reply')
        self.reply.clicked.connect(self.replyButtonPressed)

        
    #todo if press back button back to dashboard.ui(or ticket_list.ui)
    def backButtonPressed(self):
        from admin_dashboard import AdminDashboardUi
        self.OtherWindow = AdminDashboardUi()
        self.OtherWindow.show()
        self.close()

    #todo if press send button go to dashboard page and save it in ticket table and set 'pasokh dade shod'
    def replyButtonPressed(self):
        #save response and back to dashboard
        from admin_dashboard import AdminDashboardUi
        self.OtherWindow = AdminDashboardUi()
        self.OtherWindow.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = ResponseTicketUi() # Create an instance of our class
    window.show()
    app.exec_() # Start the application

if __name__ == "__main__":
    main()