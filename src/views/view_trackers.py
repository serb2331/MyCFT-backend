import json
import flask
from db import db_trackers

trackers = flask.Blueprint('views/trackers', __name__, url_prefix = '/trackers')

@trackers.route('/<string:id>', methods = ['POST'])
def post_tracker(user_id: str):
    trackerJson = flask.request.get_json()
    db_trackers.db_tracker_get()