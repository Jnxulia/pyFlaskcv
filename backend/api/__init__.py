from flask import Flask, abort, request,g
from flask_restful import  Api
from .info  import InfoResource
from .courses  import CoursesResource
from .experiences import ExperiencesResource
from .skills import SkillsResource
from .utils import json_response
import db
import pymongo

app = Flask(__name__)
api = Api(app)

@app.before_request
def before_request():
    g.db = db.connect_mongodb(app.config['DATABASE_HOST'],app.config['DATABASE_NAME'])
@app.route("/api")
def index():
    return json_response(list({"main" : "1"}) , status=204)
api.add_resource(InfoResource, '/api/info')
api.add_resource(CoursesResource, '/api/courses')
api.add_resource(ExperiencesResource, '/api/experiences')
api.add_resource(SkillsResource, '/api/skills')
