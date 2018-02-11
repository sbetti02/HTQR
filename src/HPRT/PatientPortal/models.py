from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

#########
## TODO: Many of these fields shouldn't have null=True in production!
#########

## TODO: Write API that runs on top of this base model layer to be able to interact
##       with the models appropriately

class Sites(models.Model):
    name = models.CharField(max_length=200, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return self.name

class Drug_Storage(models.Model):
    drug_name = models.CharField(max_length=100)
    concentration = models.CharField(max_length=10) # Like 88mcg
    quantity = models.IntegerField(default=1)
    campsite = models.ForeignKey(Sites, on_delete=models.CASCADE)

    def __str__(self):
        return self.drug_name

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
    height = models.DecimalField(max_digits = 4, decimal_places = 1, null=True) # In centimeters
    weight = models.DecimalField(max_digits = 4, decimal_places = 1, null=True) # In kg, max_digits non-inclusive
    campsite = models.ForeignKey(Sites, on_delete = models.CASCADE, null=True)
    allergies = models.TextField(default='')
    current_medications = models.TextField(default='')
    phone_number = PhoneNumberField()
    email = models.EmailField()
    doctor = models.ForeignKey(Doctors, on_delete = models.CASCADE, null=True) # How doctor instance finds all patients
    picture = models.ImageField(upload_to="PatientPortal/profiles.py", 
                                height_field=500, width_field=500, null=True)
    # TODO: fingerprints, picture

    def __str__(self):
        return self.name

# TODO: Does this still implicitly create an ID column? I don't want it to 
class RelativeRelationships(models.Model):
    relationship_num = models.PositiveSmallIntegerField(primary_key=True)
    relationship_type = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.relationship_num) + " - " + self.relationship_type


# TODO: On add/alter, add/alter reverse relationship as well
class Relatives(models.Model):
    person = models.ForeignKey(PatientInfo, related_name="person1", on_delete=models.CASCADE)
    related_to = models.ForeignKey(PatientInfo, related_name="person2", on_delete=models.CASCADE)
    relation = models.ForeignKey(RelativeRelationships, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.name + " => " + self.related_to.name + ", " + self.relation.relationship_type


# TODO: Probably should alter these fields to more appropriate values
class DoctorAppointments(models.Model):
    patient = models.ForeignKey(PatientInfo, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    systolic_blood_pressure = models.IntegerField(null=True)
    diastolic_blood_pressure = models.IntegerField(null=True)
    tempurature = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    doctor_notes = models.TextField(default='')
