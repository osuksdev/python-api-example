# project/__init__.py

from flask import Flask, jsonify
from flask_restx import Resource, Api

# create an instantiation of the Flask app
app = Flask(__name__)

api = Api(app)

# set environment config here
app.config.from_object('project.config.DevelopmentConfig')

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(Ping, '/ping')