from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)
	image = models.ImageField(default="profile_pics/Screenshot_from_2019-05-13_02-31-56.png",blank=True, null=True, upload_to='media/profile_pics')
	# username = models.CharField(max_length=30, blank=True)
	firstname = models.CharField(max_length=30, blank=True)
	lastname = models.CharField(max_length=30,blank=True)
	address = models.TextField(max_length=100, blank=True)
	
	def __str__(self):
		return f'{self.user.username} Profile'