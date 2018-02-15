from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import Patient

class PatientListView(ListView):
    model = Patient
    template_name = 'home.html'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'patient_new.html'
    fields = '__all__'

# class PatientUpdateView(UpdateView):
#     model = Patient
#     fields = '__all__'
#     template_name = 'patient_edit.html'

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient_delete.html'
    success_url = reverse_lazy('home')