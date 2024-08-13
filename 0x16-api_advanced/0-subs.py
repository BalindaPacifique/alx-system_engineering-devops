#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0
    
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
