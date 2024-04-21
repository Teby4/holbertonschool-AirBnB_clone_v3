#!/usr/bin/python3



from models import storage 
from api.v1.views import app_views
from flask import Flask
from os import getenv

app = Flask(import_name=__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close() -> None:
    storage.close()


if __name__ == '__main__':
    app.run(host=getenv(key="HBNB_API_HOST"), port=getenv(key="HBNB_API_PORT"), threaded=True)