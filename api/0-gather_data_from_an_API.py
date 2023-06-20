#!/usr/bin/python3
"""Gather information from API."""

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

    for item in response:
        username = item['name']

    for item in info:
        if item['completed'] is True:
            done += 1
        undone += 1

    print(f"Employee {username} is done with tasks({done}/{undone}):")

    for items in info:
        if items['completed'] is True:
            task = items['title']
            print(f"\t {task}")
