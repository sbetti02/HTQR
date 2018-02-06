from django.db import models
import datetime
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Q(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    q = models.ForeignKey(Q, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Site(models.Model):
    pass


class PatientInfo(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField()
    blood_type = models.CharField(max_length = 10)
    height = models.DecimalField(max_digits = 3, decimal_places = 1) # In centimeters
    weight = models.DecimalField(max_digits = 4, decimal_places = 1) # In kg
    campsite = models.ForeignKey(Site, on_delete = models.CASCADE)
    allergies = models.TextField()
    current_medications = models.TextField()
    phone_number = PhoneNumberField()
    email = models.EmailField()
    #picture = models.ImageField() # TODO: set height, width requirements
    # TODO: fingerprints, family 


