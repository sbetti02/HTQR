from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . models import Patient


class PatientListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'home.html'

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
    success_url = reverse_lazy('home')

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

