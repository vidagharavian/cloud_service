from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

cloud_list_manager = {'User id': 'user_id','Cloud id': 'cloud_id', 'Cloud name': 'host_name', 'First name':                 'first_name', 'Cloud status': 'status',
              'CPU': 'cpu_amount', 'CORE': 'core_amount',
              'DISK': 'disk_amount', 'RAM': 'ram_amount', 'cost per day': 'Cost_per_day','New Column':'last_name','Date': 'date_created'}

class ManageCloudListUi(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None):
        super(ManageCloudListUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('manag_cloud_list.ui', self) # Load the .ui file
        self.user_id = user_id

        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.cloudlist = self.findChild(QtWidgets.QTableWidget,'tableWidget')       
        #self.cloudlist.setColumnHidden(1 ,True) #column 1 is user id
        #self.cloudlist.setColumnHidden( 0 ,True) #column 0 is cloud id


    #todo if press back button back to manag_dashboard.ui
    def backButtonPressed(self):
        from ui.manag_dashboard import ManageDashboardUi
        self.OtherWindow = ManageDashboardUi(user_id = self.user_id)
        self.OtherWindow.show()
        self.close()

    def get_value(object):
        if isinstance(object,QtWidgets.QComboBox):
            value = object.itemData(object.currentIndex())
        if isinstance( object,QtWidgets.QTextEdit):
            value = object.toPlainText()
        if isinstance(object,QtWidgets.QTextBrowser):
            value = object.toPlainText()
        if isinstance(object,QtWidgets.QLabel):
            value = object.text()
        if isinstance(object,QtWidgets.QSpinBox):
            value = object.value()
        if isinstance (object,QtWidgets.QDoubleSpinBox):
            value = object.value()
        return value

def main():
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = ManageCloudListUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()
