#!/usr/bin/python3
"""Gather information from API."""

import json
from requests import get
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    user_data = get(f'{url}?id={user_id}').json()

    for item in user_data:
        username = item['username']

    todos = get(f'{url}/{user_id}/todos').json()
    data_list = []
    final_dictionary = {}
    for todo in todos:
        tasks = todo['title']
        done = todo['completed']
        dic = {
            "task": tasks,
            "completed": done,
            "username": username
        }
        data_list.append(dic)
    final_dictionary[user_id] = data_list
    with open(f'{user_id}.json', 'w') as f:
        json.dump(final_dictionary, f)
