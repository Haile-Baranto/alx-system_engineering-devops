#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""

import csv
import requests
import sys


def fetch_todos_for_user(user_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{user_id}"
    todos_url = f"{base_url}todos"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        username = user_data.get("username")

        todos_response = requests.get(todos_url, params={"userId": user_id})
        todos_response.raise_for_status()
        todos = todos_response.json()

        return user_id, username, todos
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


def export_todos_to_csv(user_id, username, todos):
    csv_file_name = f"{user_id}.csv"

    with open(csv_file_name, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow([
                user_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ])

    print(f"Data exported to {csv_file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        user_id, username, todos = fetch_todos_for_user(employee_id)
        export_todos_to_csv(user_id, username, todos)
    except ValueError:
        print("Please provide a valid integer for EMPLOYEE_ID.")
