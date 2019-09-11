from django.shortcuts import render

from .models import TwitterTweet

# Create your views here.
def feed(request):
    follows = [request.user.id]
    for id in request.user.twitterprofile.follows.all():
        follows.append(id.user)
    tweets = TwitterTweet.objects.filter(user_id__in=follows)
    return render(request, 'feed.html', {'tweets': tweets})