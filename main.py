import praw
import datetime
import concurrent.futures

reddit = praw.Reddit()

# choose a subreddit
subreddit_name = 'python'

# get N random posts from the subreddit
N = 50
posts = []

# define a function to get a post and append it to a list


def get_post():
    sub = reddit.subreddit(subreddit_name).random()
    posts.append(sub)


# use concurrent.futures to get N posts in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=N) as executor:
    futures = [executor.submit(get_post) for _ in range(N)]
    concurrent.futures.wait(futures)


# print the titles of the posts
for post in posts:
    print(post.title)
    print(post.permalink)
    print(datetime.datetime.fromtimestamp(post.created_utc))
    print('===============')
