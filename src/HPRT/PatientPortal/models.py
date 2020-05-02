from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import Doctor
from datetime import date
import datetime

#########
## TODO: Many of these fields shouldn't have null=True in production!
#########

class Site(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=6,
        default=None,
        choices=[('', "Choose one"),
                 ('Male', 'Male'),
                 ('Female', 'Female'),
                 ('Other', 'Other')])
    DOB = models.DateField(null=True)
    blood_type = models.CharField(max_length=10, null=True)
    height = models.DecimalField(
        max_digits=4, decimal_places=1, null=True)  # In centimeters
    weight = models.DecimalField(
        max_digits=4, decimal_places=1, null=True)  # In kg, max_digits non-inclusive
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    allergies = models.TextField(default='', blank=True, null=True)
    current_medications = models.TextField(default='', blank=True, null=True)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def age(self):
        today = date.today()
        return today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))

class DocPat(models.Model):
    class Meta:
        unique_together = (('doctor', 'patient'),)

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.doctor.__str__() + ": " + self.patient.name
