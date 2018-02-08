from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Sites(models.Model):
    name = models.CharField(max_length=200, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    # TODO: Inventory of items

    def __str__(self):
        return self.name


class Doctors(models.Model):
    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)
    campsite = models.ForeignKey(Sites, on_delete = models.CASCADE, null=True)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    # profile_picture = models.ImageField() # TODO: height, width requirements
    # TODO: fingerprints

    def __str__(self):
        return self.name


class PatientInfo(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)
    blood_type = models.CharField(max_length = 10, null=True)
    height = models.DecimalField(max_digits = 3, decimal_places = 1, null=True) # In centimeters
    weight = models.DecimalField(max_digits = 4, decimal_places = 1, null=True) # In kg
    campsite = models.ForeignKey(Sites, on_delete = models.CASCADE, null=True)
    allergies = models.TextField(default='')
    current_medications = models.TextField(default='')
    phone_number = PhoneNumberField()
    email = models.EmailField()
    doctor = models.ForeignKey(Doctors, on_delete = models.CASCADE, null=True) # How doctor instance finds all patients
    #picture = models.ImageField() # TODO: set height, width requirements
    # TODO: fingerprints, family 

    def __str__(self):
        return self.name

class Relatives(models.Model):
    person = models.ForeignKey(PatientInfo, related_name="person1", on_delete=models.CASCADE)
    related_to = models.ForeignKey(PatientInfo, related_name="person2", on_delete=models.CASCADE)
    relation = models.PositiveSmallIntegerField(null=True)

