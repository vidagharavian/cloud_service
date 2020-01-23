from data_base_connection import cur
from models import Model

UserTable = "Customer"
CustomerInfo = "customerinfo"


def get_user_clouds(user_id: int) -> dict:
    Model.select_query(model_name='Cloud', out_put_array=['host_name', 'status', 'ip', 'date_created'],
                       condition=f'where user_id={user_id}')


def create_cloud(os_version_id: int, user_id: int, host_name: str, cpu_amount, disk_amount: float, ram_amount: float,
                 band_width: float) -> dict:
    Model.insert_query(model_name='Cloud',input_array={'user_id':user_id,'host_name':host_name,'cpu_amount':cpu_amount,'disk_amount':disk_amount,'ram_amount':ram_amount,'band_width':band_width,'os_version_id':os_version_id})


def take_snapshot(cloud_id:int,os_version_id:int,cpu_amount,core_amount,disk_amount,ram_amount,band_width):
    Model.insert_query()
#todo: change os to os_version_id in snapshot


def create_ssh(name,key,user_id):
    pass


def get_user_ssh(user_id):
    pass


def get_snapshots(user_id):
    pass


def revert_snapshot(snapshot_id):
    pass


def get_oses():
    pass


def get_os_versions(os_id):
    pass


def do_transaction(amount,wallet_id):
    def update_wallet():
        pass


def get_user_wallet(user_id):
    pass

