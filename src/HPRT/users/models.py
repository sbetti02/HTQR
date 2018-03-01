from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	USER_TYPES = (
					('A', 'Administrator'),
					('D', 'Doctor'),
				)
	user_type = models.CharField(max_length=1, choices = USER_TYPES, default = 'D')
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	specialty = models.CharField(max_length = 100)
	site = models.CharField(max_length = 100)
