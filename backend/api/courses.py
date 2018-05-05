from flask_restful import Resource
from flask import g , request
from .utils import json_response
from bson.json_util import dumps

class CoursesResource(Resource):
    def get(self):
        print (request.args)
        cursor = g.db.courses.find({},{'_id':0})

        return json_response(dumps(cursor))
