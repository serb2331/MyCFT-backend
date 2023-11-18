import json
import flask
from classes.user.user import User
from flask import request

users = flask.Blueprint('views/users', __name__, url_prefix = '/users')

@users.route('/<string:id>', methods = ['POST'])
def post_user(id: str):
    userJson = flask.request.get_json()
    userObj = User(id, userJson['username'], userJson['email'], None, None)        
    #return "<p>" + str(userObj.getId()) + " " + str(userObj.getEmail()) + " " + str(userObj.getUsername()) + "<\p>"
    # de postat

@users.route('/<string:id>', methods = ['GET'])
def get_user(id: str):
    returnValues={
        "id": id ,
        "username": ,
        "email": ,
        "fuelType": ,
        "fuelEfficiency":
    }
    return json.dumps(returnValues)

@users.route('/<string:id>', methods = ['UPDATE'])
def update_user(id: str, fuelType: str, fuelEfficiency: float):
    pass
    #de facut update
