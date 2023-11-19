from db import db_trackers
import app

database = app.get_database() 

def post_tracker(user_id: str, tracker_data):
    db_trackers.db_tracker_add(database, user_id, tracker_data)

def get_tracker(user_id: str, tracker_id: str):
    db_trackers.db_tracker_get(database, user_id, tracker_id)

def put_tracker(user_id: str, tracker_id: str, tracker_data):
    db_trackers.db_tracker_set(database, user_id, tracker_id, tracker_data)

def delete_tracker(user_id: str, tracker_id: str):
    db_trackers.db_tracker_delete(user_id, tracker_id)