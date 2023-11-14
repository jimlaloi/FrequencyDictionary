# This script collects titles and all comments from the top posts in a list of subreddits (limited to ~1000 posts)

import praw, time

# You'll need a Reddit account with a script app
# Tutorial: https://www.jcchouinard.com/reddit-api/
# Access your app's credentials: https://old.reddit.com/prefs/apps
# Supply your app's info
reddit = praw.Reddit(client_id= '',  # code appearing under your app's name
                     client_secret='',  # code listed as "secret"
                     user_agent= '',  # your app's name
                     username='',  # your Reddit username
                     password='')  # your Reddit password

subreddits = ['france',
              'quebec',
              'montreal',
              'jeuxvideo',
              'jardin',
              'nouvelles',
              'musique',
              'Cuisine',
              'Ligue1',
              'programmation',
              'ScienceFr',
              'causerie',
              'penseesdedouche'
              ]

# set number of seconds to sleep between each request for more comments
# If you get "Too many requests" errors, increase the sleep time
t = 3

print(str(len(subreddits))+" subreddits provided")

for sub in subreddits:
    with open("r_" + sub + ".txt", "w", encoding="utf-8") as output:
        print("\nCollecting posts from subreddit r/" + sub)
        posts = {}
        top_posts = reddit.subreddit(sub).top(limit = None)

        for post in top_posts:
            posts[post.id] = post.title

        IDs = list(posts.keys())

        print("There are " + str(len(IDs)) + " posts collected from r/" + sub)

        for index,ID in enumerate(IDs):
            output.write(posts[ID]+"\n")
            print("- Collecting comments from post #" + str(index + 1) + " of " + str(len(IDs))+" (https://www.reddit.com/r/" + sub + "/comments/" + ID + ")")
            submission = reddit.submission(ID)
            submission.comments.replace_more(limit= None)
            comments = submission.comments.list()
            for comment in comments:
                output.write(comment.body + "\n")
            print("     - Post title and " + str(len(comments)) + " comments written to file")
            time.sleep(t)
