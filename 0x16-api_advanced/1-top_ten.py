#!/usr/bin/python3
"""
The module contain a function to prints the top 10 hot posts
"""

import requests


def top_ten(subreddit):
    """
    Retrieve and print the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Prints:
        The titles of the first 10 hot posts, or None if the subreddit is
        invalid or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My Reddit Scraper (by /u/YourRedditUsername)"}

    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 404:
            print("None")
            return

        results = response.json().get("data")
        titles = [child.get("data").get("title")
                  for child in results.get("children")]
        for title in titles:
            print(title)
    except Exception as e:
        print('None')
