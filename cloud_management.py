from asn1crypto._ffi import null

from models import Model

UserTable = "Customer"
CustomerInfo = "customerinfo"
Cloud = 'Cloud'
SnapShot = 'Snapshot'
UserCloud = 'UserCloud'
SSH = 'SSH'
OsVersion = 'OsVersion'


def get_user_clouds(user_id: int) -> dict:
    return Model.select_query(model_name=Cloud, out_put_array=['id', 'host_name', 'status', 'ip', 'date_created'],
                              condition=f'where user_id={user_id}')


def create_cloud(os_version_id: int, user_id: int, host_name: str, cpu_amount, disk_amount: float, ram_amount: float,
                 band_width: float):
    Model.insert_query(model_name=Cloud,
                       input_array={'user_id': user_id, 'host_name': host_name, 'cpu_amount': cpu_amount,
                                    'disk_amount': disk_amount, 'ram_amount': ram_amount, 'band_width': band_width,
                                    'os_version_id': os_version_id})


def take_snapshot(cloud_id: int, name: str):
    cloud = Model.select_query(model_name='Cloud',
                               out_put_array=['os_version_id', 'cpu_amount', 'core_amount', 'disk_amount', 'ram_amount',
                                              'band_width'], condition=f'where id={cloud_id}')
    cloud = cloud[0]
    Model.insert_query(model_name=SnapShot,
                       input_array={'cloud': cloud_id, 'os_version_id': cloud['os_version_id'],
                                    'cpu_amount': cloud['cpu_amount'] if cloud['cpu_amount'] is not None else 0,
                                    'core_amount': cloud['core_amount'] if cloud['core_amount'] is not None else 0,
                                    'disk_amount': cloud['disk_amount'] if cloud['disk_amount'] is not None else 0,
                                    'ram_amount': cloud['ram_amount'],
                                    'band_width': cloud['band_width'], 'name': name})
    # todo create trigger


def create_ssh(name, user_id, public_key: str, cloud_id: int = None):
    if cloud_id is not None:
        Model.insert_query(model_name=SSH,
                           input_array={'name': name, 'user_id': user_id, 'key': public_key.decode("utf-8"),
                                        'cloud_id': cloud_id})
    else:
        Model.insert_query(model_name=SSH,
                           input_array={'name': name, 'user_id': user_id, 'key': public_key.decode("utf-8")})


def get_user_ssh(user_id):
    return Model.select_query(model_name=SSH, out_put_array=['name', 'id', 'cloud_id'],
                              condition=f'where user_id={user_id}')


def get_snapshots(user_id):
    return Model.select_query(model_name=SnapShot)


def revert_snapshot(snapshot_id):
    snapshot = Model.select_query(model_name=SnapShot, condition=f'where id ={snapshot_id}')
    snapshot = snapshot[0]
    Model.update_query(model_name=Cloud, condition=f"where id={snapshot['cloud']}",
                       input_array={'os_version_id': snapshot['os_version_id'],
                                    'cpu_amount': snapshot['cpu_amount'] if snapshot['cpu_amount'] is not None else 0,
                                    'core_amount': snapshot['core_amount'] if snapshot[
                                                                                  'core_amount'] is not None else 0,
                                    'disk_amount': snapshot['disk_amount'] if snapshot[
                                                                                  'disk_amount'] is not None else 0,
                                    'ram_amount': snapshot['ram_amount'],
                                    'band_width': snapshot['band_width']})


def get_oses():
    return Model.select_query(model_name='OS')


def get_os_versions(os_id):
    return Model.select_query(model_name=OsVersion, condition=f'where os_id={os_id}')


def do_transaction(amount, wallet_id):
    def update_wallet():
        pass


def get_user_wallet(user_id):
    pass


def get_cloud(cloud_id):
    return Model.select_query(model_name=Cloud, condition=f'where id={cloud_id}')


# create_cloud(os_version_id=1, user_id=2, host_name='mona', cpu_amount=3,disk_amount= 4.0, ram_amount=4.0, band_width=4.0)

# for user_ssh in get_user_ssh(user_id=2):
#     print(user_ssh)
# for user_cloud in get_user_clouds(2):
#     print(user_cloud)
# take_snapshot(2, 'hh')
# revert_snapshot(1)
def get_os_version(os_version: int):
    return Model.select_query(model_name='OsOsVersion', condition=f'where os_version_id={os_version}',
                              out_put_array=['os_id', 'os_version_id', 'number', 'name'], is_view=True)


def get_os(os_id):
    return Model.select_query(model_name='OS', condition=f'where id={os_id}')
