from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class ManageUserListUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(ManageUserListUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('manag_users_list.ui', self) # Load the .ui file
        
        self.back = self.findChild(QtWidgets.QPushButton,'pb_back')
        self.back.clicked.connect(self.backButtonPressed)

        self.seeSources = self.findChild(QtWidgets.QPushButton,'clouds')
        self.seeSources.clicked.connect(self.seeButtonPressed)

        self.userlist = self.findChild(QtWidgets.QTableWidget,'tableWidget')       
        self.userlist.setColumnHidden( 5 ,True) #column 4 is id
        


    #todo if press see button then save go to manag_cloud_list.ui and show list of that user sources
    def seeButtonPressed(self):
        #see clouds of selected user
        from manag_cloud_list import ManageCloudListUi
        self.OtherWindow = ManageCloudListUi()
        self.OtherWindow.show()
        self.close()

    #todo if press back button back to manag_dashboard.ui
    def backButtonPressed(self):
        from manag_dashboard import ManageDashboardUi
        self.OtherWindow = ManageDashboardUi()
        self.OtherWindow.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = ManageUserListUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()