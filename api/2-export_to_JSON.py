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
    undone = 0
    done = 0

    for user in response:
        username = user['username']

    json_filename = f"{user_id}.json"
    json_data = []

    for item in info:
        done = item['completed']
        task_title = item['title']
        json_data.append({
            "USER_ID": user_id,
            "USERNAME": username,
            "TASK_COMPLETED_STATUS": done,
            "TASK_TITLE": task_title
        })

    with open(json_filename, mode='w') as file:
        json.dump(json_data, file, indent=4)