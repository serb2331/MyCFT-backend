import flask
from api import api_emissions

emissions = flask.Blueprint('views/emissions', __name__, url_prefix = '/emissions')

@emissions.route('/<string:user_id>/<string:start_date>/<string:end_date>', methods = ['GET'])
def calculate_emissions_time_interval(user_id: str, start_date: str, end_date: str):
    return api_emissions.calculate_emissions_time_interval(user_id, start_date, end_date)
