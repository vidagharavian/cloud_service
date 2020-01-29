from cloud_management import UserTable, UserCloud
from models import Model


def get_customers():
    return Model.select_query(model_name=UserTable)


def get_clouds():
    return Model.select_query(model_name=UserCloud,is_view=True,out_put_array=['cloud_id','host_name','first_name','last_name','cost_per_day'])



def get_ticks(status: str = None):
    if status is None:
        pass
