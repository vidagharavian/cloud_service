import datetime
import time

from asn1crypto._ffi import null
from cryptography.hazmat.backends.openssl import rsa

from models import Model

UserTable = "Customer"
CustomerInfo = "customerinfo"
Cloud = 'Cloud'
SnapShot = 'Snapshot'
UserCloud = 'UserCloud'
SSH = 'SSH'
OsVersion = 'OsVersion'
SSHINFO = 'SSHInfo'
Ticket = 'Ticket'


def get_user_clouds(user_id: int) -> dict:
    return Model.select_query(model_name=Cloud,
                              out_put_array=['id', 'host_name', 'status', 'ip', 'date_created', 'cost_per_day'],
                              condition=f'where user_id={user_id}')


<<<<<<< HEAD
def create_cloud(os_version_id: int, user_id: int, host_name: str, cpu_amount, disk_amount: float,            ram_amount: float,band_width: float, core_amount: int):
    cost_per_day = calculate_price(core=core_amount, cpu=cpu_amount, storage=disk_amount, bandwidth=band_width,ram=ram_amount)
=======
def create_cloud(os_version_id: int, user_id: int, host_name: str, cpu_amount, disk_amount: float, ram_amount: float,
                 band_width: float, core_amount: int):
    cost_per_day = calculate_price(core=core_amount, cpu=cpu_amount, storage=disk_amount, bandwidth=band_width,
                                   ram=ram_amount)
>>>>>>> 91058be1a342e6a0842666b41145a31705e85d60
    Model.insert_query(model_name=Cloud,
                       input_array={'user_id': user_id, 'host_name': host_name, 'cpu_amount': cpu_amount,
                                    'disk_amount': disk_amount, 'ram_amount': ram_amount, 'band_width': band_width,
                                    'os_version_id': os_version_id, 'core_amount': core_amount,
                                    'cost_per_day': cost_per_day})


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
                           input_array={'name': name, 'user_id': user_id, 'key': public_key,
                                        'cloud_id': cloud_id})
    else:
        Model.insert_query(model_name=SSH,
                           input_array={'name': name, 'user_id': user_id, 'key': public_key})


def get_user_ssh(user_id):
    return Model.select_query(model_name=SSHINFO, out_put_array=['id', 'name', 'public_key', 'cloud_name', 'cloud_id'],
                              condition=f'where user_id={user_id}', is_view=True)


def get_snapshots(user_id):
    return Model.select_query(model_name=SnapShot,
                              condition=f'where cloud in (select id from public."Cloud" where user_id = {user_id})')


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
    Model.insert_query(model_name='Transaction', input_array={'amount': amount, 'wallet_id': wallet_id})


def get_wallet(user_id):
    clouds = get_user_clouds(user_id=user_id)
    if len(clouds) == 0:
        return Model.select_query(model_name='Wallet', condition=f'where user_id={user_id}')
    else:
        wallet = Model.select_query(model_name='Wallet', condition=f'where user_id={user_id}')
        wallet_id = int(wallet[0]['id'])
        transactions = Model.select_query(model_name='Transaction', condition=f'where wallet_id={wallet_id}')
        if len(transactions) == 0:
            amount = 0
            for cloud in clouds:
                amount = amount + cloud['cost_per_day']
            do_transaction(-amount, wallet_id)
            return wallet
        now = datetime.date.today()
        if now > transactions[len(transactions) - 1]['date_created']:
            amount = 0
            for cloud in clouds:
                amount = amount + cloud['cost_per_day']
            do_transaction(-amount, wallet_id)
            time.sleep(0.25)
            return wallet
        return wallet


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


def calculate_price(core, cpu, ram, storage, bandwidth):
    return core * cpu * 5000 + ram * 4000 + storage * 2000 + bandwidth * 1000


def edit_profile(first_name, last_name, email, national_num, user_id: int, password=None):
    from athentication import hash_password
    if password is not None:
        hashed_password = hash_password(password)
        Model.update_query(model_name=UserTable, input_array={'name': first_name, 'f_name': last_name, 'email': email,
                                                              'hashd_password': hashed_password,
                                                              'national_num': national_num},
                           condition=f'where id={user_id}')
    else:
        Model.update_query(model_name=UserTable, input_array={'name': first_name, 'f_name': last_name, 'email': email,
                                                              'national_num': national_num},
                           condition=f'where id={user_id}')


def update_cloud(os_version_id: int, user_id: int, host_name: str, cpu_amount, disk_amount: float, ram_amount: float,
                 band_width: float, core_amount: int, status: int, cloud_id):
    cost_per_day = calculate_price(core=core_amount, cpu=cpu_amount, storage=disk_amount, bandwidth=band_width,
                                   ram=ram_amount)
    Model.update_query(model_name=Cloud,
                       input_array={'user_id': user_id, 'host_name': host_name, 'cpu_amount': cpu_amount,
                                    'disk_amount': disk_amount, 'ram_amount': ram_amount, 'band_width': band_width,
                                    'os_version_id': os_version_id, 'core_amount': core_amount,
                                    'cost_per_day': cost_per_day, 'status': status}, condition=f'where id = {cloud_id}')


def get_public_private_key():
    from cryptography.hazmat.primitives import serialization as crypto_serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.backends import default_backend as crypto_default_backend
    key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=2048
    )
    private_key = key.private_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PrivateFormat.PKCS8,
        crypto_serialization.NoEncryption())
    public_key = key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )
    return {
        'private_key': private_key.decode("utf-8"),
        'public_key': public_key.decode("utf-8")
    }


def delete_snapshot(snap_shot_id: int):
    Model.delete_query(model_name=SnapShot, condition=f'where id= {snap_shot_id}')


def delete_ssh(ssh_id):
    Model.delete_query(model_name=SSH, condition=f'where id={ssh_id}')


def get_ssh(ssh_id):
    Model.select_query(model_name=SSH, condition=f'where id={ssh_id}')


def get_tickets(user_id: int):
    return Model.select_query(model_name='getticketinfo',
                              condition=f'where cloud_id in (select id from public."Cloud" where user_id = {user_id})')


def create_ticket(title, body, cloud_id):
    Model.insert_query(model_name=Ticket, input_array={'title': title, 'body': body, 'cloud_id': cloud_id})


def delete_ticket(ticket_id):
    Model.delete_query(model_name=Ticket,condition=f"where id = {ticket_id}")