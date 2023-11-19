from db import db_trackers, database

_database = database.get_database() 

def post_tracker(user_id: str, tracker_data):
    return db_trackers.db_tracker_add(_database, user_id, tracker_data)

def get_tracker(user_id: str, tracker_id: str):
    return db_trackers.db_tracker_get(_database, user_id, tracker_id)

def put_tracker(user_id: str, tracker_id: str, tracker_data):
    return db_trackers.db_tracker_set(_database, user_id, tracker_id, tracker_data)

def delete_tracker(user_id: str, tracker_id: str):
    return db_trackers.db_tracker_delete(_database, user_id, tracker_id)