from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=50)
	author = models.ForeignKey(User)
	url = models.TextField()
	pub_date = models.DateTimeField()
	vote_count = models.IntegerField(default=1)
