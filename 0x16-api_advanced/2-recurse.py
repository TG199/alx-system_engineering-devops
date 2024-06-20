#!/usr/bin/python3
"""Recursively query Reddit API"""
import requests


def add_title(hot_list, hot_posts):
    """Adds to a list"""
    if len(hot_posts) == 0:
        return

    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {
        'after': after
    }

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    dic = response.json()
    host_posts = dic['data']['children']
    add_title(hot_list, host_posts)
    after = dic['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
