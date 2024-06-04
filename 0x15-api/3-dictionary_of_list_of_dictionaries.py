#!/usr/bin/python3
""" Script that uses API to get info about employee """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    response = requests.get(user)
    json_o = response.json()
    d_task = {}
    for user in json_o:
        name = user.get('username')
        user_id = user.get('id')
        todos = '{}todos?userId={}'.format(url, user_id)
        response = requests.get(todos)
        tasks = response.json()
        l_task = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            l_task.append(dict_task)

        d_task[str(user_id)] = l_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
