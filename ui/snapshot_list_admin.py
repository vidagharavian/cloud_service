from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

snapshot_list_admin = {'User id': 'user_id','Cloud id': 'cloud_id', 'Cloud name': 'host_name', 
                'Date creation':'date_created', 'Cloud status': 'status',
                'minimum CPU': 'cpu_amount', 'minimum core': 'core_amount',
                'minimum disk': 'disk_amount', ' minimum RAM': 'ram_amount', 'Bound width': 'band_width'}

class AdminSnapshotListUi(QtWidgets.QMainWindow):
    def __init__(self,user_id:int = None):
        super(AdminSnapshotListUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('snapshot_list_admin.ui', self) # Load the .ui file
        self.user_id = user_id

        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.revert = self.findChild(QtWidgets.QPushButton,'revert')
        self.revert.clicked.connect(self.revertButtonPressed)

        self.delete = self.findChild(QtWidgets.QPushButton,'delete_2')
        self.delete.clicked.connect(self.deleteButtonPressed)

        self.snapshot_table = self.findChild(QtWidgets.QPushButton,'tableWidget')
    
    #todo if press revert I don't know 
    def revertButtonPressed(self):
        pass

    #todo if press back button back to dashboard.ui
    def backButtonPressed(self):
        from admin_dashboard import AdminDashboardUi
        self.OtherWindow = AdminDashboardUi(user_id = self.user_id)
        self.OtherWindow.show()
        self.close()
   
   
    #todo if press delete button then delete ssh and update table
    def deleteButtonPressed(self):
        pass


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
    app = QtWidgets.QApplication(sys.argv) #Create an instance of QtWidgets.QApplication
    window = AdminSnapshotListUi() # Create an instance of our class
    window.show()
    app.exec_() # Start the application

if __name__ == "__main__":
    main()
#todo pak shavad