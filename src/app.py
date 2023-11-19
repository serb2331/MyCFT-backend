import flask
from views import view_users, view_consumption
from db import db_firestore, db_trackers, db_userdata

app = flask.Flask("__name__")

app.register_blueprint(view_users.users)


database = db_firestore.initialize_database()

def get_database():
    return database