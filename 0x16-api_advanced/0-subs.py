#!/usr/bin/python3
"""
Queries the Reddit API to return the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My Reddit Scraper (by /u/YourRedditUsername)"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data.get("data", {}).get("subscribers", 0) if\
            response.status_code == 200 else 0
    except Exception as e:
        return 0
