import json
import flask
from flask import request
from api import api_users

users = flask.Blueprint('views/users', __name__, url_prefix = '/users')

@users.route('/<string:id>', methods = ['POST'])
def post_user(user_id: str):
    userJson = flask.request.get_json()
    api_users.post_user(user_id, userJson)

@users.route('/<string:id>', methods = ['GET'])
def get_user(user_id: str):
    returnValues = api_users.get_user(user_id)
    print(returnValues)
    print(json.dumps(returnValues))
    return json.dumps(returnValues)

@users.route('/<string:id>', methods = ['PUT'])
def put_user(user_id: str, fuelType: str, fuelEfficiency: float):
    userJson = flask.request.get_json()
    api_users.put_user(user_id, userJson)

@users.route('/<string:id>', methods = ['DELETE'])
def delete_user(user_id: str):
    api_users.delete_user(user_id)