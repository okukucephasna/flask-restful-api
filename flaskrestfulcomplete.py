from flask import Flask, request
from flask_restful import Api, Resource
import pymysql

app = Flask(__name__)
api = Api(app)

# MySQL configuration
connection = pymysql.connect(host='localhost', user='root', password='',
                                     database='testone')

class DataResource(Resource):
    def get(self):
        try:
            # Connect to MySQL
            cursor = connection.cursor()

            # Execute query
            query = "SELECT * FROM users"
            cursor.execute(query)
            result = cursor.fetchall()

            # Convert result to a list of dictionaries
            data = []
            columns = [column[0] for column in cursor.description]
            for row in result:
                data.append(dict(zip(columns, row)))

            # Close connection
            cursor.close()
            connection.close()

            return {'data': data}

        except Exception as e:
            return {'error': str(e)}

    def post(self):
        try:
            # Connect to MySQL
            cursor = connection.cursor()

            # Get data from request
            data = request.get_json()
            # Assuming the request data is a dictionary with keys matching the table columns
            columns = ', '.join(data.keys())
            values = ', '.join(["'{}'".format(value) for value in data.values()])

            # Execute query
            query = "INSERT INTO users ({}) VALUES ({})".format(columns, values)
            cursor.execute(query)
            connection.commit()

            # Close connection
            cursor.close()
            connection.close()

            return {'message': 'Data inserted successfully'}

        except Exception as e:
            return {'error': str(e)}

    def put(self):
        try:
            # Connect to MySQL
            cursor = connection.cursor()

            # Get data from request
            data = request.get_json()
            # Assuming the request data is a dictionary with keys matching the table columns
            values = ', '.join(["{}='{}'".format(key, value) for key, value in data.items()])

            # Execute query
            query = "UPDATE users SET {} WHERE id={}".format(values, data['id'])  # Assuming 'id' is the primary key
            cursor.execute(query)
            connection.commit()

            # Close connection
            cursor.close()
            connection.close()

            return {'message': 'Data updated successfully'}

        except Exception as e:
            return {'error': str(e)}

    def delete(self):
        try:
            # Connect to MySQL
            cursor = connection.cursor()

            # Get data from request
            data = request.get_json()

            # Execute query
            query = "DELETE FROM users WHERE id={}".format(data['id'])  # Assuming 'id' is the primary key
            cursor.execute(query)
            connection.commit()

            # Close connection
            cursor.close()
            connection.close()

            return {'message': 'Data deleted successfully'}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(DataResource, '/data')

if __name__ == '__main__':
    app.run(debug=True)
