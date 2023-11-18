import json

def db_user_get(db, id: str):
    user = db.collection("Users").document(id)
    user_data = user.get()
    if user_data.exists:
        return json.dumps(user_data.to_dict())
    else:
        return "ERROR"
    

def db_user_set(db, id: str, user_data):
    user = db.collection("Users").document(id)
    print(user_data)
    user.set(user_data)
