import flask
from views import view_users, view_trackers, view_consumption

app = flask.Flask("__name__")

app.register_blueprint(view_users.users)
app.register_blueprint(view_trackers.trackers)
