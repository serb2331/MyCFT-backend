import json
import flask
from classes.user.user import User

users = flask.Blueprint('views/users', __name__, url_prefix = '/users')

@users.route('/<string:id>', methods = ['POST'])
def post_user(id: str):
    userJson = flask.request.get_json()
    userObj = User(userJson['id'], userJson['username'], userJson['email'])
    
    return "<p>" + str(userObj.getId()) + " " + str(userObj.getEmail()) + " " + str(userObj.getUsername()) + "<\p>"