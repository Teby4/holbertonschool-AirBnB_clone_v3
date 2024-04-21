#!/usr/bin/python3



from models import storage 
from api.v1.views import app_views
from flask import Response, jsonify, Flask
from os import getenv

app = Flask(import_name=__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close(error):
    storage.close()

@app.errorhandler(404)
def not_found_error(error):
    """Handler for 404 errors"""
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    return response


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)