from cloud_management import UserTable, UserCloud
from models import Model


def get_customers():
    return Model.select_query(model_name=UserTable)


def get_clouds():
    return Model.select_query(model_name=UserCloud, is_view=True,
                              out_put_array=['cloud_id', 'host_name', 'first_name', 'last_name', 'cost_per_day','status','date_created'])


def response_ticket(ticket_id: int, body: str, user_id):
    Model.insert_query(model_name='TicketResponse',
                       input_array={'ticket_id': ticket_id, 'body': body, 'responser_id': user_id})
