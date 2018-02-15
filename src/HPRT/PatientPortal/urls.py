from django.urls import path

from . import views

urlpatterns = [
    path('', views.PatientListView.as_view(), name='home'),
    path('patient/<int:pk>/', views.PatientDetailView.as_view(), name = 'patient_detail'),
    path('patient/new/', views.PatientCreateView.as_view(), name = 'patient_new'),
    #path('patient/<int:pk>/edit/', views.BlogUpdateView.as_view(), name = 'post_edit'),
    path('patient/<int:pk>/delete/', views.PatientDeleteView.as_view(), name = 'patient_delete'),
]
