from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . models import Toolkit, HTQ, DSMV, TortureHistory, HopkinsPart1, HopkinsPart2
from PatientPortal.models import Patient


class ToolkitDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    template_name = 'toolkit_detail.html'

class ToolkitUpdateAskView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    fields = ['ask']
    template_name = 'toolkit_ask.html'
    def get_success_url(self):
        return reverse_lazy('toolkit_detail', kwargs={'pk' : self.object.pk})

class ToolkitUpdateIdentifyView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    fields = ['identify']
    template_name = 'toolkit_identify.html'
    def get_success_url(self):
        return reverse_lazy('toolkit_detail', kwargs={'pk' : self.object.pk})

class ToolkitUpdateDiagTreatView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    fields = ['diagnose_and_treat']
    template_name = 'toolkit_diagtreat.html'
    def get_success_url(self):
        return reverse_lazy('toolkit_detail', kwargs={'pk' : self.object.pk})

class ToolkitUpdateReferView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    fields = ['refer']
    template_name = 'toolkit_refer.html'
    def get_success_url(self):
        return reverse_lazy('toolkit_detail', kwargs={'pk' : self.object.pk})

class ToolkitUpdateReinTeachView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    fields = ['reinforce_and_teach']
    template_name = 'toolkit_reinteach.html'
    def get_success_url(self):
        return reverse_lazy('toolkit_detail', kwargs={'pk' : self.object.pk})

class ToolkitUpdateRecommendView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    fields = ['recommend']
    template_name = 'toolkit_recommend.html'
    def get_success_url(self):
        return reverse_lazy('toolkit_detail', kwargs={'pk' : self.object.pk})

class ToolkitUpdateReduceRiskView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    fields = ['reduce_high_risk_behavior']
    template_name = 'toolkit_reducerisk.html'
    def get_success_url(self):
        return reverse_lazy('toolkit_detail', kwargs={'pk' : self.object.pk})

class ToolkitUpdateCulturalView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    fields = ['be_culturally_attuned']
    template_name = 'toolkit_culture.html'
    def get_success_url(self):
        return reverse_lazy('toolkit_detail', kwargs={'pk' : self.object.pk})

class ToolkitUpdatePrescribeView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    fields = ['prescribe']
    template_name = 'toolkit_prescribe.html'
    def get_success_url(self):
        return reverse_lazy('toolkit_detail', kwargs={'pk' : self.object.pk})

class ToolkitUpdateCloseView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    fields = ['close_and_schedule']
    template_name = 'toolkit_close.html'
    def get_success_url(self):
        return reverse_lazy('toolkit_detail', kwargs={'pk' : self.object.pk})

class ToolkitUpdateBurnoutView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Toolkit
    fields = ['prevent_burnout']
    template_name = 'toolkit_burnout.html'
    def get_success_url(self):
        return reverse_lazy('toolkit_detail', kwargs={'pk' : self.object.pk})

class ScreeningsListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HTQ
    template_name = 'screenings.html'
    def get_context_data(self, **kwargs):
        kwargs = super(ScreeningsListView, self).get_context_data(**kwargs)
        kwargs.update({
            'patient': self.kwargs['pk'],
            'dsmv_list': DSMV.objects.filter(patient = Patient.objects.filter(pk = self.kwargs['pk'])[0] ),
            'th_list': TortureHistory.objects.filter(patient = Patient.objects.filter(pk = self.kwargs['pk'])[0] ),
            'hp1_list': HopkinsPart1.objects.filter(patient = Patient.objects.filter(pk = self.kwargs['pk'])[0] ),
            'hp2_list': HopkinsPart2.objects.filter(patient = Patient.objects.filter(pk = self.kwargs['pk'])[0] ),
        })
        return kwargs

class HTQCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HTQ
    template_name = 'htq_new.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('screenings', kwargs={'pk' : self.object.patient.pk})

class DSMVCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = DSMV
    template_name = 'dsmv_new.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('screenings', kwargs={'pk' : self.object.patient.pk})

class TortureHistoryCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = TortureHistory
    template_name = 'th_new.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('screenings', kwargs={'pk' : self.object.patient.pk})

class HopkinsPart1CreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HopkinsPart1
    template_name = 'hp1_new.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('screenings', kwargs={'pk' : self.object.patient.pk})

class HopkinsPart2CreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HopkinsPart2
    template_name = 'hp2_new.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('screenings', kwargs={'pk' : self.object.patient.pk})

class HTQDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HTQ
    template_name = 'htq_detail.html'

class DSMVDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = DSMV
    template_name = 'dsmv_detail.html'

class TortureHistoryDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = TortureHistory
    template_name = 'th_detail.html'

class HopkinsPart1DetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HopkinsPart1
    template_name = 'hp1_detail.html'

class HopkinsPart2DetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HopkinsPart2
    template_name = 'hp2_detail.html'


