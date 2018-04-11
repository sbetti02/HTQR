from django.urls import path

from . import views
from .models import Patient

urlpatterns = [
    path('', views.PatientListView.as_view(), name='home'),
    path('patient/<int:pk>/', views.PatientDetailView.as_view(), name = 'patient_detail'),
    path('patient/new/', views.PatientCreateView.as_view(), name = 'patient_new'),
    path('patient/<int:pk>/edit/', views.PatientUpdateView.as_view(), name = 'patient_edit'),
    path('patient/<int:pk>/delete/', views.PatientDeleteView.as_view(), name = 'patient_delete'),
    path('site/new/', views.SiteCreateView.as_view(), name = 'site_new'),
]
