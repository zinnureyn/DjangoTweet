from django.contrib import admin
# from . import models
from tweetapp.models import Tweet


class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tweet Group', {'fields': ['tweet']}),
        ('Nickname Group', {'fields': ['nickname']}),

    ]
    #fields = ['tweet', 'nickname']


admin.site.register(Tweet, TweetAdmin)
