from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView



def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {'tweets': all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)


@login_required(login_url='/login/')
def addtweet(request):
    if request.method == 'POST':
        # nickname = request.POST['nickname']
        message = request.POST['message']
        # tweet = models.Tweet(nickname=nickname, message=message)
        # tweet.save()
        models.Tweet.objects.create(username=request.user, tweet=message)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, 'tweetapp/addtweet.html')


@login_required(login_url='/login/')
def addtweetbyform(request):
    if request.method == 'POST':
        form = forms.AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname_input']
            message = form.cleaned_data['message_input']
            models.Tweet.objects.create(nickname=nickname, tweet=message)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            return render(request, 'tweetapp/addtweetbyform.html', context={'form': form})
    else:
        form = forms.AddTweetForm()
        return render(request, 'tweetapp/addtweetbyform.html', context={'form': form})


@login_required(login_url='/login/')
def addtweetbymodelform(request):
    if request.method == 'POST':
        form = forms.AddTweetModelForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            return render(request, 'tweetapp/addtweetbymodelform.html', context={'form': form})
    else:
        form = forms.AddTweetModelForm()
        return render(request, 'tweetapp/addtweetbymodelform.html', context={'form': form})

@login_required(login_url='/login/')
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if tweet.username == request.user:
        tweet.delete()
        return redirect(reverse('tweetapp:listtweet'))


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy ('login')
    template_name = 'registration/signup.html'


