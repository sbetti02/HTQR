from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . models import Patient, DocPat, Site, Doctor

from toolkit.models import Toolkit

from . forms import AddExistingPatientForm


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
    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        context['toolkit'] = Toolkit.objects.get(docpat = DocPat.objects.get(doctor = self.request.user, patient = self.object))
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
    fields = '__all__'
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

# class ToolkitDetailView(LoginRequiredMixin, DetailView):
#     login_url = 'login'
#     redirect_field_name = 'redirect_to'
#     model = Toolkit
#     template_name = 'toolkit_detail.html'



