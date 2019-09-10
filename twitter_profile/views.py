from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import SignUpForm, LogInForm
from twitter_tweet.forms import TweetForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('/' + request.user.username + '/')
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

def signout(request, username):
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
