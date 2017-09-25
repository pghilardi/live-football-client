#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps

MONGODB_URI = os.environ.get('MONGODB_URI')

if not MONGODB_URI:
    MONGODB_URI = "mongodb://localhost:27017/live-football";

app = Flask(__name__)

app.config['MONGO_URI'] = MONGODB_URI
mongo = PyMongo(app)

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj, ensure_ascii=False), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = { 'application/json; charset=utf-8': output_json, }

api = Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import flask_rest_service.resources
