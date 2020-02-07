#!/usr/bin/python3
"""module to request the top 10 for a subscribers"""
import json
import requests


def top_ten(subreddit):
    """Return the top 10 hot post for a subreddit"""
    req = requests.get("https://www.reddit.com/r/{}/hot/.json?limit=10"
                       .format(subreddit),
                       headers={"User-Agent": "Mozilla/5.0\
                       (X11; Ubuntu; Linux x86_64; rv:72.0)\
                       Gecko/20100101 Firefox/72.0"},
                       allow_redirects=False)
    if req.status_code == 404:
        print("None")
    else:
        data = req.json().get("data").get("children")
        for child in data:
            print(child.get("data").get("title"))
