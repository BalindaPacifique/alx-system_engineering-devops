#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    data = response.json().get("data", {})
    hot_list += [post.get("data", {}).get("title") for post in data.get("children", [])]
    
    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list

