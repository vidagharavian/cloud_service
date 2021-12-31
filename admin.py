from psycopg2._psycopg import AsIs

from cloud_management import UserTable, UserCloud
from data_base_connection import cur, conn
from models import Model


def get_customers():
    return Model.select_query(model_name=UserTable)


def get_clouds():
    return Model.select_query(model_name=UserCloud, is_view=True,
                              out_put_array=['cloud_id', 'host_name', 'first_name', 'last_name', 'cost_per_day',
                                             'status', 'date_created'])


def response_ticket(ticket_id: int, body: str, user_id):
    Model.insert_query(model_name='TicketResponse',
                       input_array={'ticket_id': ticket_id, 'body': body, 'responser_id': user_id})


def create_os(name, base_RAM, base_CPU, base_CORE, base_cost, base_band_width,base_disk):
    query = 'insert into %s."%s" (name,"base_RAM","base_CPU","base_CORE",base_cost, base_band_width,base_disk)'+f" values ('{name}',{base_RAM},{base_CPU},{base_CORE},{base_cost},{base_band_width},{base_disk})"
    cur.execute(query, (AsIs('public'), AsIs('OS')))
    conn.commit()


def create_version(os_id, number):
    Model.insert_query(model_name='OsVersion', input_array={'os_id': os_id, 'number': number})


def update_os(os_id, name, base_RAM, base_CPU, base_CORE, base_cost, base_band_width):
    Model.update_query(model_name='OS',
                       input_array={'name': name, 'base_RAM': base_RAM, 'base_CORE': base_CORE, 'base_CPU': base_CPU,
                                    'base_cost': base_cost, 'base_band_width': base_band_width},
                       condition=f'where id={os_id}')


def ignore_tickets(ticket_id):
    Model.update_query(model_name='TicketStatus', input_array={'status': 'Ignored'},
                       condition=f'where ticket_id={ticket_id}')
