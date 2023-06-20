#!/usr/bin/python3
"""Gather information from API."""

import requests
import sys
import csv


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

    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # writer.writerow(["USER_ID", "USERNAME",
        # "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for item in info:
            done = item['completed']
            item = item['title']
            writer.writerow([user_id, username, done, item])
