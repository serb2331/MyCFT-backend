from db import database, db_userdata

_database = database.get_database() 

def post_user(user_id: str, user_data):
    return db_userdata.db_user_add(_database, user_id, user_data)

def get_user(user_id: str):
    return db_userdata.db_user_get(_database, user_id)

def put_user(user_id: str, user_data):
    return db_userdata.db_user_set(_database, user_id, user_data)

def delete_user(user_id: str):
    return db_userdata.db_user_delete(_database, user_id)