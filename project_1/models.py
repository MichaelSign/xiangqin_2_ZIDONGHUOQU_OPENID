from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model) :
	name = models.CharField(max_length = 128)
	sex = models.CharField(max_length = 2)
	age = models.IntegerField(default=0)
	education = models.IntegerField (default=0)
	Occupation = models.CharField(max_length=128)
	height = models.IntegerField(default=0)
	weight = models.IntegerField(default=0)
	BJHouseholds = models.BooleanField(default = False)
	car =  models.BooleanField(default = False)
	house = models.BooleanField(default = False)
	hometown = models.CharField(max_length=1024)
	require = models.CharField(max_length=8096,blank=True)
	flag = models.BooleanField(default = False)
	WxNo = models.CharField(max_length=128,blank=True)
	img = models.ImageField(upload_to='profile_images', blank=True)
	message = models.CharField(max_length=8096,blank=True)
	QqNo = models.CharField(max_length = 128,blank=True)
	location = models.CharField(max_length = 1024,blank=True)
	Character = models.CharField(max_length = 128,blank=True)
	views = models.IntegerField(default=0)
	synopsis = models.CharField(max_length=128,blank=True)

	OpenID = models.CharField(max_length = 128, unique=True)

	def __unicode__(self) :
		return self.name

'''
class UserProfile(models.Model) :
	name = models.CharField(max_length = 128)
	sex = models.CharField(max_length = 2)
	age = models.IntegerField(default=0)
	education = models.CharField(max_length=128)
	Occupation = models.CharField(max_length=128)
	height = models.IntegerField(default=0)
	weight = models.IntegerField(default=0)
	BJHouseholds = models.BooleanField(default = False)
	car =  models.BooleanField(default = False)
	house = models.BooleanField(default = False)
	hometown = models.CharField(max_length=1024)
	require = models.CharField(max_length=8096)
	flag = models.BooleanField(default = False)
	WxNo = models.CharField(max_length=128)
	img = models.ImageField(upload_to='profile_images', blank=True)
	message = models.CharField(max_length=8096)
	QqNo = models.CharField(max_length = 128)
	location = models.CharField(max_length = 1024)
	Character = models.CharField(max_length = 128)
	views = models.IntegerField(default=0)
	synopsis = models.CharField(max_length=128)

	OpenID = models.CharField(max_length = 128, unique=True)

	def __unicode__(self) :
		return self.name
'''

'''
class Female(models.Model) :
	name = models.CharField(max_length = 128)
	sex = models.CharField(max_length = 2)
	age = models.IntegerField(default=0)
	education = models.CharField(max_length=128)
	Occupation = models.CharField(max_length=128)
	height = models.IntegerField(default=0)
	weight = models.IntegerField(default=0)
	BJHouseholds = models.BooleanField(default = False)
	car =  models.BooleanField(default = False)
	house = models.BooleanField(default = False)
	hometown = models.CharField(max_length=1024)
	require = models.CharField(max_length=8096)
	flag = models.BooleanField(default = False)
	WxNo = models.CharField(max_length=128)
	img = models.ImageField(upload_to='Female', blank=True)
	message = models.CharField(max_length=8096)
	QqNo = models.CharField(max_length = 128)
	location = models.CharField(max_length = 1024)
	Character = models.CharField(max_length = 128)
	views = models.IntegerField(default=0)
	synopsis = models.CharField(max_length=128)

	def __unicode__(self) :
		return self.name

class Man(models.Model) :
	name = models.CharField(max_length = 128)
	sex = models.CharField(max_length = 2)
	age = models.IntegerField(default=0)
	education = models.CharField(max_length=128)
	Occupation = models.CharField(max_length=128)
	height = models.IntegerField(default=0)
	weight = models.IntegerField(default=0)
	BJHouseholds = models.BooleanField(default = False)
	car =  models.BooleanField(default = False)
	house = models.BooleanField(default = False)
	hometown = models.CharField(max_length=1024)
	require = models.CharField(max_length=8096)
	flag = models.BooleanField(default = False)
	WxNo = models.CharField(max_length=128)
	img = models.ImageField(upload_to='man', blank=True)
	message = models.CharField(max_length=8096)
	QqNo = models.CharField(max_length = 128)
	location = models.CharField(max_length = 1024)
	Character = models.CharField(max_length = 128)
	views = models.IntegerField(default=0)
	synopsis = models.CharField(max_length=128)

	def __unicode__(self) :
		return self.name
'''
