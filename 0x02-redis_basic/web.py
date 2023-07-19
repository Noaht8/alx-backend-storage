# !/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import requests
import time
from functools import wraps

CACHE_EXPIRATION = 10  # seconds


def cache_decorator(func):
    """
    :param func:
    :return: The HTML content
    """
    cache = {}

    @wraps(func)
    def wrapper(url):
        if url in cache and time.time() - cache[url]['timestamp'] < CACHE_EXPIRATION:
            print(f"Retrieving cached content for {url}")
            return cache[url]['content']

        print(f"Fetching content for {url}")
        content = func(url)
        cache[url] = {'content': content, 'timestamp': time.time()}
        return content

    return wrapper


@cache_decorator
def get_page(url):
    """
    :param url: 
    :return: response
    """
    response = requests.get(url)
    return response.text
