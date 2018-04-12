from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.edit import FormView
from django.views.generic import ListView
from Analytics.forms import AnalyticsQueryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from PatientPortal.models import Patient




# Create your views here.

class AnalyticQueryView(LoginRequiredMixin, FormView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    template_name = 'analytics_home.html'
    form_class = AnalyticsQueryForm
    #success_url = '/results/'

    def get_success_url(self):
        #temp = DocPat(doctor = self.request.user, patient = self.object)
        #temp.save()
        #print(self.object)
        return reverse('analytics_results') #kwargs={'pk' : self.object.pk})


    def form_valid(self, form):
        # Do stuff with valid form
        return super().form_valid(form)
        #return HttpResponse("Hi")

    def form_invalid(self, form):
        return reverse('analytics_results')




class AnalyticResultsView(LoginRequiredMixin, ListView):
    template_name = 'analytics_results.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    def get_queryset(self):
        return Patient.objects.filter(docpat__doctor__pk = self.request.user.pk)

