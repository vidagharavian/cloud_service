from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from cloud_management import get_oses, get_os_versions, get_cloud, get_os_version, get_os


class CreateCloudUi(QtWidgets.QMainWindow):
    def __init__(self, cloud_id: int = None , user_id:int=None):
        super(CreateCloudUi, self).__init__()  # Call the inherited classes __init__ method
        self.default_os_id=0
        uic.loadUi('create_cloud.ui', self)  # Load the .ui file
        self.cloud_id = cloud_id
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

    # todo if press caclulate button calculate total cost and show it in total_cost QTextBrowser
    def set_defaults(self):
        if self.cloud_id is None:
            self.os_type.addItem('--')
        else:
            cloud = get_cloud(int(self.cloud_id))
            cloud = cloud[0]
            os_version = get_os_version(int(cloud['os_version_id']))[0]
            self.default_os_id=os_version['os_id']
            self.os_type.addItem(os_version['name'], [str(os_version['os_id'])])
            self.cpu.setValue(cloud['cpu_amount'])
            self.core.setValue(cloud['core_amount'])
            self.disk.setValue(cloud['disk_amount'])
            self.ram.setValue(cloud['ram_amount'])
            self.cpu.setValue(cloud['cpu_amount'])

    def add_os_type(self):

        for os_type in get_oses():
            if os_type['id'] !=self.default_os_id:
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
        pass

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
        from ui.dashboard import DashboardUi
        self.OtherWindow = DashboardUi()
        self.OtherWindow.show()
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = CreateCloudUi()  # Create an instance of our class
    window.show()
    sys.exit(app.exec_())  # Start the application


if __name__ == "__main__":
    main()
#todo maryam oon cloud numbero bardar