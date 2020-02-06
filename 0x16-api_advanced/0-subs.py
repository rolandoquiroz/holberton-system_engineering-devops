#!/usr/bin/python3
import requests
"""
MethodModule that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for
a given subreddit.
"""


def number_of_subscribers(subreddit):
    """
    This method queries the Reddit API and returns the number
    of subscribers
    If an invalid subreddit is given, the function should return 0.
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code is 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
