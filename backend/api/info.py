from flask_restful import Resource
from flask import g
from .utils import json_response
from bson.json_util import dumps

class InfoResource(Resource):
    def get(self):
        cursor = g.db.info.find({},{'_id':0})

        return json_response(dumps(cursor))
