import flask
from views.view_users import users
from views.view_consumption import consumption

app = flask.Flask("__name__")

app.register_blueprint(users)
app.register_blueprint()


# if __name__ == "__main__":
#     app.run(debug=True)
