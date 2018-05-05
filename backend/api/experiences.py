from flask_restful import Resource
from flask import g , request
from .utils import json_response
from bson.json_util import dumps

class ExperiencesResource(Resource):
    def get(self):
        print (request.args)
        cursor = g.db.experiences.find({},{'_id':0})

        return json_response(dumps(cursor))
