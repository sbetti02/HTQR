from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.edit import FormView
from django.views.generic import ListView
from Analytics.forms import AnalyticsQueryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from PatientPortal.models import Patient
from toolkit.models import HTQ, DSMV, TortureHistory, HopkinsPart1, HopkinsPart2, GeneralHealth
from datetime import date  
from django.db.models import Avg

import datetime




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
        session_form["htq_count"] = form.cleaned_data["htq_count"]
        session_form["dsmv_count"] = form.cleaned_data["dsmv_count"]
        session_form["dsmv_avg_score"] = form.cleaned_data["dsmv_avg_score"]
        session_form["torture_history_count"] = form.cleaned_data["torture_history_count"]
        session_form["hopkins_pt_1_count"] = form.cleaned_data["hopkins_pt_1_count"]
        session_form["hopkins_pt_2_count"] = form.cleaned_data["hopkins_pt_2_count"]
        session_form["hopkins_pt_2_avg_score"] = form.cleaned_data["hopkins_pt_2_avg_score"]

        self.request.session['temp_data'] = session_form
        return super().form_valid(form)

    def form_invalid(self, form):
        return reverse('analytics_results')


class AnalyticResultsView(LoginRequiredMixin, ListView):
    template_name = 'analytics_results.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Patient

    # given a list of questionnaire objects and a number of weeks, extrapolates scores for the patient at the specified intervals
    @staticmethod
    def get_patient_data(data_list, num_weeks):
        if len(data_list) == 0:
            return []
        scores = []
        data_list.sort(key=lambda x: x.date)
        time_delta = datetime.timedelta(weeks=num_weeks)
        desired_date = data_list[0].date
        i = 0
        while i < (len(data_list)-1):
            if data_list[i].date == desired_date:
                scores.append(data_list[i].score)
                desired_date += time_delta
            elif data_list[i].date < desired_date < data_list[i+1].date:
                run = (data_list[i+1].date - data_list[i].date).days
                x = (desired_date - data_list[i].date).days
                rise = data_list[i+1].score - data_list[i].score
                m = rise/run
                score = m * x + data_list[i].score
                scores.append(score)
                desired_date += time_delta
            else:
                i+=1
        return scores

    # given a list of lists, each describing a patient's scores, returns a list containing the average scores
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
            avg_score = float(sum/n)
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

        table_col_headers = [
            GROUP_DEMOGRAPHIC,
            PATIENT_COUNT
        ]

        table_rows = [
            [
                g1_query,
                g1_patients.count()
            ],
            [
                g2_query,
                g2_patients.count()
            ]
        ]

        num_weeks = 6

        g1_DSMV_avg = self.find_avg_scores(list([self.get_patient_data(x, num_weeks) for x in [list(DSMV.objects.filter(patient=x.id)) for x in list(g1_patients)]]))
        g2_DSMV_avg = self.find_avg_scores(list([self.get_patient_data(x, num_weeks) for x in [list(DSMV.objects.filter(patient=x.id)) for x in list(g2_patients)]]))
        g1_DSMV_x = [i * num_weeks for i in (list(range(0, len(g1_DSMV_avg))))]
        g2_DSMV_x = [i * num_weeks for i in (list(range(0, len(g2_DSMV_avg))))]

        g1_HP1_avg = self.find_avg_scores(list([self.get_patient_data(x, num_weeks) for x in [list(HopkinsPart1.objects.filter(patient=x.id)) for x in list(g1_patients)]]))
        g2_HP1_avg = self.find_avg_scores(list([self.get_patient_data(x, num_weeks) for x in [list(HopkinsPart1.objects.filter(patient=x.id)) for x in list(g2_patients)]]))
        g1_HP1_x = [i * num_weeks for i in (list(range(0, len(g1_HP1_avg))))]
        g2_HP1_x = [i * num_weeks for i in (list(range(0, len(g2_HP1_avg))))]

        g1_HP2_avg = self.find_avg_scores(list([self.get_patient_data(x, num_weeks) for x in [list(HopkinsPart2.objects.filter(patient=x.id)) for x in list(g1_patients)]]))
        g2_HP2_avg = self.find_avg_scores(list([self.get_patient_data(x, num_weeks) for x in [list(HopkinsPart2.objects.filter(patient=x.id)) for x in list(g2_patients)]]))
        g1_HP2_x = [i * num_weeks for i in (list(range(0, len(g1_HP2_avg))))]
        g2_HP2_x = [i * num_weeks for i in (list(range(0, len(g2_HP2_avg))))]

        g1_GH_avg = self.find_avg_scores(list([self.get_patient_data(x, num_weeks) for x in [list(GeneralHealth.objects.filter(patient=x.id)) for x in list(g1_patients)]]))
        g2_GH_avg = self.find_avg_scores(list([self.get_patient_data(x, num_weeks) for x in [list(GeneralHealth.objects.filter(patient=x.id)) for x in list(g2_patients)]]))
        g1_GH_x = [i * num_weeks6 for i in (list(range(0, len(g1_GH_avg))))]
        g2_GH_x = [i * num_weeks for i in (list(range(0, len(g2_GH_avg))))]

        htq_count = self.request.session['temp_data']['htq_count']
        dsmv_count = self.request.session['temp_data']['dsmv_count']
        dsmv_avg_score = self.request.session['temp_data']['dsmv_avg_score']
        th_count = self.request.session['temp_data']['torture_history_count']
        hp1_count = self.request.session['temp_data']['hopkins_pt_1_count']
        hp2_count = self.request.session['temp_data']['hopkins_pt_2_count']
        hp2_avg_score = self.request.session['temp_data']['hopkins_pt_2_avg_score']

        ### TODO: We NEed to delete this as soon as the demo is over
        if htq_count:
            table_col_headers.append(HTQ_COUNT)
            g1_HTQs = HTQ.objects.filter(patient__in=g1_patients)
            g2_HTQs = HTQ.objects.filter(patient__in=g2_patients)
            table_rows[0].append(g1_HTQs.count())
            table_rows[1].append(g2_HTQs.count())
        if dsmv_count:
            table_col_headers.append(DSMV_COUNT)
            g1_DSMVs = DSMV.objects.filter(patient__in=g1_patients)
            g2_DSMVs = DSMV.objects.filter(patient__in=g2_patients)
            table_rows[0].append(g1_DSMVs.count())
            table_rows[1].append(g2_DSMVs.count())
        if dsmv_avg_score:
            table_col_headers.append(DSMV_AVG_SCORE)
            g1_DSMVs = DSMV.objects.filter(patient__in=g1_patients)
            g2_DSMVs = DSMV.objects.filter(patient__in=g2_patients)
            table_rows[0].append(g1_DSMVs.aggregate(Avg('score'))['score__avg'])
            table_rows[1].append(g2_DSMVs.aggregate(Avg('score'))['score__avg'])
        if th_count:
            table_col_headers.append(TORTURE_HISTORY_CT)
            g1_THs = TortureHistory.objects.filter(patient__in=g1_patients)
            g2_THs = TortureHistory.objects.filter(patient__in=g2_patients)
            table_rows[0].append(g1_THs.count())
            table_rows[1].append(g2_THs.count())
        if hp1_count:
            table_col_headers.append(HOPKINS_P1_COUNT)
            g1_HP1s = HopkinsPart1.objects.filter(patient__in=g1_patients)
            g2_HP1s = HopkinsPart1.objects.filter(patient__in=g2_patients)
            table_rows[0].append(g1_HP1s.count())
            table_rows[1].append(g2_HP1s.count())
        if hp2_count:
            table_col_headers.append(HOPKINS_P2_COUNT)
            g1_HP2s = HopkinsPart2.objects.filter(patient__in=g1_patients)
            g2_HP2s = HopkinsPart2.objects.filter(patient__in=g2_patients)
            table_rows[0].append(g1_HP2s.count())
            table_rows[1].append(g2_HP2s.count())
        if hp2_avg_score:
            table_col_headers.append(HOPKINS_P2_AVG)
            g1_HP2s = HopkinsPart2.objects.filter(patient__in=g1_patients)
            g2_HP2s = HopkinsPart2.objects.filter(patient__in=g2_patients)
            table_rows[0].append(g1_HP2s.aggregate(Avg('score'))['score__avg'])
            table_rows[1].append(g2_HP2s.aggregate(Avg('score'))['score__avg'])

        kwargs.update({
            "columns": table_col_headers,
            "rows": table_rows,
            "DSMV_x_axes": [g1_DSMV_x, g2_DSMV_x],
            "DSMV_y_axes": [g1_DSMV_avg, g2_DSMV_avg],
            "HP1_x_axes": [g1_HP1_x, g2_HP1_x],
            "HP1_y_axes": [g1_HP1_avg, g2_HP1_avg],
            "HP2_x_axes": [g1_HP2_x, g2_HP2_x],
            "HP2_y_axes": [g1_HP2_avg, g2_HP2_avg],
            "GH_x_axes": [g1_GH_x, g2_GH_x],
            "GH_y_axes": [g1_GH_avg, g2_GH_avg]
        })
        return kwargs
