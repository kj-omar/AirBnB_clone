#!/usr/bin/python3
"""simple RESTful API for playing around with Flask"""
from flask import Flask, render_template, jsonify, abort, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth
from fontTools import unicode

app = Flask(__name__)
auth = HTTPBasicAuth()

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
    },
    {
        'id': 3,
        'title': 'Read a book',
        'description': 'Need to find a good Python book on the web',
    },
    {
        'id': 4,
        'title': 'Watch TV',
        'description': 'Need to find a good Python TV show on the web',
    }
]


def make_public_task(task):
    """make a public task"""
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'admin'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@app.route('/todo/api/v1.0/tasks', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_tasks():
    """get all the tasks"""
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'], strict_slashes=False)
@auth.login_required
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'], strict_slashes=False)
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'], strict_slashes=False)
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'], strict_slashes=False)
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
