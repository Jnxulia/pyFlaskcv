from flask_restful import Resource
from flask import g , request
from .utils import json_response
from bson.json_util import dumps

class SkillsResource(Resource):
    def get(self):
        cursor = g.db.skills.find({},{'_id':0})
        return json_response(dumps(cursor))
