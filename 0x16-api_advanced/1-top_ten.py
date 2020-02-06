#!/usr/bin/python3
import requests
"""
Module that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""


def top_ten(subreddit):
    """
    This method queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://api.reddit.com/r/{}/?limit=10".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code is 200:
        response_json = response.json()
        for i in range(0, 10):
            print(response_json['data']['children'][i]['data']['title'])
    else:
        print(None)
