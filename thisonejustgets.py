from flask import Flask
from flask_restful import Api, Resource
import pymysql

# Create Flask application and API
app = Flask(__name__)
api = Api(app)

connection = pymysql.connect(host='localhost', user='root', password='',
                                     database='testone')


# Create a cursor object to interact with the database
cursor = connection.cursor()

# Example resource to fetch data from the database
class DataResource(Resource):
    def get(self):
        # Execute the SQL query to retrieve data
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()

        # Convert the result into a list of dictionaries
        data = []
        for row in result:
            data.append({
                'id': row[0],
                'name': row[1],
                'description': row[2]
            })

        # Return the data as JSON
        return {'data': data}

# Add the resource to the API with a specified endpoint
api.add_resource(DataResource, '/data')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
