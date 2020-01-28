from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from cloud_management import get_oses, get_os_versions, get_cloud, get_os_version, get_os, calculate_price, \
    create_cloud, update_cloud


class CreateCloudUi(QtWidgets.QMainWindow):
    def __init__(self, cloud_id: int = None, user_id: int = None):
        super(CreateCloudUi, self).__init__()  # Call the inherited classes __init__ method
        self.default_os_id = 0
        uic.loadUi('create_cloud.ui', self)  # Load the .ui file
        self.cloud_id = cloud_id
        self.user_id = user_id
        self.os_type = self.findChild(QtWidgets.QComboBox, 'os_type')
        self.layout = QtWidgets.QVBoxLayout(self)
        self.set_defaults()
        self.add_os_type()
        self.show()
        self.os_ver = self.findChild(QtWidgets.QComboBox, 'os_ver')

        self.cpu = self.findChild(QtWidgets.QSpinBox, 'cpu')
        self.ram = self.findChild(QtWidgets.QSpinBox, 'ram')
        self.core = self.findChild(QtWidgets.QSpinBox, 'core')
        self.disk = self.findChild(QtWidgets.QSpinBox, 'disk')
        self.bandwidth = self.findChild(QtWidgets.QDoubleSpinBox, 'bandwidth')

        self.cloud_name = self.findChild(QtWidgets.QTextEdit, 'cloud_name')
        self.cloud_num = self.findChild(QtWidgets.QSpinBox, 'cloud_num')

        self.total_cost = self.findChild(QtWidgets.QTextBrowser, 'cost')

        self.back = self.findChild(QtWidgets.QPushButton, 'back')
        self.back.clicked.connect(self.backButtonPressed)

        self.createCloud = self.findChild(QtWidgets.QPushButton, 'create')
        self.createCloud.clicked.connect(self.createButtonPressed)

        self.calculate_cost = self.findChild(QtWidgets.QPushButton, 'calculate')
        self.calculate_cost.clicked.connect(self.calculateButtonPressed)

        self.update_cloud = self.findChild(QtWidgets.QPushButton, 'update')
        self.update_cloud.clicked.connect(self.updateButtonPressed)

        self.status = self.findChild(QtWidgets.QComboBox, 'status')
        self.status_label = self.findChild(QtWidgets.QLabel, 'label_status')
        self.status.addItem("Active", [1])
        self.status.addItem("Inactive", [0])
        if cloud_id is None:
            self.update_cloud.setVisible(False)
            self.createCloud.setVisible(True)
            self.status.setVisible(False)
            self.status_label.setVisible(False)
        else:
            self.update_cloud.setVisible(True)
            self.createCloud.setVisible(False)
            self.status.setVisible(True)
            self.status_label.setVisible(True)
        self.status = self.findChild(QtWidgets.QComboBox, 'status')
        self.status.addItem("Active", [1])
        self.status.addItem("Inactive", [0])
        if cloud_id is None:
            self.update_cloud.setVisible(False)
            self.createCloud.setVisible(True)
            self.status.setVisible(False)
        else:
            self.update_cloud.setVisible(True)
            self.createCloud.setVisible(False)
            self.status.setVisible(True)

    # todo if press caclulate button calculate total cost and show it in total_cost QTextBrowser
    def set_defaults(self):
        if self.cloud_id is None:
            self.os_type.addItem('--')
        else:
            cloud = get_cloud(int(self.cloud_id))
            cloud = cloud[0]
            os_version = get_os_version(int(cloud['os_version_id']))[0]
            self.default_os_id = os_version['os_id']
            self.os_type.addItem(os_version['name'], [str(os_version['os_id'])])
            self.cpu.setValue(cloud['cpu_amount'] if cloud['cpu_amount'] is not None else 1)
            self.core.setValue(cloud['core_amount'] if cloud['core_amount'] is not None else 1)
            self.disk.setValue(cloud['disk_amount'])
            self.ram.setValue(cloud['ram_amount'])
            self.cpu.setValue(cloud['cpu_amount'])
            self.cost.setText(str(cloud['cost_per_day']))
            self.cloud_name.setText(cloud['host_name'])

    def add_os_type(self):

        for os_type in get_oses():
            if os_type['id'] != self.default_os_id:
                self.os_type.addItem(os_type['name'], [str(os_type['id'])])
        self.os_type.currentIndexChanged.connect(self.indexChanged)
        self.layout.addWidget(self.os_type)
        self.indexChanged(self.os_type.currentIndex())

    def indexChanged(self, index):
        self.layout.addWidget(self.os_ver)
        self.os_ver.clear()
        data = self.os_type.itemData(index)
        if data is not None:
            items = get_os_versions(int(data[0]))
            for item in items:
                self.os_ver.addItem(item['number'], [str(item['id'])])
            os = get_os(int(data[0]))[0]
            self.cpu.setMinimum(os['base_CPU'])
            self.core.setMinimum(os['base_CORE'])
            self.ram.setMinimum(os['base_RAM'])
            self.disk.setMinimum(os['base_disk'])
            self.bandwidth.setMinimum(os['base_band_width'])

    def calculateButtonPressed(self):
        # calculate cost and show it to customer
        self.cost.setText(str(calculate_price(self.core.value(), self.cpu.value(), self.ram.value(), self.disk.value(),
                                              self.bandwidth.value())))

    # todo first check cost<wallet and then update cloud and then go to cloud_list
    def updateButtonPressed(self):
        os_version = self.os_ver.itemData(self.os_ver.currentIndex())[0]
        status = self.status.itemData(self.status.currentIndex())[0]
        update_cloud(int(os_version), self.user_id, self.cloud_name.toPlainText(), self.cpu.value(), self.disk.value()
                     , self.ram.value(), self.bandwidth.value(),self.core.value(),status,self.cloud_id)
        from ui.cloudList import CloudlistUi
        self.OtherWindow = CloudlistUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()

    # todo if press back button back to dashboard.ui or admin_dashboard.ui
    def backButtonPressed(self):
        # pass parameters to dashboard
        # then go to dashboard

        # from admin_dashboard import AdminDashboardUi -> set defualt amount for each object
        # if id= admin
        # self.OtherWindow = AdminDashboardUi()
        # self.OtherWindow.show()
        # self.close()

        # if id=costumer if come from edit button -> set defualt amount for each object
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()

    # todo if press create button 1.check wallet>cost 2.add all attributes in clouds of user
    def createButtonPressed(self):
        # if create successfully then go to dashboard
        data = self.os_ver.itemData(self.os_ver.currentIndex())[0]
        create_cloud(int(data), self.user_id, self.cloud_name.toPlainText(), self.cpu.value(), self.disk.value()
                     , self.ram.value(), self.bandwidth.value())
        from ui.cloudList import CloudlistUi
        self.OtherWindow = CloudlistUi(user_id=self.user_id)
        self.OtherWindow.show()
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = CreateCloudUi()  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()
# todo maryam oon cloud numbero bardar
