from gtts import gTTS
from praw import models
from praw.models import MoreComments
import praw
from praw.models.reddit.comment import CommentModeration
from praw.reddit import Comment
import os
from playsound import playsound

reddit = praw.Reddit(
    client_id = "J2IA0AOx5mAp9_bM3hVIrg",
    client_secret = "-G_ALHUzvvN0dKnprk2QUJxzvFCs7w",
    user_agent = "brainded",
    password = "Sparkles0001"
)

subreddit = reddit.subreddit("shitposting")
submission = reddit.submission(id="qnbksb")

comments = submission.comments
while 1 ==1 :
    for comment in submission.comments.list():
        if hasattr(comment, "body"):
            def textToAudio(str):
                audio = gTTS(str)
                audio.save('example.mp3')


            textToAudio(comment.body)
            playsound('example.mp3')

