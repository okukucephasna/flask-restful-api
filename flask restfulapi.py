# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Employee(Resource):# corresponds to the GET request.
# this function is called whenever there
# is a GET request for this resource
 def get(self):
  return jsonify({'message': 'hello world GET'})
# Corresponds to POST request
 def post(self):
  return jsonify({'message': 'hello world POST'})
 def delete(self):
  return jsonify({'message': 'hello world DELETE'})
 def put(self):
  return jsonify({'message': 'hello world UPDATE'})
# adding the defined resource/Class along with its corresponding url
api.add_resource(Employee, '/employees')
# driver function
if __name__ == '__main__':
 app.run(debug = True)