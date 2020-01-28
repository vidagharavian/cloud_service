from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class AdminDashboardUi(QtWidgets.QMainWindow):
    def __init__(self,user_id:int=None):
        super(AdminDashboardUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('admin_dashboard.ui', self) # Load the .ui file
        self.user_id = user_id
        
        self.users = self.findChild(QtWidgets.QPushButton,'bt_users')
        self.users.clicked.connect(self.UsersButtonPressed)

        self.clouds = self.findChild(QtWidgets.QPushButton,'bt_cloud')
        self.clouds.clicked.connect(self.cloudsButtonPressed)
        
        self.ticket = self.findChild(QtWidgets.QPushButton,'bt_tickets') 
        self.ticket.clicked.connect(self.ticketsButtonPressed)

        self.exit = self.findChild(QtWidgets.QPushButton,'bt_exit')
        self.exit.clicked.connect(self.exitButtonPressed)

        self.username = self.findChild(QtWidgets.QTextBrowser,'userName')
        self.notif = self.findChild(QtWidgets.QTextBrowser,'notification')
        self.remain = self.findChild(QtWidgets.QTextBrowser,'tb_masraf')
        self.consume = self.findChild(QtWidgets.QTextBrowser,'tb_remainConsume')

    #todo if editProf pressed then go to users_list.ui and send ids
    def UsersButtonPressed(self):
        from ui.users_list import UsersListUi
        self.OtherWindow = UsersListUi(user_id = self.user_id)
        self.OtherWindow.show()
        self.close()
    
    #todo if clouds pressed then go to cloud_list.ui
    def cloudsButtonPressed(self):
        from ui.admin_cloud_list import AdminCloudListUi
        self.OtherWindow = AdminCloudListUi(user_id = self.user_id)
        self.OtherWindow.show()
        self.close()
    #todo if snapshot pressed then go to show_image.ui
    # def snapshotButtonPressed(self):
    #     from ui.snapshot_list_admin import AdminSnapshotListUi
    #     self.OtherWindow = AdminSnapshotListUi()
    #     self.OtherWindow.show()
    #     self.close()
    # #todo if ssh pressed then go to ssh (create or show ?)
    # def sshButtonPressed(self):
    #     from ui.show_ssh import ShowSSHUi
    #     self.OtherWindow = ShowSSHUi()
    #     self.OtherWindow.show()
    #     self.close()


    #todo if tickets pressed then go to make_ticket.ui
    def ticketsButtonPressed(self):
        from ui.ticket_list_admin import AdminTicketListUi
        self.OtherWindow = AdminTicketListUi(user_id = self.user_id)
        self.OtherWindow.show()
        self.close()

    #todo not used :)
    def exitButtonPressed(self):
        from ui.loginui import LoginUi
        self.OtherWindow = LoginUi()
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
    window = AdminDashboardUi() # Create an instance of our class
    window.show()
    sys.exit(app.exec_()) # Start the application

if __name__ == "__main__":
    main()
#todo maryam pak kon oon ssh va snapshoto be admin rabty nadare