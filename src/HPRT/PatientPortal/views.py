from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect


#from twilio.twiml.messaging_response import MessagingResponse

from django.views.generic import View
from django.utils.decorators import method_decorator
# from twilio.rest import Client

# from django_twilio.decorators import twilio_view
from django.views.decorators.csrf import csrf_exempt
from . models import Patient, DocPat, Site, Doctor

from toolkit.models import Toolkit

from django.http import QueryDict
from . forms import AddExistingPatientForm


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
        return Patient.objects.filter(docpat__doctor__pk = self.request.user.pk)

class PatientDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'patient_detail.html'
    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        docpats = DocPat.objects.filter(doctor = self.request.user, patient = self.object)
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
    fields = ['name', 'DOB', 'blood_type', 'height', 'weight', 'site', 'phone_number', 'email', 'allergies', 'current_medications']
    def get_success_url(self):
        print(self.object.phone_number)
        account_sid = 'ACc98959cdcde7e6833b8bc683e5fca5c3'
        auth_token = '05a2c0d38c131a9c50423ec576343dd5'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                      body="Hi " + self.object.name + ", welcome to HPRT!",
                                      from_= "+17743261027",
                                      to= "+1" + self.object.phone_number

                                  )
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


@method_decorator(csrf_exempt, name='dispatch')
class smsResponse(View):
    # @method_decorator(twilio_view)

    def post(self, request):
        body = QueryDict(request.body)['Body']
        number = QueryDict(request.body)['From'][2:]
        r = MessagingResponse()
        if "y" in body.lower():
            patient = Patient.objects.filter(phone_number = number)[0]
            while patient.ask_story == False:
                patient.ask_story = True
                patient.save(update_fields=["ask_story"])
                patient = Patient.objects.filter(phone_number = number)[0]
            r.message('Thank you, your doctor will ask you about your trauma event when you are visiting.')
        elif "n" in body.lower():
            patient = Patient.objects.filter(phone_number = number)[0]
            while patient.ask_story == True:
                patient.ask_story = False
                patient.save(update_fields=["ask_story"])
                patient = Patient.objects.filter(phone_number = number)[0]
            r.message('Thank you. Please feel free to text yes to this number whenever you are ready to tell your doctor your trauma story.')
        else:
            r.message('Response is not understood. Please text yes or no. Would you like to tell your doctor about your trauma story?')
        return r


@method_decorator(csrf_exempt, name='dispatch')
class askStory(View):
    model = Patient
    # @method_decorator(twilio_view)

    def post(self, request, *args, **kwargs):
        account_sid = 'ACc98959cdcde7e6833b8bc683e5fca5c3'
        auth_token = '05a2c0d38c131a9c50423ec576343dd5'
        client = Client(account_sid, auth_token)

        patient = Patient.objects.filter(pk=kwargs['pk'])[0]

        message = client.messages.create(
                                      body="Hi " + patient.name + ", you have an appointment coming up soon. Would you like to talk to your doctor about your trauma story?",
                                      from_= "+17743261027",
                                      to= "+1" + patient.phone_number

                                  )
        return HttpResponseRedirect(reverse_lazy('patient_detail', kwargs={'pk' : kwargs['pk']}))






