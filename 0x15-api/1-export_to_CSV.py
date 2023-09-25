#!/usr/bin/python3
"""
This script retrieves and exports TODO list progress for
a given employee using the JSONPlaceholder API to a CSV file.

Usage: python script.py EMPLOYEE_ID
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves TODO list progress for the specified
    employee ID and exports it to a CSV file.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    api_url = f"{base_url}todos?userId={employee_id}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            todo_list = response.json()
            employee_name = get_employee_name(employee_id)
            csv_file_name = f"{employee_id}.csv"

            with open(csv_file_name, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(
                    csv_file, quoting=csv.QUOTE_MINIMAL
                )

                for task in todo_list:
                    csv_writer.writerow([employee_id, employee_name.split()[0],
                                         task["completed"], task["title"]])

            print(f"Data exported to {csv_file_name}")
        else:
            print("Failed to retrieve TODO list progress.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("Failed to retrieve TODO list progress.")


def get_employee_name(employee_id):
    """
    Retrieves the employee's name for the specified employee ID.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        str: The employee's name or "Unknown" if not found.
    """
    user_api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    try:
        response = requests.get(user_api_url)
        if response.status_code == 200:
            user_info = response.json()
            return user_info["name"].split()[0]  # Use only the first name
        else:
            return "Unknown"
    except requests.exceptions.RequestException:
        return "Unknown"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for EMPLOYEE_ID.")
