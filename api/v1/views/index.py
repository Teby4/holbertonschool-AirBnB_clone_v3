#!/usr/bin/python3

from api.v1.views import app_views
from flask import Response, jsonify

@app_views.route(rule='/status')
def status():
    response = {'status': 'OK'}
    return jsonify(response)