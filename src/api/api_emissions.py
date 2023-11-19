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
        print(tracker["emissions"])
        if ((Units.calcDateDay(tracker["start_date"]) >= start_date) and (Units.calcDateDay(tracker["start_date"]) <= end_date) and 
            (Units.calcDateDay(tracker["end_date"]) >= start_date) and (Units.calcDateDay(tracker["end_date"]) <= end_date)):
            total_emissions += tracker["emissions"]
        elif ((Units.calcDateDay(tracker["start_date"]) >= start_date) and (Units.calcDateDay(tracker["start_date"]) <= end_date)):
            total_emissions += tracker["emissions"] * (end_date - Units.calcDateDay(tracker["start_date"])) / (Units.calcDateDay(tracker["end_date"]) - Units.calcDateDay(tracker["start_date"]))
        elif ((Units.calcDateDay(tracker["end_date"]) >= start_date) and (Units.calcDateDay(tracker["end_date"]) <= end_date)):
            total_emissions += tracker["emissions"] * (Units.calcDateDay(tracker["end_date"]) - start_date) / (Units.calcDateDay(tracker["end_date"]) - Units.calcDateDay(tracker["start_date"]))
    return str(total_emissions)