from flask import Flask, request
from flask_restful import Api, Resource
import pymysql

# Create Flask application and API
app = Flask(__name__)
api = Api(app)

# Configure MySQL connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="testone"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

class DataResource(Resource):
    def get(self):
        # Execute the SQL query to retrieve data
        cursor.execute("SELECT * FROM users1")
        result = cursor.fetchall()

        # Convert the result into a list of dictionaries
        users = []
        for row in result:
            users.append({
                'id': row[0],
                'first_name': row[1],
                'second_name': row[2],
                'job': row[3]
            })

        # Return the data as JSON
        return {'data': users}


# Example resource to create a new user in the database
class CreateUserResource(Resource):
    def post(self):
        # Retrieve user data from the request
        data = request.get_json()
        first_name = data['first_name']
        second_name = data['second_name']
        job = data['job']

        # Execute the SQL query to insert the user into the database
        query = "INSERT INTO users1 (first_name, second_name, job) VALUES (%s, %s, %s)"
        cursor.execute(query, (first_name, second_name, job))
        connection.commit()

        # Return a success message
        return {'message': 'User created successfully'}


class UpdateUserResource(Resource):
    def put(self, user_id):
        # Retrieve user data from the request
        data = request.get_json()
        first_name = data['first_name']
        second_name = data['second_name']
        job = data['job']

        # Execute the SQL query to update the user in the database
        query = "UPDATE users1 SET first_name=%s, second_name=%s, job=%s WHERE id=%s"
        cursor.execute(query, (first_name, second_name, job, user_id))
        connection.commit()

        # Return a success message
        return {'message': 'User updated successfully'}


# Add the resources to the API with specified endpoints
api.add_resource(CreateUserResource, '/users')
api.add_resource(UpdateUserResource, '/users/<int:user_id>')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
