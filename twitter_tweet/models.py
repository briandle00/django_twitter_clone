from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TwitterTweet(models.Model):
	user = models.ForeignKey(User, related_name='tweets', on_delete=models.DO_NOTHING)
	message = models.CharField(max_length=280)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created_at',)