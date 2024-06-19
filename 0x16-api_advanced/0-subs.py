#!/usr/bin/python3
"""Query subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the total number of subscribers for a given subreddit
    Args: subreddit

    Return: No of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    dic = response.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return response.json()['data']['subscribers']
