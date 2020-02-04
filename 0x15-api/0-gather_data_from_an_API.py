#!/usr/bin/python3
""" using a REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get("{}users/{}".format(url, user_id))
    name = user.json().get('name')
    todos = requests.get("{}todos".format(url))
    result = 0
    total = 0

    for task in todos.json():
        if task.get('userId') == int(user_id):
            result += 1
            if task.get('completed'):
                total += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, total, result))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(user_id) and task.get('completed')]))
