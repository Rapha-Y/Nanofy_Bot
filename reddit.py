import praw
from nanofy import nanofy as nano

reddit = praw.Reddit("nanofy_bot", user_agent = "Nanofy Bot v0.1")

subreddit = reddit.subreddit("thanybombsbottesting")

for comment in subreddit.stream.comments():
    #bot was summoned
    if "!nanofy" == comment.body:
        with open("answered.txt", "a+") as f:
            #read replied comment list
            f.seek(0)
            ans_list = f.read()
            #comment has not been replied to
            if comment.id not in ans_list:
                #parent is a post
                if hasattr(comment.parent(), "selftext"):
                    raw_txt = comment.parent().selftext
                #parent is a comment
                else:
                    raw_txt = comment.parent().body
                nano_txt = nano(raw_txt)
                comment.reply(nano_txt)
                #append to replied comment list
                f.write(comment.id + "\n")