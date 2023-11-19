from db import db_trackers

def db_user_get(db, user_id: str):
    user = db.collection("UserData").document(user_id)
    user_data = user.get()
    if user_data.exists:
        return user_data.to_dict()
    else:
        return "User not in database"
    

def db_user_set(db, user_id: str, user_data):
    user = db.collection("UserData").document(user_id)
    if not user.get().exists:
        return "User not in database"
    
    user.set(user_data)
    return "valid"


def db_user_add(db, user_id: str, user_data):
    user = db.collection("UserData").document(user_id)
    if user.get().exists:
        return "User with that id already exists"
    
    user.set(user_data)
    db_trackers.db_user_init(db, user_id)
    return "valid"


def db_user_delete(db, user_id: str):
    user = db.collection("UserData").document(user_id)
    if not user.get().exists:
        return "User not in database"
    
    db.collection("UserData").document(user_id).delete()
    db_trackers.db_user_delete(db, user_id)
    return "valid"