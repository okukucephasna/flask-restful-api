from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pymysql

app = Flask(__name__)
api = Api(app)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': ' ',
    'database': 'swiss_collection',
}

class Employee(Resource):
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

            return jsonify({'data': result})

        except Exception as e:
            return jsonify({'error': str(e)})

    def post(self):
        try:
            # Connect to MySQL
            connection = pymysql.connect(**db_config)

            # Create cursor
            with connection.cursor() as cursor:
                # Get data from request
                data = request.get_json()
                name = data['name']
                age = data['age']
                # Execute query
                query = "INSERT INTO product (name, age) VALUES (%s, %s)"
                cursor.execute(query, (name, age))
                connection.commit()

            # Close connection
            connection.close()

            return jsonify({'message': 'Data inserted successfully'})

        except Exception as e:
            return jsonify({'error': str(e)})

    def delete(self):
        try:
            # Connect to MySQL
            connection = pymysql.connect(**db_config)

            # Create cursor
            with connection.cursor() as cursor:
                # Get data from request
                data = request.get_json()
                employee_id = data['id']
                # Execute query
                query = "DELETE FROM product WHERE id=%s"
                cursor.execute(query, (employee_id,))
                connection.commit()

            # Close connection
            connection.close()

            return jsonify({'message': 'Data deleted successfully'})

        except Exception as e:
            return jsonify({'error': str(e)})

    def put(self):
        try:
            # Connect to MySQL
            connection = pymysql.connect(**db_config)

            # Create cursor
            with connection.cursor() as cursor:
                # Get data from request
                data = request.get_json()
                employee_id = data['id']
                name = data['name']
                age = data['age']
                # Execute query
                query = "UPDATE employees SET name=%s, age=%s WHERE id=%s"
                cursor.execute(query, (name, age, employee_id))
                connection.commit()

            # Close connection
            connection.close()

            return jsonify({'message': 'Data updated successfully'})

        except Exception as e:
            return jsonify({'error': str(e)})

api.add_resource(Employee, '/employees')

if __name__ == '__main__':
    app.run(debug=True)
