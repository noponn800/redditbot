import praw

query_string = "query string"
#put what you want to reply to here
subreddit_name - "teenagers"
#put the subreddit name here
post_limit = 1000
#put the limit of posts processed here
reply_string = "reply string"
#put what you want to reply here

reddit = praw.Reddit(
    #user credentials
)

subreddit = reddit.subreddit(subreddit_name)

for comment in subreddit.comments(limit=post_limit):
    if query_string in comment.body:
        comment.reply(reply_string)