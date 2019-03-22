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


GROUP_DEMOGRAPHIC="Group Demographic"
PATIENT_COUNT="Patient Count"
HTQ_COUNT="HTQ Count"
DSMV_COUNT="DSMV Count"
DSMV_AVG_SCORE="DSMV Avg Score"
TORTURE_HISTORY_CT="Torture History Count"
HOPKINS_P1_COUNT="Hopkins Part 1 Count"
HOPKINS_P1_AVG="Hopkins Part 1 Avg Score"
HOPKINS_P2_COUNT="Hopkins Part 2 Count"
HOPKINS_P2_AVG="Hopkins Part 2 Avg Score"

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
    def subtractYears(d, years):
        try:
            return d.replace(year = d.year - years)
        except ValueError:
            return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1)) # Leap day

    def get_context_data(self, **kwargs):
        kwargs = super(AnalyticResultsView, self).get_context_data(**kwargs)

        today = date.today()

        g1_patients = Patient.objects.all()
        g1_query = ""
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
                    g1_query += ", " + site
                else:
                    g1_query += site
                    first_site = False

        g1_HTQs = HTQ.objects.filter(patient__in=g1_patients)
        g1_DSMVs = DSMV.objects.filter(patient__in=g1_patients)
        g1_THs = TortureHistory.objects.filter(patient__in=g1_patients)
        g1_HP1s = HopkinsPart1.objects.filter(patient__in=g1_patients)
        g1_HP2s = HopkinsPart2.objects.filter(patient__in=g1_patients)

        g2_patients = Patient.objects.all()
        g2_query = ""
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

        # TODO generalize groups and columns

        columns = [
            GROUP_DEMOGRAPHIC,
            PATIENT_COUNT,
            HTQ_COUNT,
            DSMV_COUNT,
            DSMV_AVG_SCORE,
            TORTURE_HISTORY_CT,
            HOPKINS_P1_COUNT,
            HOPKINS_P1_AVG,
            HOPKINS_P2_COUNT,
            HOPKINS_P2_AVG
        ]

        # Parallel array with columns :)

        rows = [
            [
                g1_query,
                g1_patients.count(),
                g1_HTQs.count(),
                g1_DSMVs.count(),
                g1_DSMVs.aggregate(Avg('score'))['score__avg'],
                g1_THs.count(),
                g1_HP1s.count(),
                g1_HP1s.aggregate(Avg('score'))['score__avg'],
                g1_HP2s.count(),
                g1_HP2s.aggregate(Avg('score'))['score__avg'],
            ],
            [
                g2_query,
                g2_patients.count(),
                g2_HTQs.count(),
                g2_DSMVs.count(),
                g2_DSMVs.aggregate(Avg('score'))['score__avg'],
                g2_THs.count(),
                g2_HP1s.count(),
                g2_HP1s.aggregate(Avg('score'))['score__avg'],
                g2_HP2s.count(),
                g2_HP2s.aggregate(Avg('score'))['score__avg'],
            ]
        ]

        kwargs.update({
            "columns": columns,
            "rows": rows
        })
        return kwargs
