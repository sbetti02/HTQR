from django.contrib import admin

from .models import Patient, Doctors, Sites

admin.site.register(Patient)
admin.site.register(Doctors)
admin.site.register(Sites)

# Register your models here.
