from django.db import models
from PatientPortal.models import DocPat


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