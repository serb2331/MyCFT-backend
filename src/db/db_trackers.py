
empty_user_data = {'TrackerNumber': 0}

def db_tracker_get_all(db, user_id: str):
    user_trackers = db.collection("UserTrackers").document(user_id)
    return_array = []
    for tracker in user_trackers.collection("Trackers").stream():
        return_array.append(tracker.to_dict())
    return return_array

def db_tracker_get(db, user_id: str, tracker_id: str):
    user_trackers = db.collection("UserTrackers").document(user_id)
    tracker_data = user_trackers.collection("Trackers").document(tracker_id).get()
    if tracker_data.exists:
        return tracker_data.to_dict()
    else:
        return "ERROR"


def db_tracker_set(db, user_id: str, tracker_id: str,  tracker_data):
    user_trackers = db.collection("UserTrackers").document(user_id)
    tracker = user_trackers.collection("Trackers").document(tracker_id)
    tracker.set(tracker_data)


def db_tracker_add(db, user_id: str, tracker_data: str):
    user_trackers = db.collection("UserTrackers").document(user_id)
    tracker_number = user_trackers.get().to_dict()["TrackerNumber"]
    user_trackers.update({"TrackerNumber": tracker_number + 1})
    user_trackers.collection("Trackers").document(str(tracker_number)).set(tracker_data)


def db_tracker_delete(db, user_id: str, tracker_id: str):
    user_trackers = db.collection("UserTrackers").document(user_id)
    user_trackers.collection("Trackers").document(tracker_id).delete()
    tracker_number = user_trackers.get().to_dict()["TrackerNumber"]
    user_trackers.update({"TrackerNumber": tracker_number - 1})
    
    for index in range(tracker_number - 1):
        tracker = user_trackers.collection("Trackers").document(str(index))
        if not tracker.get().exists:
            tracker_data = user_trackers.collection("Trackers").document(str(index + 1)).get()
            user_trackers.collection("Trackers").document(str(index + 1)).detele()
            user_trackers.collection("Trackers").document(str(index)).set(tracker_data)


def db_user_init(db, user_id: str):
    db.collection("UserTrackers").document(user_id).set(empty_user_data)
    db.collection("UserTrackers").document(user_id).collection("Trackers").document("temp").set({"temp": "temp"})
    db.collection("UserTrackers").document(user_id).collection("Trackers").document("temp").delete()


def db_user_delete(db, user_id: str):
    user_tracker = db.collection("UserTrackers").document(user_id)
    for index in range(user_tracker.get().to_dict()["TrackerNumber"]):
        user_tracker.collection("Trackers").document(str(index)).delete()
    
    db.collection("UserTrackers").document(user_id).delete()
    


def db_user_get(db, user_id: str):
    return db.collection("UserTrackers").document(user_id).get().to_dict()