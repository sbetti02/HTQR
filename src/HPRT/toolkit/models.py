from django.db import models
from PatientPortal.models import DocPat, Patient, Doctor
import json, os


################################################
# TODO: Each of these instances of (ask, identify, etc) should be its own table
#       linked to by Toolkit to allow for inclusion the last time an item was
#       read over (extra metadata) as well as for you to get the history of all
#       the times something has been filled out, and what the responses were,
#       if applicable
################################################

class Toolkit(models.Model):
    def answer_default():
        return False

    docpat = models.ForeignKey(DocPat, on_delete = models.CASCADE) # Not unique Identifier
    ask = models.BooleanField(default=answer_default)
    identify = models.BooleanField(default=answer_default)
    diagnose_and_treat = models.BooleanField(default=answer_default)
    refer = models.BooleanField(default=answer_default)
    reinforce_and_teach = models.BooleanField(default=answer_default)
    recommend = models.BooleanField(default=answer_default)
    reduce_high_risk_behavior = models.BooleanField(default=answer_default)
    be_culturally_attuned = models.BooleanField(default=answer_default)
    prescribe = models.BooleanField(default=answer_default)
    close_and_schedule = models.BooleanField(default=answer_default)
    prevent_burnout = models.BooleanField(default=answer_default)

    def __iter__(self):
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)


class HTQ(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    date = models.DateField()
    te1 = models.BooleanField()
    te2 = models.BooleanField()
    te3 = models.BooleanField()
    te4 = models.BooleanField()
    te5 = models.BooleanField()
    te6 = models.BooleanField()
    te7 = models.BooleanField()
    te8 = models.BooleanField()
    te9 = models.BooleanField()
    te10 = models.BooleanField()
    te11 = models.BooleanField()
    te12 = models.BooleanField()
    te13 = models.BooleanField()
    te14 = models.BooleanField()
    te15 = models.BooleanField()
    te16 = models.BooleanField()
    te17 = models.BooleanField()
    te18 = models.BooleanField()
    te19 = models.BooleanField()
    te20 = models.BooleanField()
    te21 = models.BooleanField()
    te22 = models.BooleanField()
    te23 = models.BooleanField()
    te24 = models.BooleanField()
    te25 = models.BooleanField()
    te26 = models.BooleanField()
    te27 = models.BooleanField()
    te28 = models.BooleanField()
    te29 = models.BooleanField()
    te30 = models.BooleanField()
    te31 = models.BooleanField()
    te32 = models.BooleanField()
    te33 = models.BooleanField()
    te34 = models.BooleanField()
    te35 = models.BooleanField()
    te36 = models.BooleanField()
    te37 = models.BooleanField()
    te38 = models.BooleanField()
    te39 = models.BooleanField()
    te40 = models.BooleanField()
    te41 = models.TextField(default = '')
   
    pd1 = models.TextField(default = '')
    pd2 = models.TextField(default = '')

    hi1 = models.BooleanField()
    hi1_a = models.NullBooleanField()
    hi1_b = models.DurationField()
    hi2 = models.BooleanField()
    hi2_a = models.NullBooleanField()
    hi2_b = models.DurationField()
    hi3 = models.BooleanField()
    hi3_a = models.NullBooleanField()
    hi3_b = models.DurationField()
    hi4 = models.BooleanField()
    hi4_a = models.NullBooleanField()
    hi4_b = models.DurationField()
    hi5 = models.BooleanField()
    hi_a = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    hi_b = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    hi_c = models.BooleanField()

    def __iter__(self):
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def get_labels(self):
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
        return labels


class DSMV(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    date = models.DateField()
    d1 = models.IntegerField()
    d2 = models.IntegerField()
    d3 = models.IntegerField()
    d4 = models.IntegerField()
    d5 = models.IntegerField()
    d6 = models.IntegerField()
    d7 = models.IntegerField()
    d8 = models.IntegerField()
    d9 = models.IntegerField()
    d10 = models.IntegerField()
    d11 = models.IntegerField()
    d12 = models.IntegerField()
    d13 = models.IntegerField()
    d14 = models.IntegerField()
    d15 = models.IntegerField()
    d16 = models.IntegerField()
    d17 = models.IntegerField()
    d18 = models.IntegerField()
    d19 = models.IntegerField()
    d20 = models.IntegerField()
    d21 = models.IntegerField()
    d22 = models.IntegerField()
    d23 = models.IntegerField()
    d24 = models.IntegerField()
    d25 = models.IntegerField()
    score = models.DecimalField(max_digits = 3, decimal_places = 1)

    def __iter__(self):
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def get_labels(self):
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        dsmv_list = json.load(json_data)[5]['questions']
        i = 1
        for index in dsmv_list:
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()
        return labels



class TortureHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    date = models.DateField()
    th1 = models.BooleanField()
    th2 = models.BooleanField()
    th3 = models.BooleanField()
    th4 = models.BooleanField()
    th5 = models.BooleanField()
    th6 = models.BooleanField()
    th7 = models.BooleanField()
    th8 = models.BooleanField()
    th9 = models.BooleanField()
    th10 = models.BooleanField()
    th11 = models.BooleanField()
    th12 = models.BooleanField()
    th13 = models.BooleanField()
    th14 = models.BooleanField()
    th15 = models.BooleanField()
    th16 = models.BooleanField()
    th17 = models.BooleanField()
    th18 = models.BooleanField()
    th19 = models.BooleanField()
    th20 = models.BooleanField()
    th21 = models.BooleanField()
    th22 = models.BooleanField()
    th23 = models.BooleanField()
    th24 = models.BooleanField()
    th25 = models.BooleanField()
    th26 = models.BooleanField()
    th27 = models.BooleanField()
    th28 = models.TextField(default = '')

    def __iter__(self):
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def get_labels(self):
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        th_list = json.load(json_data)[6]['questions']
        i = 1
        for index in th_list:
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()
        return labels


class HopkinsPart1(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    date = models.DateField()
    hp1 = models.IntegerField()
    hp2 = models.IntegerField()
    hp3 = models.IntegerField()
    hp4 = models.IntegerField()
    hp5 = models.IntegerField()
    hp6 = models.IntegerField()
    hp7 = models.IntegerField()
    hp8 = models.IntegerField()
    hp9 = models.IntegerField()
    hp10 = models.IntegerField()
    score = models.DecimalField(max_digits = 3, decimal_places = 1)

    def __iter__(self):
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def get_labels(self):
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        hp1_list = json.load(json_data)[7]['questions']
        i = 1
        for index in hp1_list:
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()
        return labels



class HopkinsPart2(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    date = models.DateField()
    hp11 = models.IntegerField()
    hp12 = models.IntegerField()
    hp13 = models.IntegerField()
    hp14 = models.IntegerField()
    hp15 = models.IntegerField()
    hp16 = models.IntegerField()
    hp17 = models.IntegerField()
    hp18 = models.IntegerField()
    hp19 = models.IntegerField()
    hp20 = models.IntegerField()
    hp21 = models.IntegerField()
    hp22 = models.IntegerField()
    hp23 = models.IntegerField()
    hp24 = models.IntegerField()
    hp25 = models.IntegerField()
    score = models.DecimalField(max_digits = 3, decimal_places = 1)

    def __iter__(self):
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def get_labels(self):
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        hp2_list = json.load(json_data)[8]['questions']
        i = 11
        for index in hp2_list:
            labels[index['id']] = str(i) + '. ' + index['body']
            i+=1
        json_data.close()
        return labels


        
