from flask import Flask, request
from flask_restful import Api, Resource
import pymysql

# Create Flask application and API
app = Flask(__name__)
api = Api(app)

connection = pymysql.connect(host='localhost', user='root', password='',
                                     database='testone')
cursor = connection.cursor()
# Create a cursor object to interact with the database

# Example resource to create a new user in the database
class CreateUserResource(Resource):
    def post(self):
        # Retrieve user data from the request
        data = request.get_json()

        first_name = data['first_name']
        second_name = data['second_name']
        job = data['job']

        # Execute the SQL query to insert the user into the database
        query = "INSERT INTO users1 (first_name, second_name, job) VALUES (%s, %s,%s)"
        cursor.execute(query, (first_name, second_name, job))
        connection.commit()

        # Return a success message
        return {'message': 'User created successfully'}

# Add the resource to the API with a specified endpoint
api.add_resource(CreateUserResource, '/users')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
