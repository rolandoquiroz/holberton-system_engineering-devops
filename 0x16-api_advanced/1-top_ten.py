#!/usr/bin/python3
import requests
"""
MethodModule that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for
a given subreddit.
"""


def top_ten(subreddit):
    """
    This method queries the Reddit API and returns the number
    of subscribers
    If an invalid subreddit is given, the function should return 0.
    """
    url = "https://api.reddit.com/r/{}/?sort=hot&limit=10".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code is 200:
        response_json = response.json()
        for i in range(0, 10):
            print (response_json['data']['children'][i]['data']['title'])
    else:
        print (None)
