from django.db import models


class Tweet(models.Model):
    nickname = models.CharField(max_length=20)
    tweet = models.CharField(max_length=140)

    def __str__(self):
        return f"{self.nickname} - {self.tweet}"
