from rest_framework import serializers

from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Profile
        fields = [ 'pk', 'user', 'image', 'firstname', 'lastname', 'address']

    #  # image = serializers.ImageField(max_length=None,use_url=True)
    # documents = serializers.FileField(max_length=None,use_url=True)




    # user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)
	# image = models.ImageField(default="profile_pics/Screenshot_from_2019-05-13_02-31-56.png",blank=True, null=True, upload_to='media/profile_pics')
	# # username = models.CharField(max_length=30, blank=True)
	# firstname = models.CharField(max_length=30, blank=True)
	# lastname = models.CharField(max_length=30,blank=True)
	# address = models.TextField(max_length=100, blank=True)
	