# Toolkit/forms.py
from django import forms
from . models import HTQ, DSMV, TortureHistory, HopkinsPart1, HopkinsPart2, GeneralHealth
import json, os

class HTQForm(forms.ModelForm):

    class Meta:
        model = HTQ
        exclude = ('patient', 'doctor')

        labels = {}
        labels['date'] = 'Date (YYYY-MM-DD)'

        json_data = open(os.path.join('static', "questions.json"), 'r')
        htq_list = json.load(json_data)[0:3]
        # HTQ questions
        for i, index in enumerate(htq_list[0]['questions'],start=1):
            labels[index['id']] = str(i) + '. ' + index['body']
        # Personal Description questions
        for i, index in enumerate(htq_list[1]['questions'],start=1):
            labels[index['id']] = 'Personal Description ' + str(i) + '. ' + index['body']
        # Injury questions
        for i, index in enumerate(htq_list[2]['questions'],start=1):
            labels[index['id']] = 'Injury ' + str(i) + '. ' + index['body']
            for j, part in enumerate(index['dropdown'],start=1):
                if i == 5:
                    key = index['id'][:-1] + '_' + chr(96 + j)
                else:
                    key = index['id'] + '_' + chr(96 + j)
                labels[key] = chr(96 + j) + '. ' + part['body']
        json_data.close()

class DSMVForm(forms.ModelForm):
    class Meta:
        model = DSMV
        exclude = ('patient', 'doctor', 'score')
        labels = {}
        labels['date'] = 'Date (YYYY-MM-DD)'
        widgets = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        dsmv_list = json.load(json_data)[5]['questions']
        for i, index in enumerate(dsmv_list,start=1):
            widgets[index['id']] = forms.RadioSelect()
            labels[index['id']] = str(i) + '. ' + index['body']
        json_data.close()

class TortureHistoryForm(forms.ModelForm):

    class Meta:
        model = TortureHistory
        exclude = ('patient', 'doctor')
        labels = {}
        labels['date'] = 'Date (YYYY-MM-DD)'
        json_data = open(os.path.join('static', "questions.json"), 'r')
        th_list = json.load(json_data)[6]['questions']
        for i, index in enumerate(th_list, start=1):
            labels[index['id']] = str(i) + '. ' + index['body']
        json_data.close()

class HopkinsPart1Form(forms.ModelForm):

    class Meta:
        model = HopkinsPart1
        exclude = ('patient', 'doctor', 'score')
        labels = {}
        labels['date'] = 'Date (YYYY-MM-DD)'
        widgets = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        hp1_list = json.load(json_data)[7]['questions']
        for i, index in enumerate(hp1_list, start=1):
            widgets[index['id']] = forms.RadioSelect()
            labels[index['id']] = str(i) + '. ' + index['body']
        json_data.close()

class HopkinsPart2Form(forms.ModelForm):

    class Meta:
        model = HopkinsPart2
        exclude = ('patient', 'doctor', 'score')
        labels = {}
        labels['date'] = 'Date (YYYY-MM-DD)'
        widgets = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        hp2_list = json.load(json_data)[8]['questions']
        for i, index in enumerate(hp2_list, start=11):
            widgets[index['id']] = forms.RadioSelect()
            labels[index['id']] = str(i) + '. ' + index['body']
        json_data.close()

class GeneralHealthForm(forms.ModelForm):
    """ Abstract model of General Health/Physical Functioning questionnaire form """
    class Meta:
        """ Information passed into the process of creating object """
        model = GeneralHealth
        exclude = ('patient', 'doctor', 'score')
        labels = {}
        labels['date'] = 'Date (YYYY-MM-DD)'
        widgets = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        gh_list = json.load(json_data)[9]['questions']
        for i, index in enumerate(gh_list, start=1):
            labels[index['id']] = str(i) + '. ' + index['body']
        json_data.close()
