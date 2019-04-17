from django.db import models

# Create your models here.
#from django.conf import settings
#from datetime import datetime

class USER_PATH(models.Model):
	userName = models.CharField(max_length=64, blank=False)
	userPath = models.CharField(max_length=256, blank=False)
	loginTime = models.CharField(max_length=1024, blank=True)
	stayingTime = models.CharField(max_length=256, blank=True)

	def __str__(self):
		return self.userName + ':' + self.userPath
