import json

def db_tracker_get(db, id: str):
    tracker = db.collection("Trackers").document(id)
    tracker_data = tracker.get()
    if tracker_data.exists:
        return json.dumps(tracker_data.to_dict())
    else:
        return "ERROR"
    

def db_tracker_set(db, id: str, tracker_data):
    tracker = db.collection("Trackers").document(id)
    tracker.set(tracker_data)
