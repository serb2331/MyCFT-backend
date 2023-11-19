import json
import flask
from api import api_trackers

trackers = flask.Blueprint('views/trackers', __name__, url_prefix = '/trackers')

@trackers.route('/<string:user_id>', methods = ['POST'])
def post_tracker(user_id: str):
    tracker_data = flask.request.get_json()
    return api_trackers.post_tracker(user_id, tracker_data)

@trackers.route('/all/<string:user_id>', methods = ['GET'])
def get_all_tracker(user_id: str):
    return api_trackers.get_all_tracker(user_id)

@trackers.route('/<string:user_id>/<string:tracker_id>', methods = ['GET'])
def get_tracker(user_id: str, tracker_id: str):
    return api_trackers.get_tracker(user_id, tracker_id)
    
@trackers.route('/<string:user_id>/<string:tracker_id>', methods = ['PUT'])
def put_tracker(user_id: str, tracker_id: str):
    tracker_data = flask.request.get_json()
    return api_trackers.put_tracker(user_id, tracker_id, tracker_data)

    
@trackers.route('/<string:user_id>/<string:tracker_id>', methods = ['DELETE'])
def delete_tracker(user_id: str, tracker_id: str):
    return api_trackers.delete_tracker(user_id, tracker_id)