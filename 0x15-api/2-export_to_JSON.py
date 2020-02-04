#!/usr/bin/python3
"""Exports TODO list progress info for a given employee ID to JSON"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get("{}users/{}".format(url, user_id))
    todos = requests.get("{}todos".format(url)).json()
    todo_dict = {}
    task_list = []

    for task in todos:
        if task.get('userId') == int(user_id):
            task_dict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            task_list.append(task_dict)
    todo_dict[user_id] = task_list

    filename = user_id + '.json'
    with open(filename, mode='w') as f:
        json.dump(todo_dict, f)
