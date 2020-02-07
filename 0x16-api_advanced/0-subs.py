#!/usr/bin/python3
"""module to request number of subscribers"""
import json
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers to a subreddit"""
    req = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={"User-Agent": "Mozilla/5.0\
                       (X11; Ubuntu; Linux x86_64; rv:72.0)\
                       Gecko/20100101 Firefox/72.0"},
                       allow_redirects=False)
    if req.status_code == 404:
        return 0
    data = req.json().get("data")
    return data.get("subscribers")
