from flask import Flask, request
from flask_restful import Api, Resource
import pymysql

app = Flask(__name__)
api = Api(app)

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="testone"
)

cursor = connection.cursor()

class DataResource(Resource):
    def get(self):
        cursor.execute("SELECT * FROM users1")
        result = cursor.fetchall()

        users = []
        for row in result:
            users.append({
                'id': row[0],
                'first_name': row[1],
                'second_name': row[2],
                'job': row[3]
            })

        return {'data': users}


class CreateUserResource(Resource):
    def post(self):
        data = request.get_json()
        first_name = data['first_name']
        second_name = data['second_name']
        job = data['job']

        query = "INSERT INTO users1 (first_name, second_name, job) VALUES (%s, %s, %s)"
        cursor.execute(query, (first_name, second_name, job))
        connection.commit()

        return {'message': 'User created successfully'}


class UpdateUserResource(Resource):
    def put(self, user_id):
        data = request.get_json()
        first_name = data['first_name']
        second_name = data['second_name']
        job = data['job']

        query = "UPDATE users1 SET first_name=%s, second_name=%s, job=%s WHERE id=%s"
        cursor.execute(query, (first_name, second_name, job, user_id))
        connection.commit()

        return {'message': 'User updated successfully'}


class DeleteUserResource(Resource):
    def delete(self, user_id):
        query = "DELETE FROM users1 WHERE id=%s"
        cursor.execute(query, (user_id,))
        connection.commit()

        return {'message': 'User deleted successfully'}


api.add_resource(DataResource, '/users')
api.add_resource(CreateUserResource, '/users')
api.add_resource(UpdateUserResource, '/users/<int:user_id>')
api.add_resource(DeleteUserResource, '/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)