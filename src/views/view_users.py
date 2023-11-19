import json
import flask
from api import api_users

users = flask.Blueprint('views/users', __name__, url_prefix = '/users')

@users.route('/<string:user_id>', methods = ['POST'])
def post_user(user_id: str):
    user_data = flask.request.get_json()
    return api_users.post_user(user_id, user_data)

@users.route('/<string:user_id>', methods = ['GET'])
def get_user(user_id: str):
    return api_users.get_user(user_id)

@users.route('/<string:user_id>', methods = ['PUT'])
def put_user(user_id: str):
    user_data = flask.request.get_json()
    return api_users.put_user(user_id, user_data)

@users.route('/<string:user_id>', methods = ['DELETE'])
def delete_user(user_id: str):
    return api_users.delete_user(user_id)