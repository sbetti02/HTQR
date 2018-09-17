from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . forms import HTQForm, DSMVForm, TortureHistoryForm, HopkinsPart1Form, HopkinsPart2Form
from . models import Toolkit, HTQ, DSMV, TortureHistory, HopkinsPart1, HopkinsPart2
from PatientPortal.models import Patient
import json, os
from datetime import date  
from django.http import HttpResponse

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus.tables import Table, TableStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

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

    def get_queryset(self):
        return HTQ.objects.filter(patient=Patient.objects.filter(pk=self.kwargs['pk'])[0])

class HTQCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HTQ
    template_name = 'htq_new.html'
    form_class = HTQForm

    def get_success_url(self):
        return reverse_lazy('screenings', kwargs={'pk' : self.object.patient.pk})

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        form.instance.date = date.today()
        form.instance.patient = Patient.objects.get(pk=self.kwargs['pk'])
        return super(HTQCreateView, self).form_valid(form)


class HTQDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HTQ
    template_name = 'htq_detail.html'

    def get_context_data(self, **kwargs):
        print("HERE")
        kwargs = super(HTQDetailView, self).get_context_data(**kwargs)
        """
        labels = {}

        json_data = open(os.path.join('static', "questions.json"), 'r')
        htq_list = json.load(json_data)[0]['questions']
        i = 1
        for index in htq_list:
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()

        json_data = open(os.path.join('static', "questions.json"), 'r')
        pd = json.load(json_data)[1]['questions']
        i = 1
        for index in pd:
            labels[index['id']] = 'Personal Description ' + str(i) + '. ' + index['body']
            i+=1
        json_data.close()

        json_data = open(os.path.join('static', "questions.json"), 'r')
        hi = json.load(json_data)[2]['questions']
        i = 1
        for index in hi:
            labels[index['id']] = 'Injury ' + str(i) + '. ' + index['body']
            j = 1 
            for part in index['dropdown']:
                if i == 5:
                    key = index['id'][:-1] + '_' + chr(96 + j)
                else:
                    key = index['id'] + '_' + chr(96 + j)
                labels[key] = chr(96 + j) + '. ' + part['body']
                j+=1 
            i+=1
        json_data.close()
        print(self.object)
        print(labels)
        """
        """
        kwargs.update({
            zipped_label_res =  zip(labels, self.object)
            'labels': labels,
        })
        """

        return kwargs


class DSMVCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = DSMV
    template_name = 'dsmv_new.html'
    form_class = DSMVForm   

    def get_success_url(self):
        return reverse_lazy('screenings', kwargs={'pk' : self.object.patient.pk})

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        form.instance.date = date.today()
        form.instance.patient = Patient.objects.get(pk=self.kwargs['pk'])
        total_score = 0
        len(form.cleaned_data)
        for label in form.cleaned_data:
            total_score += form.cleaned_data[label]
        form.instance.score = float(total_score)/len(form.cleaned_data)
        return super(DSMVCreateView, self).form_valid(form)



class TortureHistoryCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = TortureHistory
    template_name = 'th_new.html'
    form_class = TortureHistoryForm

    def get_success_url(self):
        return reverse_lazy('screenings', kwargs={'pk' : self.object.patient.pk})

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        form.instance.date = date.today()
        form.instance.patient = Patient.objects.get(pk=self.kwargs['pk'])
        return super(TortureHistoryCreateView, self).form_valid(form)


class HopkinsPart1CreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HopkinsPart1
    template_name = 'hp1_new.html'
    form_class = HopkinsPart1Form

    def get_success_url(self):
        return reverse_lazy('screenings', kwargs={'pk' : self.object.patient.pk})

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        form.instance.date = date.today()
        form.instance.patient = Patient.objects.get(pk=self.kwargs['pk'])
        total_score = 0
        for label in form.cleaned_data:
            total_score += form.cleaned_data[label]
        form.instance.score = float(total_score)/len(form.cleaned_data)
        return super(HopkinsPart1CreateView, self).form_valid(form)


class HopkinsPart2CreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HopkinsPart2
    template_name = 'hp2_new.html'
    form_class = HopkinsPart2Form

    def get_success_url(self):
        return reverse_lazy('screenings', kwargs={'pk' : self.object.patient.pk})

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        form.instance.date = date.today()
        form.instance.patient = Patient.objects.get(pk=self.kwargs['pk'])
        total_score = 0
        for label in form.cleaned_data:
            total_score += form.cleaned_data[label]
        form.instance.score = float(total_score)/len(form.cleaned_data)
        return super(HopkinsPart2CreateView, self).form_valid(form)


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

# Purpose: creates PDF with arguments provided
# Arguments: HTTP response, info gathered from questionnaire and questions from questionnaire
# 
def make_pdf(response, info, questions):
    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()
    info_style = ParagraphStyle(name='Normal', fontName='Times-Bold', fontSize=13,)

    parts = [] # holds interable parts of document used in build()
    # Header
    parts.append(Paragraph(
            "HPRT", 
            ParagraphStyle(name='Normal', fontName='Helvetica-Oblique', fontSize=20,)
            ))
    parts.append(Spacer(1, 0.2 * inch))
    # Patient, Doctor and Date
    parts.append(Paragraph("Patient Name: " + info["patient"], info_style))
    parts.append(Paragraph("Doctor Administered: Dr. " + info["doctor"], info_style))
    parts.append(Paragraph("Date Administered: " + info["date"], info_style))
    parts.append(Spacer(1, 0.2 * inch))
    # Formatting questions and answers
    para_questions = []
    for [question, answer] in questions:
        para_questions.append([Paragraph(question, styles['Normal']), Paragraph(str(answer), styles['Normal'])])
    # Populating and formatting table
    t = Table(para_questions, colWidths=3*inch)
    t.setStyle(TableStyle([
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ]))
    # Adding finished table to parts
    parts.append(t)
    # If the questionnaire was scored, score will be added
    if "score" in info:
        parts.append(Spacer(1, 0.2 * inch))
        parts.append(Paragraph("Total Score: " + info["score"], info_style))
    # Finally, builds pdf
    doc.build(parts)


class HTQPDF(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HTQ
    def get(self, request, pk):
        response = HttpResponse(content_type='application/pdf')
        obj = HTQ.objects.get(pk=pk)
        response['Content-Disposition'] = 'attachment; filename=HTQ_'+ str(obj.patient.name) + '_' + str(obj.date)

        info = {"patient": obj.patient.name, "doctor": obj.doctor.first_name + obj.doctor.last_name, "date": str(obj.date)}
        labels = obj.get_labels()
        questions = []
        for field, val in obj:
            if field in labels:
                questions.append([labels[field], val])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        make_pdf(response, info, questions)

        return response

class DSMVPDF(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = DSMV
    def get(self, request, pk):
        response = HttpResponse(content_type='application/pdf')
        obj = DSMV.objects.get(pk=pk)
        response['Content-Disposition'] = 'attachment; filename=DSMV_'+ str(obj.patient.name) + '_' + str(obj.date)

        info = {"patient": obj.patient.name, "doctor": obj.doctor.last_name, "date": str(obj.date), "score": str(obj.score)}
        labels = obj.get_labels()
        questions = []
        for field, val in obj:
            if field in labels:
                questions.append([labels[field], val])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        make_pdf(response, info, questions)

        return response

class THPDF(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = TortureHistory
    def get(self, request, pk):
        response = HttpResponse(content_type='application/pdf')
        obj = TortureHistory.objects.get(pk=pk)
        response['Content-Disposition'] = 'attachment; filename=TH_'+ str(obj.patient.name) + '_' + str(obj.date)

        info = {"patient": obj.patient.name, "doctor": obj.doctor.last_name, "date": str(obj.date)}
        labels = obj.get_labels()
        questions = []
        for field, val in obj:
            if field in labels:
                questions.append([labels[field], val])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        make_pdf(response, info, questions)

        return response


class HP1PDF(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HopkinsPart1
    def get(self, request, pk):
        response = HttpResponse(content_type='application/pdf')
        obj = HopkinsPart1.objects.get(pk=pk)
        response['Content-Disposition'] = 'attachment; filename=HP1_'+ str(obj.patient.name) + '_' + str(obj.date)

        info = {"patient": obj.patient.name, "doctor": obj.doctor.last_name, "date": str(obj.date), "score": str(obj.score)}
        labels = obj.get_labels()
        questions = []
        for field, val in obj:
            if field in labels:
                questions.append([labels[field], val])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        make_pdf(response, info, questions)

        return response

class HP2PDF(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = HopkinsPart2
    def get(self, request, pk):
        response = HttpResponse(content_type='application/pdf')
        obj = HopkinsPart2.objects.get(pk=pk)
        response['Content-Disposition'] = 'attachment; filename=HP2_'+ str(obj.patient.name) + '_' + str(obj.date)

        info = {"patient": obj.patient.name, "doctor": obj.doctor.last_name, "date": str(obj.date), "score": str(obj.score)}
        labels = obj.get_labels()
        questions = []
        for field, val in obj:
            if field in labels:
                questions.append([labels[field], val])

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        make_pdf(response, info, questions)

        return response
