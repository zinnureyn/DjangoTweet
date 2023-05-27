from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    # nickname = models.CharField(max_length=20)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # kullaıcı silinirse tweetleride silinsin
    tweet = models.CharField(max_length=140)

    def __str__(self):
        return f"{self.username} - {self.tweet}"
