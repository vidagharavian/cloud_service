from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('cloud_list.ui', self) # Load the .ui file
        
        self.cloud_widget = self.findChild(QtWidgets.QTableWidget,'te_fname')
        
        self.back = self.findChild(QtWidgets.QPushButton,'pb_back')
        self.newCloud = self.findChild(QtWidgets.QPushButton,'pb_newCloud')

        self.show()

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application