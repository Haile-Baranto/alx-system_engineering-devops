#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.
"""

import json
import requests

def fetch_todos_for_user(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    return requests.get(url + "todos", params={"userId": user_id}).json()

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    todo_data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = fetch_todos_for_user(user_id)
        user_todos = []

        for todo in todos:
            task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            user_todos.append(task_info)

        todo_data[user_id] = user_todos

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_data, jsonfile)