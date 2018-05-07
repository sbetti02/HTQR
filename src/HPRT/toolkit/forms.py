# Toolkit/forms.py
from django import forms
from . models import HTQ
import json, os


class HTQQuestionForm(forms.ModelForm):

    class Meta:
        model = HTQ
        fields = '__all__'
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')   
        htq_list = json.load(json_data)[0]['questions']
        for index in htq_list:
            labels[index['id']] = index['body']
        json_data.close()
