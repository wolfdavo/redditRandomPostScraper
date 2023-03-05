import praw
import datetime

reddit = praw.Reddit()

# choose a subreddit
subreddit_name = 'python'

# get N random posts from the subreddit
N = 10
posts = []
for submission in reddit.subreddit(subreddit_name).random_rising(limit=N):
    posts.append(submission)

# print the titles of the posts
for post in posts:
    print(post.title)
    print(post.permalink)
    print(datetime.datetime.fromtimestamp(post.created_utc))
    print('===============')
