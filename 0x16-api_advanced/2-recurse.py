#!/usr/bin/python3
"""returns the number of subscribers for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Print all hot posts for a given subreddit"""
    req = requests.get("https://www.reddit.com/r/{}/hot.json?after={}".
                       format(subreddit, after),
                       headers={"User-Agent": "Mozilla/5.0\
                       (X11; Ubuntu; Linux x86_64; rv:72.0)\
                       Gecko/20100101 Firefox/72.0"},
                       allow_redirects=False)
    if req.status_code == 404:
        return None
    data = req.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    for i in data.get("children"):
        hot_list.append(i.get("data").get("title"))
    if after:
        return recurse(subreddit, hot_list, count, after)
    return hot_list
