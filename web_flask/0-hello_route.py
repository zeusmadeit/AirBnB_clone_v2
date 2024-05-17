#!/usr/bin/python3
"""
This script starts a Flask web application:
The web application must be listening on 0.0.0.0, port 5000
Routes:
/: displays “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
