from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect


from twilio.twiml.messaging_response import MessagingResponse

from django.views.generic import View
from django.utils.decorators import method_decorator
# from twilio.rest import Client

# from django_twilio.decorators import twilio_view
from django.views.decorators.csrf import csrf_exempt
from . models import Patient, DocPat, Site, Doctor, Appointment, Story

from toolkit.models import Toolkit

from django.http import QueryDict
from . forms import AddExistingPatientForm, CreateNewPatientForm, AppointmentForm

import threading
import time
import datetime
from HPRT.settings import twilio_sid, twilio_auth_token, ngrok_host


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

    def get_context_data(self, **kwargs):
        context = super(PatientListView, self).get_context_data(**kwargs)
        filtered_patients = Patient.objects.filter(docpat__doctor__pk = self.request.user.pk)
        filtered_next_appts = []
        filtered_story_existance = []
        for patient in filtered_patients:
            all_appts = Appointment.objects.filter(patient__pk=patient.pk)
            patient_stories = Story.objects.filter(patient__pk=patient.pk)
            if all_appts.exists:
                filtered_next_appts.append(all_appts.last()) # Grab most recent one
            else:
                filtered_next_appts.append(None)
            filtered_story_existance.append(patient_stories.exists)
        context['zipped_row_information'] = list(zip(filtered_patients, filtered_next_appts, filtered_story_existance))
        return context

class PatientDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'patient_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        docpats = DocPat.objects.filter(doctor = self.request.user, patient = self.object)
        stories = Story.objects.filter(patient=self.object) # TODO: Filter since last appt
        if docpats.count() > 0:
            context['toolkit'] = Toolkit.objects.get(docpat = docpats[0])
        else:
            context['toolkit'] = None
        if stories.exists:
            context['stories'] = stories
        else:
            context['stories'] = None
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

class CreateApptView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Appointment
    template_name = 'new_appt.html'
    form_class = AppointmentForm

    def get_context_data(self, **kwargs):
        context = super(CreateApptView, self).get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.patient = Patient.objects.get(pk=self.kwargs['pk'])
        return super(CreateApptView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('patient_detail', kwargs={'pk' : self.object.patient.pk})
        # return HttpResponseRedirect(reverse_lazy('ask_story', kwargs={'pk' : self.object.patient.pk}))

class PatientCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient
    template_name = 'patient_new.html'
    form_class = CreateNewPatientForm

    def get_success_url(self):
        # print(self.object.phone_number)
        # client = Client(twilio_sid, twilio_auth_token)

        # t = Thread(target=twilio_validate_and_confirm,
        #            args=(twilio_client, self.object.name, self.object.phone_number))
        # t.start()

        # validation_request = client.validation_requests.create(
        #                               friendly_name=self.object.name,
        #                               phone_number=self.object.phone_number,
        #                               status_callback='http://'+ngrok_host+'/phone_verification'
        #                               )

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
        patient = Patient.objects.filter(phone_number=number)[0]
        story = Story()
        story.patient = patient
        story.comments = body
        story.date = datetime.date.today()
        story.save()
        r.message('Thank you for your submission.  Please feel free to message this number again if you would like to send more comments to your doctor before your next appointment.')
        return r


@method_decorator(csrf_exempt, name='dispatch')
class askStory(View):
    model = Patient
    # @method_decorator(twilio_view)

    def post(self, request, *args, **kwargs):
        client = Client(twilio_sid, twilio_auth_token)

        patient = Patient.objects.filter(pk=kwargs['pk'])[0]

        message = client.messages.create(
                                      body="Hi " + patient.name + ", you have an appointment coming up soon. If there is anything in particular you would like to speak with your doctor about before your next appointment, you can send comments to your doctor by responding to this text.",
                                      from_= "+17743261027",
                                      to= "+1" + patient.phone_number

                                  )
        return HttpResponseRedirect(reverse_lazy('patient_detail', kwargs={'pk' : kwargs['pk']}))


# def twilio_validate_and_confirm(twilio_client, name, phone_number):
#     validation_request = None
#     validation_request = twilio_client.validation_requests.create(
#                                   friendly_name=name,
#                                   phone_number=phone_number
#                                   )
#     while not validation_request:
#         time.sleep(1)

#     message = twilio_client.messages.create(
#                                   body="Hi " + name + ", welcome to HPRT!",
#                                   from_= "+17743261027",
#                                   to= "+1" + phone_number
#                               )

# @twilio_view
def phone_number_confirmation(request):
    """
    Callback function to confirm/deny phone number validation.
    Only expected request type is POST (from Twilio server)
    """
    print("\n\n\najafdkj\n\n")
    if request.method == 'POST':
        if request.VerificationStatus == 'success':
            message = twilio_client.messages.create(
                                  body="Hi " + name + ", welcome to HPRT!",
                                  from_= "+17743261027",
                                  to= "+1" + phone_number
                              )
        else:
            print("Failed to verify phone number.") # TODO: Update so appears as alert statement in GUI

    else:
        print("here")

    return HttpResponse("This is a simple response !")




