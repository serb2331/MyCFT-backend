import flask
from views.view_users import users

app = flask.Flask("__name__")

app.register_blueprint(users)

