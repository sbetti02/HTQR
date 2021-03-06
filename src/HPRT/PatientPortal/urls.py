from django.urls import path

from . import views
from .models import Patient


urlpatterns = [
    path('', views.PatientListView.as_view(), name='home'),
    path('patient/<int:pk>/', views.PatientDetailView.as_view(), name = 'patient_detail'),
    path('patient/new/', views.PatientCreateView.as_view(), name = 'patient_new'),
    path('patient/addexisting/', views.PatientAddExistingView.as_view(), name = 'patient_add_existing'),
    path('patient/<int:pk>/edit/', views.PatientUpdateView.as_view(), name = 'patient_edit'),
    path('patient/<int:pk>/delete/', views.PatientDeleteView.as_view(), name = 'patient_delete'),
    path('site/new/', views.SiteCreateView.as_view(), name = 'site_new'),
    path('ajax/update_patients/', views.update_patients, name='update_patients'),
    path('patient/remove/<int:pk>/', views.patientRemove.as_view(), name = 'patient_remove'),
    path('patient/add/<int:pk>/', views.patientAdd.as_view(), name = 'patient_add'),
    path('search/results/', views.searchListView.as_view(), name = 'search_list'),
]
