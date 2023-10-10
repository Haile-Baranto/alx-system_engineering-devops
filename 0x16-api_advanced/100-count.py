#!/usr/bin/python3
"""
Module for a function that queries the Reddit API recursively.
"""

import requests


def count_words(subreddit, word_list, after='', word_dict=None):
    """Query the Reddit API recursively, parse hot article titles,
    and print sorted keyword counts."""

    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        sorted_word_counts = sorted((word, count) for
                                    word, count in word_dict.items() if count)
        for word, count in sorted_word_counts:
            print(f'{word}: {count}')
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers,
                            params=parameters, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json()['data']
        hot_posts, next_after = data['children'], data['after']

        for post in hot_posts:
            title_words = post['data']['title'].lower().split()
            for word in word_dict:
                word_dict[word] += title_words.count(word)
    except Exception:
        return

    count_words(subreddit, word_list, next_after, word_dict)
