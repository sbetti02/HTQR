from django.db import models
from PatientPortal.models import DocPat

class Toolkit(models.Model):
    def answer_default():
        return False

    docpat = models.ForeignKey(DocPat, on_delete = models.CASCADE)
    # patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    # doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)

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