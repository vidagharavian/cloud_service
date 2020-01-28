from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class ManageCloudListUi(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None):
        super(ManageCloudListUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('manag_cloud_list.ui', self) # Load the .ui file
        
        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.cloudlist = self.findChild(QtWidgets.QTableWidget,'tableWidget')       
        #self.cloudlist.setColumnHidden(1 ,True) #column 1 is user id
        #self.cloudlist.setColumnHidden( 0 ,True) #column 0 is cloud id


    #todo if press back button back to manag_dashboard.ui
    def backButtonPressed(self):
        from ui.manag_dashboard import ManageDashboardUi
        self.OtherWindow = ManageDashboardUi()
        self.OtherWindow.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = ManageCloudListUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()
