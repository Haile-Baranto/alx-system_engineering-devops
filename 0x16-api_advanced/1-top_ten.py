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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My Reddit Scraper (by /u/YourRedditUsername)"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        titles = [post["data"]["title"] for post in
                  data.get("data", {}).get("children", [])]

        # Print the titles
        print(*titles, sep='\n')
    except Exception as e:
        print(None)
