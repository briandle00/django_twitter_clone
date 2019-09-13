from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import SignUpForm, LogInForm
from twitter_tweet.forms import TweetForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('profile/' + request.user.username + '/')
    else:
        if request.method == 'POST':
            if 'signupform' in request.POST:
                signupform = SignUpForm(data=request.POST)
                loginform = LogInForm()
                if signupform.is_valid():
                    username = signupform.cleaned_data['username']
                    password = signupform.cleaned_data['password1']
                    signupform.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/')
            else:
                signupform = SignUpForm()
                loginform = LogInForm(data=request.POST)
                if loginform.is_valid():
                    login(request, loginform.get_user())
                    return redirect('/')
        else:        
            signupform = SignUpForm()
            loginform = LogInForm()
    return render(request, 'frontpage.html', {'signupform': signupform, 'loginform': loginform})

def signout(request):
    logout(request)
    return redirect('/')

def profile(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username)
        if request.method == 'POST':
            form = TweetForm(data=request.POST)

            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()

                redirecturl = request.POST.get('redirect', '/')

                return redirect(redirecturl)
        else:
            form = TweetForm()
        return render(request, 'profile.html', {'user': user, 'form': form})
    else:
        return redirect('/')

def following(request, username):
    user = User.objects.get(username=username)
    following = user.twitterprofile.follows
    return render(request, 'following.html', {'following': following})

def followers(request, username):
    user = User.objects.get(username=username)
    followers = user.twitterprofile.followed_by
    return render(request, 'followers.html', {'followers': followers})

@login_required
def addfollow(request, username):
    user = User.objects.get(username=username)
    request.user.twitterprofile.follows.add(user.twitterprofile)
    return redirect('/profile/' + user.username + '/')

@login_required
def removefollow(request, username):
    user = User.objects.get(username=username)
    request.user.twitterprofile.follows.remove(user.twitterprofile)
    return redirect('/profile/' + user.username + '/')

def search(request):
    if request.POST['username'] in [user.username for user in User.objects.all()]:
        return redirect('/profile/' + request.POST['username'] + '/')
    else:
        return render(request, 'searchfail.html')

def mentionsearch(request, username):
    if username in [user.username for user in User.objects.all()]:
        return redirect('/profile/' + username + '/')
    else:
        return render(request, 'searchfail.html')