from django import forms
from PatientPortal.models import Site

class AnalyticsQueryForm(forms.Form):
    Group_1_Min_Age = forms.IntegerField()
    Group_1_Max_Age = forms.IntegerField()
    Group_1_Sites = forms.ModelMultipleChoiceField(queryset=Site.objects.all())
    Group_2_Min_Age = forms.IntegerField()
    Group_2_Max_Age = forms.IntegerField()
    Group_2_Sites = forms.ModelMultipleChoiceField(queryset=Site.objects.all())

    #def send_email(self):
        # send email using the self.cleaned_data dictionary
    #    pass
