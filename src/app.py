import flask
from flask_cors import CORS, cross_origin
from views import view_emissions, view_users, view_trackers

app = flask.Flask("__name__")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"


app.register_blueprint(view_users.users)
app.register_blueprint(view_trackers.trackers)
app.register_blueprint(view_emissions.emissions)