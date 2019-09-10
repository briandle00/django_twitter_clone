from django import forms
from django.contrib.auth.models import User
from django.utils.html import strip_tags

from .models import TwitterTweet

class TweetForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "What's on your mind?", 'class': 'form-control'}), max_length=280)

	class Meta:
		model = TwitterTweet
		fields = ('message',)
		exclude = ('user',)