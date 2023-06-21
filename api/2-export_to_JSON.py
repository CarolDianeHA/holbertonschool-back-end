#!/usr/bin/python3
"""Gather information from API."""

import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com"
    url = f"{api_url}/users/{user_id}/todos"
    users = f"{api_url}/users?id={user_id}"
    data = requests.get(url)
    info = data.json()
    users_names = requests.get(users)
    response = users_names.json()

    for user in response:
        username = user['username']

    json_filename = f"{user_id}.json"
    json_data = {user_id: []}

    for item in info:
        done = item['completed']
        task_title = item['title']
        json_data[user_id].append({
            "task": task_title,
            "completed": done,
            "username": username
        })

    with open(json_filename, mode='w') as file:
        json.dump(json_data, file, indent=4)
