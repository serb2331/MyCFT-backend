import flask
from views import view_users, view_consumption
from db import db_firestore, db_trackers, db_userauth

app = flask.Flask("__name__")

app.register_blueprint(view_users.users)


database = db_firestore.initialize_database()

db_trackers.db_tracker_add(database, "1", {"a": "a"})
db_userauth.db_user_delete(database, "1")

