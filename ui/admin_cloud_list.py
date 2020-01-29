from PyQt5 import QtWidgets, uic
import sys

from PyQt5.QtWidgets import QTableWidgetItem

from admin import get_clouds
from cloud_management import Cloud
from models import Model

cloud_list = {'Cloud id': 'cloud_id', 'Cloud name': 'host_name', 'Firstname': 'first_name', 'Cloud status': 'status',
              'Date': 'date_created', 'User id': 'user_id', 'CPU': 'cpu_amount', 'CORE': 'core_amount',
              'DISK': 'disk_amount', 'RAM': 'ram_amount', 'cost per day': 'cost_per_day', 'Lastname': 'last_name'}


class AdminCloudListUi(QtWidgets.QMainWindow):
    def __init__(self, user_id: int = None, is_manager=False):
        super(AdminCloudListUi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('admin_cloud_list.ui', self)  # Load the .ui file
        self.user_id = user_id
        self.is_manager = is_manager
        self.back = self.findChild(QtWidgets.QPushButton, 'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.editCloud = self.findChild(QtWidgets.QPushButton, 'edit')
        self.editCloud.clicked.connect(self.editButtonPressed)

        self.deleteCloud = self.findChild(QtWidgets.QPushButton, 'delete_2')
        self.deleteCloud.clicked.connect(self.deleteButtonPressed)

        self.cloudlist = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.cloudlist.setColumnHidden(0, True)  # column 0 is cloud id
        self.create_table()
        if is_manager:
            self.editCloud.setVisible(False)
            self.deleteCloud.setVisible(False)

    # todo: no need for user_id
    def create_table(self):
        clouds = get_clouds()
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

    # todo if press edit button go to create_cloud.ui
    def editButtonPressed(self):
        # pass ids to the other page
        from ui.create_cloud import CreateCloudUi
        row = self.cloudlist.currentItem().row()
        self.OtherWindow = CreateCloudUi(cloud_id=self.cloudlist.item(row, 0).text(), user_id=self.user_id
                                         , is_admin=True)
        self.OtherWindow.show()
        self.close()

    # todo if press back button back to dashboard.ui
    def backButtonPressed(self):
        from ui.admin_dashboard import AdminDashboardUi
        self.OtherWindow = AdminDashboardUi(user_id=self.user_id,is_manager=self.is_manager)
        self.OtherWindow.show()
        self.close()

    # todo if press delete then delete selected cloud and update table
    def deleteButtonPressed(self):
        row = self.cloudlist.currentItem().row()
        Model.delete_query(model_name=Cloud, condition=f'where id={self.cloudlist.item(row, 0).text()}')
        self.create_table()

    def get_value(object):
        if isinstance(object, QtWidgets.QComboBox):
            value = object.itemData(object.currentIndex())
        if isinstance(object, QtWidgets.QTextEdit):
            value = object.toPlainText()
        if isinstance(object, QtWidgets.QTextBrowser):
            value = object.toPlainText()
        if isinstance(object, QtWidgets.QLabel):
            value = object.text()
        if isinstance(object, QtWidgets.QSpinBox):
            value = object.value()
        if isinstance(object, QtWidgets.QDoubleSpinBox):
            value = object.value()
        return value


def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = AdminCloudListUi(user_id=1)  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()
