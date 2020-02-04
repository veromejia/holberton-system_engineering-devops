#!/usr/bin/python3
"""Exports data in the JSON format"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(url)).json()
    todos = requests.get("{}todos".format(url)).json()
    todo_dict = {}

    for user in users:
        task_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                task_list.append(task_dict)
        todo_dict[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_dict, f)
