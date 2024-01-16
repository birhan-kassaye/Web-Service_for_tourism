#!/usr/bin/python3
""" Flask Application """
from views import app_views
from os import getenv
from flask import Flask, render_template, make_response, jsonify

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
from flask_cors import CORS

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

"""@app.teardown_appcontext
def close_db(error):
    Close Storage 
    storage.close()
"""

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """ Main Function """
    host = getenv('HOST')
    port = getenv('PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = 5001
    app.run(host=host, port=5001)
