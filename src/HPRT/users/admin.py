# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import DoctorCreationForm, DoctorChangeForm
from .models import Doctor

class DoctorAdmin(UserAdmin):
    model = Doctor
    add_form = DoctorCreationForm
    form = DoctorChangeForm

admin.site.register(Doctor, DoctorAdmin)