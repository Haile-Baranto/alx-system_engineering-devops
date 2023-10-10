#!/usr/bin/python3
"""
This module provides a recursive function to retrieve titles of all
hot articles in a subreddit using the Reddit API.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieve titles of all hot articles in a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): A list to store the titles (default is []).
        after (str, optional): A token for pagination (default is None).

    Returns:
        list or None: A list of titles of hot articles, or None
        if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "My Reddit Scraper (by /u/YourRedditUsername)"}

    if after:
        url += f"&after={after}"

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json().get("data")
            hot_list.extend(post["data"]["title"] for post in
                            data.get("children", []))
            after = data.get("after")
            return recurse(subreddit, hot_list, after) if after else hot_list
        return None
    except Exception as e:
        return None
