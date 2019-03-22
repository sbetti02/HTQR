from django import forms
from PatientPortal.models import Site

class AnalyticsQueryForm(forms.Form):
    Group_1_Min_Age = forms.IntegerField()
    Group_1_Max_Age = forms.IntegerField()
    Group_1_Sites = forms.ModelMultipleChoiceField(queryset=Site.objects.all())
    Group_2_Min_Age = forms.IntegerField()
    Group_2_Max_Age = forms.IntegerField()
    Group_2_Sites = forms.ModelMultipleChoiceField(queryset=Site.objects.all())

    htq_count = forms.BooleanField(initial=False, required=False)
    dsmv_count = forms.BooleanField(initial=False, required=False)
    dsmv_avg_score = forms.BooleanField(initial=False, required=False)
    torture_history_count = forms.BooleanField(initial=False, required=False)
    hopkins_pt_1_count = forms.BooleanField(initial=False, required=False)
    hopkins_pt_2_count = forms.BooleanField(initial=False, required=False)
    hopkins_pt_2_avg_score = forms.BooleanField(initial=False, required=False)
