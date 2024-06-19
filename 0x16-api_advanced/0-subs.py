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

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']

        else:
            return 0
    except requests.RequestException:
        return 0
