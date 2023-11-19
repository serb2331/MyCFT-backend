import flask
from views import view_users
from db import db_firestore, db_trackers, db_userauth

app = flask.Flask("__name__")

app.register_blueprint(view_users.users)


database = db_firestore.initialize_database()

print(db_trackers.db_user_delete(database, "empty"))

