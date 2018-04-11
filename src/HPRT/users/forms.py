# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Doctor

class DoctorCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Doctor
        fields = ('user_type', 'username', 'first_name', 'last_name', 'email')

class DoctorChangeForm(UserChangeForm):

    class Meta:
        model = Doctor
        fields = ('user_type', 'username', 'first_name', 'last_name', 'email')