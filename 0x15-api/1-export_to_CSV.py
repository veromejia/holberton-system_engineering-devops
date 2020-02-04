#!/usr/bin/python3
"""script that returns information for a given employee of his/her
TODO list progress."""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get("{}users/{}".format(url, user_id)).json()
    todos = requests.get("{}todos".
                         format(url), params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, user.get('username'),
                             task.get('completed'), task.get('title')])
