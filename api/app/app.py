# -*- coding: utf-8 -*-
# ！usr/bin/python
# ==========================
from flask import Flask, Response
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = Api(app)

ITEMS = '''
    {
        "MemberList": [{
                "Id":1,
                "UserName": "sb1",
                "Age":10
            },
            {
                "Id":2,
                "UserName": "sb2",
                "Age":10
            },
            {
                "Id":3,
                "UserName": "sb3",
                "Age":10
            }]
    }
    '''
my_friends = json.loads(ITEMS)
memberList = my_friends.get('MemberList')

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self,user_id):
        return memberList[user_id]

    def delete(self, todo_id):
        del ITEMS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        ITEMS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return Response(json.dumps(memberList), mimetype='application/json')

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == "__main__":
    app.run(host='0.0.0.0')