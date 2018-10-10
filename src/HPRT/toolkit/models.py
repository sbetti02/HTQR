from django.db import models
from PatientPortal.models import DocPat, Patient, Doctor
from django.core.validators import MaxValueValidator, MinValueValidator
import json, os

CHOICES = [(i,i) for i in range(1,5)]

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
    te1 = models.NullBooleanField()
    te2 = models.NullBooleanField()
    te3 = models.NullBooleanField()
    te4 = models.NullBooleanField()
    te5 = models.NullBooleanField()
    te6 = models.NullBooleanField()
    te7 = models.NullBooleanField()
    te8 = models.NullBooleanField()
    te9 = models.NullBooleanField()
    te10 = models.NullBooleanField()
    te11 = models.NullBooleanField()
    te12 = models.NullBooleanField()
    te13 = models.NullBooleanField()
    te14 = models.NullBooleanField()
    te15 = models.NullBooleanField()
    te16 = models.NullBooleanField()
    te17 = models.NullBooleanField()
    te18 = models.NullBooleanField()
    te19 = models.NullBooleanField()
    te20 = models.NullBooleanField()
    te21 = models.NullBooleanField()
    te22 = models.NullBooleanField()
    te23 = models.NullBooleanField()
    te24 = models.NullBooleanField()
    te25 = models.NullBooleanField()
    te26 = models.NullBooleanField()
    te27 = models.NullBooleanField()
    te28 = models.NullBooleanField()
    te29 = models.NullBooleanField()
    te30 = models.NullBooleanField()
    te31 = models.NullBooleanField()
    te32 = models.NullBooleanField()
    te33 = models.NullBooleanField()
    te34 = models.NullBooleanField()
    te35 = models.NullBooleanField()
    te36 = models.NullBooleanField()
    te37 = models.NullBooleanField()
    te38 = models.NullBooleanField()
    te39 = models.NullBooleanField()
    te40 = models.NullBooleanField()
    te41 = models.TextField(default = '', null=True, blank=True)
   
    pd1 = models.TextField(default = '', null=True, blank=True)
    pd2 = models.TextField(default = '', null=True, blank=True)

    hi1 = models.NullBooleanField()
    hi1_a = models.NullBooleanField()
    hi1_b = models.DurationField(null=True, blank=True)
    hi2 = models.NullBooleanField()
    hi2_a = models.NullBooleanField()
    hi2_b = models.DurationField(null=True, blank=True)
    hi3 = models.NullBooleanField()
    hi3_a = models.NullBooleanField()
    hi3_b = models.DurationField(null=True, blank=True)
    hi4 = models.NullBooleanField()
    hi4_a = models.NullBooleanField()
    hi4_b = models.DurationField(null=True, blank=True)
    hi5 = models.NullBooleanField()
    hi_a = models.DecimalField(max_digits = 4, decimal_places = 1, null=True, blank=True)
    hi_b = models.DecimalField(max_digits = 4, decimal_places = 1, null=True, blank=True)
    hi_c = models.NullBooleanField()

    def __iter__(self):
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def get_labels(self):
        labels = {}

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
        return labels


class DSMV(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    date = models.DateField()
    d1 = models.IntegerField(default=None, choices=CHOICES)
    d2 = models.IntegerField(default=None, choices=CHOICES)
    d3 = models.IntegerField(default=None, choices=CHOICES)
    d4 = models.IntegerField(default=None, choices=CHOICES)
    d5 = models.IntegerField(default=None, choices=CHOICES)
    d6 = models.IntegerField(default=None, choices=CHOICES)
    d7 = models.IntegerField(default=None, choices=CHOICES)
    d8 = models.IntegerField(default=None, choices=CHOICES)
    d9 = models.IntegerField(default=None, choices=CHOICES)
    d10 = models.IntegerField(default=None, choices=CHOICES)
    d11 = models.IntegerField(default=None, choices=CHOICES)
    d12 = models.IntegerField(default=None, choices=CHOICES)
    d13 = models.IntegerField(default=None, choices=CHOICES)
    d14 = models.IntegerField(default=None, choices=CHOICES)
    d15 = models.IntegerField(default=None, choices=CHOICES)
    d16 = models.IntegerField(default=None, choices=CHOICES)
    d17 = models.IntegerField(default=None, choices=CHOICES)
    d18 = models.IntegerField(default=None, choices=CHOICES)
    d19 = models.IntegerField(default=None, choices=CHOICES)
    d20 = models.IntegerField(default=None, choices=CHOICES)
    d21 = models.IntegerField(default=None, choices=CHOICES)
    d22 = models.IntegerField(default=None, choices=CHOICES)
    d23 = models.IntegerField(default=None, choices=CHOICES)
    d24 = models.IntegerField(default=None, choices=CHOICES)
    d25 = models.IntegerField(default=None, choices=CHOICES)
    score = models.DecimalField(max_digits = 3, decimal_places = 1)

    def __iter__(self):
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def get_labels(self):
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        dsmv_list = json.load(json_data)[5]['questions']
        for i, index in enumerate(dsmv_list,start=1):
            labels[index['id']] = str(i) + '. ' + index['body']
        json_data.close()
        return labels



class TortureHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    date = models.DateField()
    th1 = models.NullBooleanField()
    th2 = models.NullBooleanField()
    th3 = models.NullBooleanField()
    th4 = models.NullBooleanField()
    th5 = models.NullBooleanField()
    th6 = models.NullBooleanField()
    th7 = models.NullBooleanField()
    th8 = models.NullBooleanField()
    th9 = models.NullBooleanField()
    th10 = models.NullBooleanField()
    th11 = models.NullBooleanField()
    th12 = models.NullBooleanField()
    th13 = models.NullBooleanField()
    th14 = models.NullBooleanField()
    th15 = models.NullBooleanField()
    th16 = models.NullBooleanField()
    th17 = models.NullBooleanField()
    th18 = models.NullBooleanField()
    th19 = models.NullBooleanField()
    th20 = models.NullBooleanField()
    th21 = models.NullBooleanField()
    th22 = models.NullBooleanField()
    th23 = models.NullBooleanField()
    th24 = models.NullBooleanField()
    th25 = models.NullBooleanField()
    th26 = models.NullBooleanField()
    th27 = models.NullBooleanField()
    th28 = models.TextField(default = '', null=True, blank=True)

    def __iter__(self):
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def get_labels(self):
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        th_list = json.load(json_data)[6]['questions']
        for i, index in enumerate(th_list, start=1):
            labels[index['id']] = str(i) + '. ' + index['body']
        json_data.close()
        return labels


class HopkinsPart1(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    date = models.DateField()
    hp1 = models.IntegerField(default=None, choices=CHOICES)
    hp2 = models.IntegerField(default=None, choices=CHOICES)
    hp3 = models.IntegerField(default=None, choices=CHOICES)
    hp4 = models.IntegerField(default=None, choices=CHOICES)
    hp5 = models.IntegerField(default=None, choices=CHOICES)
    hp6 = models.IntegerField(default=None, choices=CHOICES)
    hp7 = models.IntegerField(default=None, choices=CHOICES)
    hp8 = models.IntegerField(default=None, choices=CHOICES)
    hp9 = models.IntegerField(default=None, choices=CHOICES)
    hp10 = models.IntegerField(default=None, choices=CHOICES)
    score = models.DecimalField(max_digits = 3, decimal_places = 1)

    def __iter__(self):
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def get_labels(self):
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        hp1_list = json.load(json_data)[7]['questions']
        for i, index in enumerate(hp1_list, start=1):
            labels[index['id']] = str(i) + '. ' + index['body']
        json_data.close()
        return labels



class HopkinsPart2(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    date = models.DateField()
    hp11 = models.IntegerField(default=None, choices=CHOICES)
    hp12 = models.IntegerField(default=None, choices=CHOICES)
    hp13 = models.IntegerField(default=None, choices=CHOICES)
    hp14 = models.IntegerField(default=None, choices=CHOICES)
    hp15 = models.IntegerField(default=None, choices=CHOICES)
    hp16 = models.IntegerField(default=None, choices=CHOICES)
    hp17 = models.IntegerField(default=None, choices=CHOICES)
    hp18 = models.IntegerField(default=None, choices=CHOICES)
    hp19 = models.IntegerField(default=None, choices=CHOICES)
    hp20 = models.IntegerField(default=None, choices=CHOICES)
    hp21 = models.IntegerField(default=None, choices=CHOICES)
    hp22 = models.IntegerField(default=None, choices=CHOICES)
    hp23 = models.IntegerField(default=None, choices=CHOICES)
    hp24 = models.IntegerField(default=None, choices=CHOICES)
    hp25 = models.IntegerField(default=None, choices=CHOICES)
    score = models.DecimalField(max_digits = 3, decimal_places = 1)

    def __iter__(self):
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def get_labels(self):
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        hp2_list = json.load(json_data)[8]['questions']
        for i, index in enumerate(hp2_list, start=1):
            labels[index['id']] = str(i) + '. ' + index['body']
        json_data.close()
        return labels


class GeneralHealth(models.Model):
    """ Abstract model of General Health/Physical Functioning questionnaire. """
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    date = models.DateField()
    gh1 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = Poor"),(2,"2 = Fair"),(3,"3 = Good"),(4,"4 = Very Good"),(5,"5 = Excellent")])
    gh2 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = None"),(2,"2 = A Little"),(3,"3 = Some"),(4,"4 = Quite A Lot"),(5,"5 = Very Much")])
    gh3 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = Extremely"),(2,"2 = Quite A Lot"),(3,"3 = Moderately"),(4,"4 = Slightly"),(5,"5 = Not At All")])
    gh4 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = Seven"),(2,"2 = Five to Seven"),(3,"3 = Three to Five"),(4,"4 = One to Three"),(5,"5 = Zero")])
    gh5 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = None"),(2,"2 = Less than Four"),(3,"3 = Four to Five"),(4,"4 = Five to Seven"),(5,"5 = More than Seven")])
    gh6 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = Daily"),(2,"2 = Weekly"),(3,"3 = Monthly"),(4,"4 = Yearly"),(5,"5 = No")])
    gh7 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = Zero"),(2,"2 = One to Three"),(3,"3 = Three to Five"),(4,"4 = Five to Seven"),(5,"5 = More than Seven")])
    gh8 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = Zero"),(2,"2 = One to Three"),(3,"3 = Three to Five"),(4,"4 = Five to Seven"),(5,"5 = More than Seven")])
    gh9 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = No"),(2,"2 = Yes")])
    gh10 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = No"),(2,"2 = No, but trying to obtain work"),(3,"3 = Yes")])
    gh11 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = Yes"),(2,"2 = Yes and has been referred"),(3,"3 = No")])
    gh12 = models.IntegerField(null=True, choices=[('',"Choose one"),(1,"1 = Yes"),(2,"2 = Yes and has been referred"),(3,"3 = No")])
    score = models.DecimalField(max_digits=3, decimal_places=1)

    def __iter__(self):
        """ Make object iterable. """
        for field_name in [f.name for f in self._meta.get_fields()]:
            value = getattr(self, field_name, None)
            yield (field_name, value)

    def get_labels(self):
        """ Get labels(questions) to General Health questionnaire. """
        labels = {}
        json_data = open(os.path.join('static', "questions.json"), 'r')
        gh_list = json.load(json_data)[9]['questions']
        for i, index in enumerate(gh_list, start=1):
            labels[index['id']] = str(i) + '. ' + index['body']
        json_data.close()
        return labels