#!/usr/bin/python3
"""simple RESTful API for playing around with Flask"""
from flask import Flask, render_template, jsonify

app = Flask(__name__)

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


@app.route('/todo/api/v1.0/tasks', methods=['GET'], strict_slashes=False)
def get_tasks():
    """get all the tasks"""
    return jsonify({'tasks': 'all the tasks'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
