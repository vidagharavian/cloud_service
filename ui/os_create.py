from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from admin import create_os


class CreateOS(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None,os_id:int=None):
        super(CreateOS, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('os_create.ui', self) # Load the .ui file
        self.user_id = user_id
        self.os_id = os_id
        self.base_ram = self.findChild(QtWidgets.QSpinBox,'ram')
        self.base_cpu = self.findChild(QtWidgets.QSpinBox,'cpu')
        self.base_core = self.findChild(QtWidgets.QSpinBox,'core')
        self.base_bandwidth = self.findChild(QtWidgets.QSpinBox,'bandwidth')
        self.base_disk = self.findChild(QtWidgets.QSpinBox,'disk')

        self.cost = self.findChild(QtWidgets.QTextEdit,'cost')

        self.os_name = self.findChild(QtWidgets.QTextEdit,'os_name')

        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.add = self.findChild(QtWidgets.QPushButton,'add')
        self.add.clicked.connect(self.addButtonPressed)


    #todo if press back button back to dashboard
    def backButtonPressed(self):
        from ui.os_list import OSList
        self.OtherWindow = OSList(user_id = self.user_id)
        self.OtherWindow.show()
        self.close()
    #todo if press submit button go to dashboard and save public_key and name for the cloud
    def addButtonPressed(self):
        #first add this os version then go to dashboard
        create_os(self.get_value(self.os_name),self.get_value(self.base_ram),self.get_value(self.base_cpu),self.get_value(self.base_core),self.get_value(self.cost),self.get_value(self.base_bandwidth))
        from ui.os_list import OSList
        self.OtherWindow = OSList(user_id = self.user_id)
        self.OtherWindow.show()
        self.close()
    @staticmethod
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
    window = CreateOS() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()