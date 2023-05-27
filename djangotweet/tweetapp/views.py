from django.shortcuts import render

from . import models


def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {'tweets': all_tweets}
    return render(request, 'tweetapp/listtweet.html', context={'all_tweets': tweet_dict})


def addtweet(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'tweetapp/addtweet.html')
