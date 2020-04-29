from django.db import models
from django.contrib.auth.models import AbstractUser

class Doctor(AbstractUser):
    USER_TYPES = (
                    ('A', 'Administrator'),
                    ('D', 'Doctor'),
                )
    user_type = models.CharField(max_length=1, choices = USER_TYPES, default = 'D')
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    specialty = models.CharField(max_length=200)
    campsite = models.ForeignKey('PatientPortal.Site', on_delete = models.CASCADE, null = True)
    email = models.EmailField()

    def __str__(self):
        return "Dr. " + self.first_name + " " + self.last_name