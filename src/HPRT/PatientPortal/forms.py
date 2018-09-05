# PatientPortal/forms.py
from django import forms
from . models import Patient, DocPat, Doctor, Site, Appointment


class AddExistingPatientForm(forms.ModelForm):

    site = forms.ModelChoiceField(
        queryset=Site.objects.all(),
        to_field_name = "name",
        )

    class Meta:
        model = DocPat
        fields = ['site', 'patient']

    def __init__(self, *args, **kwargs):
        doctor = kwargs.pop('doctor')
        super(AddExistingPatientForm, self).__init__(*args, **kwargs)
        self.fields['site'].initial = doctor.campsite
        patient_list = DocPat.objects.values_list('patient', flat=True).filter(doctor=doctor)
        self.fields['patient'].queryset = Patient.objects.filter(site=doctor.campsite).exclude(pk__in=set(patient_list))

class CreateNewPatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        exclude = ['ask_story']
        # widgets = {'DOB': forms.DateInput(attrs={'id': 'datetimepicker12'})}

    def __init__(self, *args, **kwargs):
        super(CreateNewPatientForm, self).__init__(*args, **kwargs)
        # self.fields['DOB'].widget.attrs['class'] = 'datepicker'
        self.fields['height'].widget.attrs['placeholder'] = 'Enter in cm'
        self.fields['weight'].widget.attrs['placeholder'] = 'Enter in kg'
        self.fields['DOB'].label = "Date of Birth (mm/dd/yyyy)"

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['appt_time']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
