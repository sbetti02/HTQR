# Toolkit/forms.py
from django import forms
from . models import HTQ, DSMV, TortureHistory, HopkinsPart1, HopkinsPart2
import json, os


class HTQForm(forms.ModelForm):

    class Meta:
        model = HTQ
        fields = '__all__'
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

class DSMVForm(forms.ModelForm):

    class Meta:
        model = DSMV
        fields = '__all__'
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        dsmv_list = json.load(json_data)[5]['questions']
        i = 1
        for index in dsmv_list:
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()

class TortureHistoryForm(forms.ModelForm):

    class Meta:
        model = TortureHistory
        fields = '__all__'
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
        fields = '__all__'
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        hp1_list = json.load(json_data)[7]['questions']
        i = 1
        for index in hp1_list:
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()


class HopkinsPart2Form(forms.ModelForm):

    class Meta:
        model = HopkinsPart2
        fields = '__all__'
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        hp2_list = json.load(json_data)[8]['questions']
        i = 11
        for index in hp2_list:
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()