from utils.units import Units
from db import db_userdata

empty_user_data = {'TrackerNumber': 0}

def db_tracker_get_all(db, user_id: str):
    user_trackers = db.collection("UserTrackers").document(user_id)
    if not user_trackers.get().exists:
        return "User not in database"
    return_array = []
    for tracker in user_trackers.collection("Trackers").stream():
        return_array.append(tracker.to_dict())
    return return_array


def db_tracker_get(db, user_id: str, tracker_id: str):
    user_trackers = db.collection("UserTrackers").document(user_id)
    if not user_trackers.get().exists:
        return "User not in database"
    tracker = user_trackers.collection("Trackers").document(tracker_id)
    
    if tracker.get().exists:
        return tracker.get().to_dict()
    else:
        return "User not in database"


def db_tracker_set(db, user_id: str, tracker_id: str,  tracker_data):
    user_trackers = db.collection("UserTrackers").document(user_id)
    if not user_trackers.get().exists:
        return "User not in database"
    tracker = user_trackers.collection("Trackers").document(tracker_id)
    if not tracker.get().exists:
        return "Tracker not in database"
    tracker.set(tracker_data)
    if tracker.get().to_dict()["tracker"] == "energy":
        tracker.update({"emissions": Units.powerToCarbon(int(tracker.get().to_dict()["value"]))})
    elif tracker.get().to_dict()["tracker"] == "water":
        tracker.update({"emissions": Units.waterToCarbon(int(tracker.get().to_dict()["value"]))})
    elif tracker.get().to_dict()["tracker"] == "fuel":
        tracker.update({"emissions": Units.fuelToCarbon(int(tracker.get().to_dict()["value"]), db_userdata.db_user_get(db, user_id)["fuel_type"], db_userdata.db_user_get(db, user_id)["fuel_consumption"])})
    return "valid"


def db_tracker_add(db, user_id: str, tracker_data: str):
    user_trackers = db.collection("UserTrackers").document(user_id)
    if not user_trackers.get().exists:
        return "User not in database"
    tracker_number = user_trackers.get().to_dict()["TrackerNumber"]
    user_trackers.update({"TrackerNumber": tracker_number + 1})
    tracker = user_trackers.collection("Trackers").document(str(tracker_number))
    tracker.set(tracker_data)
    
    if tracker.get().to_dict()["tracker"] == "energy":
        tracker.update({"emissions": Units.powerToCarbon(int(tracker.get().to_dict()["value"]))})
    elif tracker.get().to_dict()["tracker"] == "water":
        tracker.update({"emissions": Units.waterToCarbon(int(tracker.get().to_dict()["value"]))})
    elif tracker.get().to_dict()["tracker"] == "fuel":
        tracker.update({"emissions": Units.fuelToCarbon(int(tracker.get().to_dict()["value"]), db_userdata.db_user_get(db, user_id)["FuelType"], db_userdata.db_user_get(db, user_id)["FuelConsumption"])})
    return "valid"


def db_tracker_delete(db, user_id: str, tracker_id: str):
    user_trackers = db.collection("UserTrackers").document(user_id)
    if not user_trackers.get().exists:
        return "User not in database"
    tracker = user_trackers.collection("Trackers").document(tracker_id)
    if not tracker.get().exists:
        return "Tracker not in database"
    tracker.delete()
    tracker_number = user_trackers.get().to_dict()["TrackerNumber"]
    user_trackers.update({"TrackerNumber": tracker_number - 1})
    
    for index in range(tracker_number - 1):
        tracker = user_trackers.collection("Trackers").document(str(index))
        if not tracker.get().exists:
            tracker_data = user_trackers.collection("Trackers").document(str(index + 1)).get()
            user_trackers.collection("Trackers").document(str(index + 1)).delete()
            user_trackers.collection("Trackers").document(str(index)).set(tracker_data)
    
    return "valid"


def db_user_init(db, user_id: str):
    db.collection("UserTrackers").document(user_id).set(empty_user_data)
    db.collection("UserTrackers").document(user_id).collection("Trackers").document("temp").set({"temp": "temp"})
    db.collection("UserTrackers").document(user_id).collection("Trackers").document("temp").delete()
    return "valid"


def db_user_delete(db, user_id: str):
    user_trackers = db.collection("UserTrackers").document(user_id)
    if not user_trackers.get().exists:
        return "User not in database"
    for index in range(user_trackers.get().to_dict()["TrackerNumber"]):
        user_trackers.collection("Trackers").document(str(index)).delete()
    
    db.collection("UserTrackers").document(user_id).delete()
    return "valid"
    

def db_tracker_user_get(db, user_id: str):
    if not db.collection("UserTrackers").document(user_id).get().exists:
        return "User not in database"
    db.collection("UserTrackers").document(user_id).get().to_dict()
    return "valid"