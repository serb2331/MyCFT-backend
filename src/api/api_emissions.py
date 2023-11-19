from db import db_trackers, database
from utils.units import Units

_database = database.get_database()

def calculate_emissions_time_interval(user_id: str, start_date_s: str, end_date_s: str):
    total_emissions = 0
    start_date = Units.calcDateDay(start_date_s)
    end_date = Units.calcDateDay(end_date_s)
    tracker_dict = db_trackers.db_tracker_get_all(_database, user_id)
    for tracker in tracker_dict:
        print(start_date, Units.calcDateDay(tracker["start_date"]))
        print(end_date, Units.calcDateDay(tracker["end_date"]))
        if (Units.calcDateDay(tracker["start_date"]) >= start_date) and (Units.calcDateDay(tracker["end_date"]) <= end_date):
            print("yess")
            total_emissions += tracker["emissions"]
    
    return str(total_emissions)