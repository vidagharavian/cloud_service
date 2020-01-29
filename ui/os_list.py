from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys


class OSList(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None):
        super(OSList, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('os_list.ui', self) # Load the .ui file
        self.user_id = user_id

        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.new_os = self.findChild(QtWidgets.QPushButton,'new_os')
        self.new_os.clicked.connect(self.newOSButtonPressed)

        self.edit_os = self.findChild(QtWidgets.QPushButton,'edit_os')
        self.edit_os.clicked.connect(self.editOSButtonPressed)

    #todo if press back button back to dashboard
    def backButtonPressed(self):
        from admin_dashboard import AdminDashboardUi
        self.OtherWindow = AdminDashboardUi(user_id = self.user_id)
        self.OtherWindow.show()
        self.close()
    #todo if press submit button go to dashboard and save public_key and name for the cloud
    def newOSButtonPressed(self):
        #first add this os then go to dashboard
        from os_create import CreateOS
        self.OtherWindow = CreateOS(user_id = self.user_id)
        self.OtherWindow.show()
        self.close()

    def editOSButtonPressed(self):
        #todo update os
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
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = OSList() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()