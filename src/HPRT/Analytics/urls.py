from django.urls import path

from . import views

urlpatterns = [
    path('', views.AnalyticQueryView.as_view(), name='analytics_home'),
    path('results/', views.AnalyticResultsView.as_view(), name='analytics_results')
]
