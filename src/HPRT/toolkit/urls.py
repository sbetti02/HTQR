from django.urls import path

from . import views
from .models import Toolkit

urlpatterns = [
    path('toolkit/<int:pk>/', views.ToolkitDetailView.as_view(), name = 'toolkit_detail'),
    path('toolkit/<int:pk>/ask/', views.ToolkitUpdateAskView.as_view(), name = 'toolkit_ask'),
    path('toolkit/<int:pk>/identify/', views.ToolkitUpdateIdentifyView.as_view(), name = 'toolkit_identify'),
    path('toolkit/<int:pk>/diagnose&treat/', views.ToolkitUpdateDiagTreatView.as_view(), name = 'toolkit_diagtreat'),
    path('toolkit/<int:pk>/refer/', views.ToolkitUpdateReferView.as_view(), name = 'toolkit_refer'),
    path('toolkit/<int:pk>/reinforce&teach/', views.ToolkitUpdateReinTeachView.as_view(), name = 'toolkit_reinteach'),
    path('toolkit/<int:pk>/recommend/', views.ToolkitUpdateRecommendView.as_view(), name = 'toolkit_recommend'),
    path('toolkit/<int:pk>/reduce_risks/', views.ToolkitUpdateReduceRiskView.as_view(), name = 'toolkit_reducerisk'),
    path('toolkit/<int:pk>/culturally_attuned/', views.ToolkitUpdateCulturalView.as_view(), name = 'toolkit_culture'),
    path('toolkit/<int:pk>/prescribe/', views.ToolkitUpdatePrescribeView.as_view(), name = 'toolkit_prescribe'),
    path('toolkit/<int:pk>/close&schedule/', views.ToolkitUpdateCloseView.as_view(), name = 'toolkit_close'),
    path('toolkit/<int:pk>/prevent_burnout/', views.ToolkitUpdateBurnoutView.as_view(), name = 'toolkit_burnout'),
]