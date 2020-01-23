from typing import List

from psycopg2._psycopg import AsIs

from data_base_connection import cur, conn


class Model:
    @staticmethod
    def get_attribute(model_name: str, schema: str = 'public'):
        get_model_attribute_query = "SELECT *  FROM information_schema.columns WHERE table_schema = %s AND table_name   = %s;"
        cur.execute(get_model_attribute_query, (schema, model_name))
        rows = cur.fetchall()
        attributes = {}
        for row in rows:
            attributes[row[3]] = row[4]
        return attributes

    @classmethod
    def select_query(cls, model_name: str = None, schema_name: str = 'public',
                     out_put_array: List[str] = None, condition=None):

        if model_name is not None:
            query = 'select * from %s."%s"'
            if condition is not None:
                query = query + condition
            cur.execute(query, (AsIs(schema_name), AsIs(model_name)))
            rows = cur.fetchall()
            if out_put_array is not None:
                attributes = cls.get_attribute(model_name, schema_name)
                get_list = {}
                for out_put in out_put_array:
                    try:
                        value = attributes[out_put]
                        get_list[out_put] = value
                    except KeyError:
                        pass
                executed_outputs = []
                for row in rows:
                    executed_output = {}
                    for key, value in get_list.items():
                        executed_output[key] = row[int(value) - 1]
                    executed_outputs.append(executed_output)
                return executed_outputs

    @classmethod
    def insert_query(cls, model_name: str = None, schema_name: str = 'public',
                     input_array: dict = None):
        if model_name is not None:
            query = 'insert into %s."%s" ('
            values = list()
            attributes = cls.get_attribute(model_name=model_name)
            inn = 0
            for key, value in input_array.items():
                if key in attributes.keys():
                    if inn == 0:
                        inn = 1
                    else:
                        query = query + ','
                    query = query + key
                    values.append(value)

            values = tuple(values)
            query = query + ') values' + str(values)
            cur.execute(query, (AsIs(schema_name), AsIs(model_name)))
            conn.commit()

    @classmethod
    def update_query(cls, model_name: str, input_array: dict, schema_name: str = 'public',
                     condition=None):
        if model_name is not None:
            query = 'update %s."%s" set '
            attributes = cls.get_attribute(model_name=model_name)
            inn = 0
            for key, value in input_array.items():
                if key in attributes.keys():
                    if inn == 0:
                        inn = 1
                    else:
                        query = query + ','
                    query = query + key + ' = ' + "'%s'" % (value,)

            if condition is not None:
                query = query + condition
            cur.execute(query, (AsIs(schema_name), AsIs(model_name)))
            conn.commit()
    @classmethod
    def delete_query(cls,model_name:str,condition:str,schema_name: str = 'public'):
        if model_name is not None:
            query='delete from %s."%s"'+condition
            cur.execute(query,(AsIs(schema_name),AsIs(model_name)))
            conn.commit()


# rows = Model.select_query(model_name='Customer', out_put_array=['id', 'name', 'f_name'])
# for row in rows:
#     print(row)
# Model.insert_query(model_name='Customer', input_array={'name': "maryam",
#                                                        'f_name': "vaqei",
#                                                        'email': "mwaqei@gmail.com", 'hashd_password': "ppppp",'national_num':1234567})
# Model.update_query(model_name='Customer', input_array={
#     'name': 'Maryam'
# }, condition="where id = 8")
# Model.delete_query(model_name='Customer',condition='where id=8')