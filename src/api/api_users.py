from db import db_userdata
import app

database = app.get_database() 

def post_user(user_id: str, user_data):
    db_userdata.db_user_add(database, user_id, user_data)

def get_user(user_id: str):
    db_userdata.db_user_get(database, user_id)

def put_user(user_id: str, user_data):
    db_userdata.db_user_set(database, user_id, user_data)

def delete_user(user_id: str):
    db_userdata.db_user_delete(user_id)