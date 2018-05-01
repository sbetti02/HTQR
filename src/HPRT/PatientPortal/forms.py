# PatientPortal/forms.py
from django import forms
from . models import Patient, DocPat, Doctor

class AddExistingPatientForm(forms.ModelForm):
    class Meta:
        model = DocPat
        fields = ['patient']

    def __init__(self, *args, **kwargs):
        doctor = kwargs.pop('doctor')
        super(AddExistingPatientForm, self).__init__(*args, **kwargs)
        PatientList = DocPat.objects.values_list('patient', flat=True).filter(doctor=doctor)
        self.fields['patient'].queryset = Patient.objects.exclude(pk__in=set(PatientList))
