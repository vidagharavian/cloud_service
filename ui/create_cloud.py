from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('create_cloud.ui', self) # Load the .ui file
        
        self.os_type = self.findChild(QtWidgets.QComboBox,'os_type')
        self.os_ver = self.findChild(QtWidgets.QComboBox,'os_ver')

        self.cpu = self.findChild(QtWidgets.QSpinBox,'cpu')
        self.ram = self.findChild(QtWidgets.QSpinBox,'ram')
        self.core = self.findChild(QtWidgets.QSpinBox,'core')
        self.disk = self.findChild(QtWidgets.QSpinBox,'disk')
        self.bandwidth = self.findChild(QtWidgets.QDoubleSpinBox,'bandwidth')

        self.cloud_name = self.findChild(QtWidgets.QTextEdit,'cloud_name')
        self.cloud_num = self.findChild(QtWidgets.QSpinBox,'cloud_num')

        self.total_cost =self.findChild(QtWidgets.QTextBrowser,'cost')

        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.createCloud = self.findChild(QtWidgets.QPushButton,'create')


        self.show()

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application