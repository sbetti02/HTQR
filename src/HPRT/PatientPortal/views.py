from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . models import Patient, DocPat, Site


class PatientListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'home.html'
    def get_queryset(self):
        return Patient.objects.filter(docpat__doctor__pk = self.request.user.pk)

class PatientDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'patient_detail.html'


class PatientCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'patient_new.html'
    fields = '__all__'
    def get_success_url(self):
        temp = DocPat(doctor = self.request.user, patient = self.object)
        temp.save()
        return reverse_lazy('patient_detail', kwargs={'pk' : self.object.pk})


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    fields = '__all__'
    template_name = 'patient_edit.html'
    success_url = ".."

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'patient_delete.html'
    success_url = reverse_lazy('home')

class SiteCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.user_type == 'A' or self.request.user.is_superuser
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Site
    template_name = 'site_new.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

