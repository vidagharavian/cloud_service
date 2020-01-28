from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class IncreaseCreditUi(QtWidgets.QMainWindow):
    def __init__(self , user_id:int=None):
        super(IncreaseCreditUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('inc_wallet.ui', self) # Load the .ui file
        self.user_id = user_id

        self.transaction = self.findChild(QtWidgets.QPushButton,'transaction') 
        self.transaction.clicked.connect(self.transactionButtonPressed)

        self.back = self.findChild(QtWidgets.QPushButton,'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.credit = self.findChild(QtWidgets.QTextBrowser,'credit')

    #todo if editProf pressed then go to dashboard.ui
    def backButtonPressed(self):
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()

    #todo if transaction pressed then go to dashboard.ui and add transaction to transaction table
    def transactionButtonPressed(self):
        #increase wallet then go to dashboard
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()


    def get_value(object):
        if isinstance(object, QtGui.QtWidgets.QComboBox):
            value = object.itemData(object.currentIndex())
        if isinstance( object, QtGui.QtWidgets.QTextEdit):
            value = object.toPlainText()
        if isinstance(object,QtGui.QtWidgets.QTextBrowser):
            value = object.toPlainText()
        if isinstance(object, QtGui.QtWidgets.QLabel):
            value = object.text()
        if isinstance(object, QtGui.QtWidgets.QSpinBox):
            value = object.value()
        if isinstance (object,QtGui.QtWidgets.QDoubleSpinBox):
            value = object.value()
        return value

def main():
    app = QtWidgets.QApplication(sys.argv) #Create an instance of QtWidgets.QApplication
    window = IncreaseCreditUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()