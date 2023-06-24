#!/usr/bin/python3
"""Gather information from API."""

import json
import requests
import sys


if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{api_url}/users"
    users_data = requests.get(users_url).json()

    all_employees_data = {}

    for user in users_data:
        user_id = user['id']
        username = user['username']

        todos_url = f"{api_url}/users/{user_id}/todos"
        todos_data = requests.get(todos_url).json()

        tasks = []
        for task in todos_data:
            task_title = task['title']
            task_completed = task['completed']
            tasks.append({
                "username": username,
                "task": task_title,
                "completed": task_completed
            })

        all_employees_data[user_id] = tasks

    json_filename = "todo_all_employees.json"

    with open(json_filename, mode='w') as file:
        json.dump(all_employees_data, file)
