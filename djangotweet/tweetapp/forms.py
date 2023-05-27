from django import forms
from django.forms import ModelForm
from .models import Tweet


class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label='Nickname', max_length=20)
    message_input = forms.CharField(label='Message', max_length=140,
                                    widget=forms.Textarea(attrs={"class": "tweetmessage"}))


class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['username', 'tweet']
        # labels = {'nickname': 'Nickname', 'tweet': 'Message'}
        # widgets = {'tweet': forms.Textarea(attrs={"class": "tweetmessage"})}
