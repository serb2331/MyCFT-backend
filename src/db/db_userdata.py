from db import db_trackers

def db_user_get(db, user_id: str):
    user = db.collection("UserData").document(user_id)
    user_data = user.get()
    if user_data.exists:
        return user_data.to_dict()
    else:
        return "ERROR"
    

def db_user_set(db, user_id: str, user_data):
    db.collection("UserData").document(user_id).set(user_data)


def db_user_add(db, user_id: str, user_data):
    db.collection("UserData").document(user_id).set(user_data)
    db_trackers.db_user_init(db, user_id)


def db_user_delete(db, user_id: str):
    db.collection("UserData").document(user_id).delete()
    db_trackers.db_user_delete(db, user_id)