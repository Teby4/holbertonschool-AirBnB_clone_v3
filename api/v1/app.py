#!/usr/bin/python3



from models import storage 
from api.v1.views import app_views
from flask import Flask
from os import getenv

app = Flask(import_name=__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close(error):
    storage.close()


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)