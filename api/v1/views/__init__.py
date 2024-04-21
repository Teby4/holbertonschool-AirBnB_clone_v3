#!/usr/bin/python3

from flask import Blueprint

app_views = Blueprint(name='app_vieimport_name=ws', import_name=__name__, url_prefix='/api/v1')
from api.v1.views.index import *