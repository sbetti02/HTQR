from django.contrib import admin

from .models import Patient, Site, DocPat

admin.site.register(Patient)
admin.site.register(Site)
admin.site.register(DocPat)

# Register your models here.
