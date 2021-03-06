from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from PyQt5.QtWidgets import QTableWidgetItem

from cloud_management import get_user_clouds, Cloud
from models import Model

cloud_list = {'Cloud id': 'id', 'Cloud name': 'host_name', 'IP address': 'ip', 'Cloud status': 'status',
              'Date': 'date_created', 'User id': 'user_id'}


class CloudlistUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None,is_admin:bool = False):
        super(CloudlistUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('cloud_list.ui', self)  # Load the .ui file
        self.user_id = user_id
        self.is_admin = is_admin

        print(user_id)
        self.back = self.findChild(QtWidgets.QPushButton, 'pb_back')
        self.back.clicked.connect(self.backButtonPressed)

        self.newCloud = self.findChild(QtWidgets.QPushButton, 'pb_newCloud')
        self.newCloud.clicked.connect(self.newCloudButtonPressed)

        self.editCloud = self.findChild(QtWidgets.QPushButton, 'edit')
        self.editCloud.clicked.connect(self.editButtonPressed)

        self.deleteCloud = self.findChild(QtWidgets.QPushButton, 'delete_2')
        self.deleteCloud.clicked.connect(self.deleteButtonPressed)

        self.cloudlist = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.cloudlist.setColumnHidden(4, True)  # column 4 is user id
        self.cloudlist.setColumnHidden(5, True)  # column 4 is cloud id
        self.create_table()

    # todo if press edit button go to create_cloud.ui
    def editButtonPressed(self):
        # set base amounts of each object
        # pass ids to the other page
        from ui.create_cloud import CreateCloudUi
        row = self.cloudlist.currentItem().row()
        self.OtherWindow = CreateCloudUi(cloud_id=self.cloudlist.item(row, 5).text(),user_id=self.user_id
                                        ,is_admin = self.is_admin)
        self.OtherWindow.show()
        self.close()

    # todo if press back button back to dashboard.ui
    def backButtonPressed(self):
        # pass ids to the other page
        if self.is_admin:
            from ui.admin_dashboard import AdminDashboardUi
            self.OtherWindow = AdminDashboardUi(user_id=self.user_id) #todo what parameter?
            self.OtherWindow.show()
            self.close()
        else:
            from ui.dashboard import DashboardUi
            self.OtherWindow = DashboardUi(user_id=self.user_id)
            self.OtherWindow.show()
            self.close()

    # todo if press newCloud button go to create_cloud.ui
    def newCloudButtonPressed(self):
        # pass ids to the other page
        from ui.create_cloud import CreateCloudUi
        self.OtherWindow = CreateCloudUi(user_id=self.user_id,is_admin = self.is_admin)
        self.OtherWindow.show()
        self.close()

    # todo if press delete button then delete it from list
    def deleteButtonPressed(self):
        # first delete cloud field and update table
        row = self.cloudlist.currentItem().row()
        Model.delete_query(model_name=Cloud, condition=f'where id={self.cloudlist.item(row, 5).text()}')
        self.create_table()

    def create_table(self):
        clouds = get_user_clouds(user_id=self.user_id)
        self.cloudlist.setRowCount(len(clouds))
        count = 0
        for cloud in clouds:
            for key, value in cloud.items():
                headercount = self.cloudlist.columnCount()
                m = key
                for x in range(0, headercount, 1):
                    headertext = self.cloudlist.horizontalHeaderItem(x).text()
                    if m == cloud_list[headertext]:
                        if m == 'status':
                            self.tableWidget.setItem(count, x, QTableWidgetItem('Active' if value else 'Inactive'))
                        else:
                            self.tableWidget.setItem(count, x, QTableWidgetItem(str(value)))
            count += 1
    
    def get_value(object):
        if isinstance(object,QtWidgets.QComboBox):
            value = object.itemData(object.currentIndex())
        if isinstance( object, QtWidgets.QTextEdit):
            value = object.toPlainText()
        if isinstance(object,QtWidgets.QTextBrowser):
            value = object.toPlainText()
        if isinstance(object, QtWidgets.QLabel):
            value = object.text()
        if isinstance(object, QtWidgets.QSpinBox):
            value = object.value()
        if isinstance (object,QtWidgets.QDoubleSpinBox):
            value = object.value()
        return value


    
def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = CloudlistUi(user_id=19)  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()
