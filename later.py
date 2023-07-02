from flask import Flask, request
from flask_restful import Api, Resource
import pymysql

app = Flask(__name__)
api = Api(app)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': ' ',
    'database': 'swiss_collection',
    'cursorclass': pymysql.cursors.DictCursor
}

class DataResource(Resource):
    def get(self):
        try:
            # Connect to MySQL
            connection = pymysql.connect(**db_config)

            # Create cursor
            with connection.cursor() as cursor:
                # Execute query
                query = "SELECT * FROM product"
                cursor.execute(query)
                result = cursor.fetchall()

            # Close connection
            connection.close()

            return {'data': result}

        except Exception as e:
            return {'error': str(e)}

    def post(self):
        try:
            # Connect to MySQL
            connection = pymysql.connect(**db_config)

            # Create cursor
            with connection.cursor() as cursor:
                # Get data from request
                data = request.get_json()
                # Assuming the request data is a dictionary with keys matching the table columns
                columns = ', '.join(data.keys())
                values = ', '.join(["'{}'".format(value) for value in data.values()])

                # Execute query
                query = "INSERT INTO product ({}) VALUES ({})".format(columns, values)
                cursor.execute(query)
                connection.commit()

            # Close connection
            connection.close()

            return {'message': 'Data inserted successfully'}

        except Exception as e:
            return {'error': str(e)}

    def put(self):
        try:
            # Connect to MySQL
            connection = pymysql.connect(**db_config)

            # Create cursor
            with connection.cursor() as cursor:
                # Get data from request
                data = request.get_json()
                # Assuming the request data is a dictionary with keys matching the table columns
                values = ', '.join(["{}='{}'".format(key, value) for key, value in data.items()])

                # Execute query
                query = "UPDATE product SET {} WHERE id={}".format(values, data['id'])  # Assuming 'id' is the primary key
                cursor.execute(query)
                connection.commit()

            # Close connection
            connection.close()

            return {'message': 'Data updated successfully'}

        except Exception as e:
            return {'error': str(e)}

    def delete(self):
        try:
            # Connect to MySQL
            connection = pymysql.connect(**db_config)

            # Create cursor
            with connection.cursor() as cursor:
                # Get data from request
                data = request.get_json()

                # Execute query
                query = "DELETE FROM product WHERE id={}".format(data['id'])  # Assuming 'id' is the primary key
                cursor.execute(query)
                connection.commit()

            # Close connection
            connection.close()

            return {'message': 'Data deleted successfully'}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(DataResource, '/data')

if __name__ == '__main__':
    app.run(debug=True)
