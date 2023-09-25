#!/usr/bin/python3
"""
This script retrieves and displays TODO list progress for
a given employee using the JSONPlaceholder API.

Usage: python script.py EMPLOYEE_ID
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves TODO list progress for the specified employee ID and displays it.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        None
    """
    # Base URL of the REST API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Construct the API URL with the employee's ID
    api_url = f"{base_url}todos?userId={employee_id}"

    try:
        # Make an HTTP GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            todo_list = response.json()

            # Calculate TODO list progress
            completed_tasks = [task for task in todo_list if task["completed"]]
            total_tasks = len(todo_list)
            employee_name = get_employee_name(employee_id)

            # Display progress information
            print("Employee {} is done with tasks ({}/{})".format(
                employee_name, len(completed_tasks), total_tasks))
            for task in completed_tasks:
                print(f"\t{task['title']}")
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
    # API endpoint to retrieve user information
    user_api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    try:
        # Make an HTTP GET request to retrieve user information
        response = requests.get(user_api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            user_info = response.json()
            return user_info["name"]
        else:
            return "Unknown"
    except requests.exceptions.RequestException:
        return "Unknown"  # Return "Unknown" on error


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for EMPLOYEE_ID.")
