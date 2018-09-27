# Toolkit/forms.py
from django import forms
from . models import HTQ, DSMV, TortureHistory, HopkinsPart1, HopkinsPart2, GeneralHealth
import json, os

class HTQForm(forms.ModelForm):

    class Meta:
        model = HTQ
        exclude = ('patient', 'doctor', 'date')

        labels = {}

        json_data = open(os.path.join('static', "questions.json"), 'r')
        htq_list = json.load(json_data)[0:3]
        # HTQ questions
        i = 1
        for index in htq_list[0]['questions']:
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        # Personal Description questions
        i = 1
        for index in htq_list[1]['questions']:
            labels[index['id']] = 'Personal Description ' + str(i) + '. ' + index['body']
            i+=1
        # Injury questions
        i = 1
        for index in htq_list[2]['questions']:
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

class DSMVForm(forms.ModelForm):
    class Meta:
        model = DSMV
        exclude = ('patient', 'doctor', 'date', 'score')
        labels = {}
        widgets = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        dsmv_list = json.load(json_data)[5]['questions']
        i = 1
        for index in dsmv_list:
            widgets[index['id']] = forms.RadioSelect()
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()

class TortureHistoryForm(forms.ModelForm):

    class Meta:
        model = TortureHistory
        exclude = ('patient', 'doctor', 'date')
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        th_list = json.load(json_data)[6]['questions']
        i = 1
        for index in th_list:
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()

class HopkinsPart1Form(forms.ModelForm):

    class Meta:
        model = HopkinsPart1
        exclude = ('patient', 'doctor', 'date', 'score')
        labels = {}
        widgets = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        hp1_list = json.load(json_data)[7]['questions']
        i = 1
        for index in hp1_list:
            widgets[index['id']] = forms.RadioSelect()
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()

class HopkinsPart2Form(forms.ModelForm):

    class Meta:
        model = HopkinsPart2
        exclude = ('patient', 'doctor', 'date', 'score')
        labels = {}
        widgets = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        hp2_list = json.load(json_data)[8]['questions']
        i = 11
        for index in hp2_list:
            widgets[index['id']] = forms.RadioSelect()
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()

class GeneralHealthForm(forms.ModelForm):

    class Meta:
        model = GeneralHealth
        exclude = ('patient', 'doctor', 'date', 'score')
        labels = {}
        widgets = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        gh_list = json.load(json_data)[9]['questions']
        i = 1
        for index in gh_list:
            # widgets[index['id']] = forms.RadioSelect() ### for use with Selection Grid format if preferred
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()
