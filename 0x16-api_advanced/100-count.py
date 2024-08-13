#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, counts={}):
    """Recursively counts the occurrences of keywords in hot article titles."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    data = response.json().get("data", {})
    titles = [post.get("data", {}).get("title").lower() for post in data.get("children", [])]
    
    for word in word_list:
        word_lower = word.lower()
        for title in titles:
            counts[word_lower] = counts.get(word_lower, 0) + title.split().count(word_lower)
    
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")


