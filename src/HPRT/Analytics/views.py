from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.edit import FormView
from django.views.generic import ListView
from Analytics.forms import AnalyticsQueryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from PatientPortal.models import Patient
from datetime import date  






# Create your views here.

class AnalyticQueryView(LoginRequiredMixin, FormView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    template_name = 'analytics_home.html'
    form_class = AnalyticsQueryForm

    def get_success_url(self):
        return reverse('analytics_results') #kwargs={'pk' : self.object.pk})


    def form_valid(self, form):
        # Do stuff with valid form

        session_form = {}
        session_form["Group_1_Min_Age"] = form.cleaned_data["Group_1_Min_Age"]
        session_form["Group_1_Max_Age"] = form.cleaned_data["Group_1_Max_Age"]
        session_form["Group_2_Min_Age"] = form.cleaned_data["Group_2_Min_Age"]
        session_form["Group_2_Max_Age"] = form.cleaned_data["Group_2_Max_Age"]
        session_form["Group_1_Sites"] = list(form.cleaned_data["Group_1_Sites"].values_list('name', flat=True))
        session_form["Group_2_Sites"] = list(form.cleaned_data["Group_2_Sites"].values_list('name', flat=True))

        self.request.session['temp_data'] = session_form
        return super().form_valid(form)

    def form_invalid(self, form):
        return reverse('analytics_results')



class AnalyticResultsView(LoginRequiredMixin, ListView):
    template_name = 'analytics_results.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient

    @staticmethod
    def subtractYears(d, years):
        try:
            return d.replace(year = d.year - years)
        except ValueError:
            return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1)) # Leap day


    def get_queryset(self):
        today = date.today()
        print(self.request.session['temp_data'])
        g1_min = self.request.session['temp_data']["Group_1_Min_Age"]
        g1_max = self.request.session['temp_data']["Group_1_Max_Age"]
        return Patient.objects.filter(DOB__range=[self.subtractYears(today, g1_max+1), self.subtractYears(today, g1_min)])
