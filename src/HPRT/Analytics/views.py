from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.edit import FormView
from django.views.generic import ListView
from Analytics.forms import AnalyticsQueryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from PatientPortal.models import Patient
from toolkit.models import HTQ, DSMV, TortureHistory, HopkinsPart1, HopkinsPart2
from datetime import date  
from django.db.models import Avg

import datetime




# Create your views here.

class AnalyticQueryView(LoginRequiredMixin, FormView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    template_name = 'analytics_home.html'
    form_class = AnalyticsQueryForm

    def get_success_url(self):
        return reverse('analytics_results') #kwargs={'pk' : self.object.pk})


    def form_valid(self, form):
        # Do stuff with valid form

        session_form = {}
        session_form["Group_1_Min_Age"] = form.cleaned_data["Group_1_Min_Age"]
        session_form["Group_1_Max_Age"] = form.cleaned_data["Group_1_Max_Age"]
        session_form["Group_2_Min_Age"] = form.cleaned_data["Group_2_Min_Age"]
        session_form["Group_2_Max_Age"] = form.cleaned_data["Group_2_Max_Age"]
        session_form["Group_1_Sites"] = list(form.cleaned_data["Group_1_Sites"].values_list('name', flat=True))
        session_form["Group_2_Sites"] = list(form.cleaned_data["Group_2_Sites"].values_list('name', flat=True))

        self.request.session['temp_data'] = session_form
        return super().form_valid(form)

    def form_invalid(self, form):
        return reverse('analytics_results')


class AnalyticResultsView(LoginRequiredMixin, ListView):
    template_name = 'analytics_results.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient

    @staticmethod
    def get_patient_data(patient):
        scores = []
        DSMV_list = list(DSMV.objects.filter(patient=patient.id))
        DSMV_list.sort(key=lambda x: x.date)
        time_delta = datetime.timedelta(weeks=6)
        desired_date = DSMV_list[0].date
        i = 0
        while i < (len(DSMV_list)-1):
            if DSMV_list[i].date == desired_date:
                scores.append(DSMV_list[i].score)
                desired_date += time_delta
            elif DSMV_list[i].date < desired_date < DSMV_list[i+1].date:
                run = (DSMV_list[i+1].date - DSMV_list[i].date).days
                x = (desired_date - DSMV_list[i].date).days
                rise = DSMV_list[i+1].score - DSMV_list[i].score
                m = rise/run
                score = m * x + DSMV_list[i].score
                scores.append(score)
                desired_date += time_delta
            else:
                i+=1
        return scores

    @staticmethod
    def find_avg_scores(data):
        if len(data) == 0:
            return []
        data.sort(key=len, reverse=True)
        avg_scores = []
        for inner_list_i in range(0, len(data[0])):
            sum = 0
            n = 0
            for outer_list_i in range(0, len(data)):
                if inner_list_i < len(data[outer_list_i]):
                    sum += data[outer_list_i][inner_list_i]
                    n += 1
            avg_score = sum/n
            avg_scores.append(avg_score)

        return avg_scores

    @staticmethod
    def subtractYears(d, years):
        try:
            return d.replace(year = d.year - years)
        except ValueError:
            return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1)) # Leap day

    def get_context_data(self, **kwargs):
        kwargs = super(AnalyticResultsView, self).get_context_data(**kwargs)

        today = date.today()

        g1_patients = Patient.objects.all()
        g1_query = "Patients "
        if ("Group_1_Min_Age" in self.request.session['temp_data'] and 
           "Group_1_Max_Age" in self.request.session['temp_data']):
            g1_min = self.request.session['temp_data']["Group_1_Min_Age"]
            g1_max = self.request.session['temp_data']["Group_1_Max_Age"]
            g1_patients = g1_patients.filter(DOB__range=[self.subtractYears(today, g1_max+1),
                                                         self.subtractYears(today, g1_min)])
            g1_query += "Age " + str(g1_min) + " - " + str(g1_max)
        if "Group_1_Sites" in self.request.session['temp_data']:
            g1_sites = self.request.session['temp_data']['Group_1_Sites']
            g1_patients = g1_patients.filter(site__name__in=g1_sites)
            g1_query += " at "
            first_site = True
            for site in g1_sites:
                if not first_site:
                    g1_query += ", " + sit
                else:
                    g1_query += site
                    first_site = False

        g1_HTQs = HTQ.objects.filter(patient__in=g1_patients)
        g1_DSMVs = DSMV.objects.filter(patient__in=g1_patients)
        g1_THs = TortureHistory.objects.filter(patient__in=g1_patients)
        g1_HP1s = HopkinsPart1.objects.filter(patient__in=g1_patients)
        g1_HP2s = HopkinsPart2.objects.filter(patient__in=g1_patients)

        g2_patients = Patient.objects.all()
        g2_query = "Patients "
        if ("Group_2_Min_Age" in self.request.session['temp_data'] and 
           "Group_2_Max_Age" in self.request.session['temp_data']):
            g2_min = self.request.session['temp_data']["Group_2_Min_Age"]
            g2_max = self.request.session['temp_data']["Group_2_Max_Age"]
            g2_patients = g2_patients.filter(DOB__range=[self.subtractYears(today, g2_max+1),
                                                         self.subtractYears(today, g2_min)])
            g2_query += "Age " + str(g2_min) + " - " + str(g2_max)
        if "Group_2_Sites" in self.request.session['temp_data']:
            g2_sites = self.request.session['temp_data']['Group_2_Sites']
            g2_patients = g2_patients.filter(site__name__in=g2_sites)
            g2_query += " at "
            first_site = True
            for site in g2_sites:
                if not first_site:
                    g2_query += ", " + site
                else:
                    g2_query += site
                    first_site = False


        g2_HTQs = HTQ.objects.filter(patient__in=g2_patients)
        g2_DSMVs = DSMV.objects.filter(patient__in=g2_patients)
        g2_THs = TortureHistory.objects.filter(patient__in=g2_patients)
        g2_HP1s = HopkinsPart1.objects.filter(patient__in=g2_patients)
        g2_HP2s = HopkinsPart2.objects.filter(patient__in=g2_patients)

        g1_avg_data = self.find_avg_scores(list(map(self.get_patient_data, list(g1_patients))))
        g2_avg_data = self.find_avg_scores(list(map(self.get_patient_data, list(g2_patients))))
        g1_x_axis = [i * 6 for i in (list(range(0, len(g1_avg_data))))]
        g2_x_axis = [i * 6 for i in (list(range(0, len(g2_avg_data))))]

        kwargs.update({
            'Group_1_Query': g1_query,
            'Group_1_P_Count': g1_patients.count(),
            'Group_1_HTQ_Count': g1_HTQs.count(),
            'Group_1_DSMV_Count': g1_DSMVs.count(),
            'Group_1_DSMV_Avg_Score': g1_DSMVs.aggregate(Avg('score'))['score__avg'],
            'Group_1_TH_Count': g1_THs.count(),
            'Group_1_HP1_Count': g1_HP1s.count(),
            'Group_1_HP1_Avg_Score': g1_HP1s.aggregate(Avg('score'))['score__avg'],
            'Group_1_HP2_Count': g1_HP2s.count(),
            'Group_1_HP2_Avg_Score': g1_HP2s.aggregate(Avg('score'))['score__avg'],
            'Group_2_Query': g2_query,
            'Group_2_P_Count': g2_patients.count(),
            'Group_2_HTQ_Count': g2_HTQs.count(),
            'Group_2_DSMV_Count': g2_DSMVs.count(),
            'Group_2_DSMV_Avg_Score': g2_DSMVs.aggregate(Avg('score'))['score__avg'],
            'Group_2_TH_Count': g2_THs.count(),
            'Group_2_HP1_Count': g2_HP1s.count(),
            'Group_2_HP1_Avg_Score': g2_HP1s.aggregate(Avg('score'))['score__avg'],
            'Group_2_HP2_Count': g2_HP2s.count(),
            'Group_2_HP2_Avg_Score': g2_HP2s.aggregate(Avg('score'))['score__avg'],


        })
        return kwargs


