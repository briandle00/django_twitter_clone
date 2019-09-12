"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from twitter_profile import views as profile_views
from twitter_tweet import views as tweet_views

urlpatterns = [
    path('', profile_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signout/', profile_views.signout, name='signout'),
    path('feed/', tweet_views.feed, name='feed'),
    path('search/', profile_views.search, name='profile'),
    path('profile/<str:username>/', profile_views.profile, name='profile'),
    path('profile/<str:username>/addfollow/', profile_views.addfollow, name='addfollow'),
    path('profile/<str:username>/removefollow/', profile_views.removefollow, name='removefollow'),
    path('profile/<str:username>/followers/', profile_views.followers, name='removefollow'),
    path('profile/<str:username>/following/', profile_views.following, name='removefollow'),
]
