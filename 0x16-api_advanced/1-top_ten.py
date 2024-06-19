#!/usr/bin/python3
"""Query top 10 post"""
import requests


def top_ten(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {
        'limit': 10
    }

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return
    dic = response.json()
    top_ten = dic['data']['children']
    if len(top_ten) == 0:
        print(None)
    else:
        for post in top_ten:
            print(post['data']['title'])
