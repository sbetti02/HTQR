from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect


from django.views.generic import View
from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from . models import Patient, DocPat, Site, Doctor

from toolkit.models import Toolkit

from django.http import QueryDict
from . forms import AddExistingPatientForm, CreateNewPatientForm

import threading
import time
import datetime


def update_patients(request):
    site = request.GET.get('site', None)
    doc_patients = DocPat.objects.values_list('patient', flat=True).filter(doctor=request.user)
    patient_list = list(Patient.objects.filter(site=Site.objects.get(name=site)).exclude(pk__in=set(doc_patients)).values('name'))
    return JsonResponse(patient_list, safe=False)

class PatientListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'home.html'

    def get_queryset(self):
        return Patient.objects.filter(docpat__doctor__pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(PatientListView, self).get_context_data(**kwargs)
        filtered_patients = Patient.objects.filter(docpat__doctor__pk=self.request.user.pk)
        context['patients'] = list(filtered_patients)
        return context

class PatientDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'patient_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        docpats = DocPat.objects.filter(doctor=self.request.user, patient=self.object)
        if docpats.count() > 0:
            context['toolkit'] = Toolkit.objects.get(docpat = docpats[0])
        else:
            context['toolkit'] = None
        return context

class PatientAddExistingView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = DocPat
    template_name = 'patient_add_existing.html'
    form_class = AddExistingPatientForm

    def get_success_url(self):
        tk = Toolkit(docpat = self.object)
        tk.save()
        return reverse_lazy('patient_detail', kwargs={'pk' : self.object.patient.pk})

    def get_form_kwargs(self):
        kwargs = super(PatientAddExistingView, self).get_form_kwargs()
        kwargs['doctor'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        return super(PatientAddExistingView, self).form_valid(form)

class PatientCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'patient_new.html'
    form_class = CreateNewPatientForm

    def get_success_url(self):
        temp = DocPat(doctor = self.request.user, patient = self.object)
        temp.save()
        tk = Toolkit(docpat = temp)
        tk.save()
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


class patientAdd(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    def post(self, request, *args, **kwargs):
        temp = DocPat(doctor = self.request.user, patient = Patient.objects.get(pk=kwargs['pk']))
        temp.save()
        tk = Toolkit(docpat = temp)
        tk.save()
        return HttpResponseRedirect(reverse_lazy('patient_detail', kwargs={'pk' : kwargs['pk']}))

class patientRemove(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    def post(self, request, *args, **kwargs):
        temp = DocPat.objects.filter(doctor = self.request.user, patient = Patient.objects.get(pk=kwargs['pk'])).delete()
        return HttpResponseRedirect(reverse_lazy('patient_detail', kwargs={'pk' : kwargs['pk']}))

class searchListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'search_results.html'
    def get_queryset(self):
        all_patients = super(searchListView, self).get_queryset()
        result = super(searchListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            result = result.filter(name__contains=query)
            query_list = query.split(" ")
            for q in query_list:
                result = result.union(all_patients.filter(name__contains = q))
        return result
