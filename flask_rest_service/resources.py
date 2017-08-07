#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import request, abort
from flask_restful import Resource
from flask_restful import Resource, reqparse
from flask_rest_service import app, api, mongo
from bson.objectid import ObjectId

class GameList(Resource):
    def get(self):
        return [x for x in mongo.db.games.find()]


class Game(Resource):
    def get(self, game_id):
        return mongo.db.games.find_one_or_404({"_id": game_id})


class Root(Resource):
    def get(self):
        return {
            'status': 'OK',
            'mongo': "",
        }

api.add_resource(Root, '/')
api.add_resource(GameList, '/games/')
api.add_resource(Game, '/games/<ObjectId:game_id>')
