# Import
import flask
from flask import request


# Initialize the app
app = flask.Flask(__name__)

# Create an index route
@app.route("/", methods=["GET"])
def predict():
    return flask.render_template("index.html")


@app.route("/detect", methods=["GET"])
def detect():
    return flask.render_template("detect.html")


# Start the server
if __name__ == "__main__":
    app.run(debug=True)
    # For public web serving:
    # app.run(host='0.0.0.0')
    app.run()
