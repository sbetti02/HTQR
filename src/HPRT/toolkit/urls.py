from django.urls import path

from . import views
from .models import Toolkit

urlpatterns = [
    path('<int:pk>/', views.ToolkitDetailView.as_view(), name = 'toolkit_detail'),
    path('<int:pk>/ask/', views.ToolkitUpdateAskView.as_view(), name = 'toolkit_ask'),
    path('<int:pk>/identify/', views.ToolkitUpdateIdentifyView.as_view(), name = 'toolkit_identify'),
    path('<int:pk>/diagnose&treat/', views.ToolkitUpdateDiagTreatView.as_view(), name = 'toolkit_diagtreat'),
    path('<int:pk>/refer/', views.ToolkitUpdateReferView.as_view(), name = 'toolkit_refer'),
    path('<int:pk>/reinforce&teach/', views.ToolkitUpdateReinTeachView.as_view(), name = 'toolkit_reinteach'),
    path('<int:pk>/recommend/', views.ToolkitUpdateRecommendView.as_view(), name = 'toolkit_recommend'),
    path('<int:pk>/reduce_risks/', views.ToolkitUpdateReduceRiskView.as_view(), name = 'toolkit_reducerisk'),
    path('<int:pk>/culturally_attuned/', views.ToolkitUpdateCulturalView.as_view(), name = 'toolkit_culture'),
    path('<int:pk>/prescribe/', views.ToolkitUpdatePrescribeView.as_view(), name = 'toolkit_prescribe'),
    path('<int:pk>/close&schedule/', views.ToolkitUpdateCloseView.as_view(), name = 'toolkit_close'),
    path('<int:pk>/prevent_burnout/', views.ToolkitUpdateBurnoutView.as_view(), name = 'toolkit_burnout'),
    path('screenings/<int:pk>', views.ScreeningsListView.as_view(), name = 'screenings'),
    path('new_htq/<int:pk>', views.HTQCreateView.as_view(), name = 'HTQ_new'),
    path('new_dsmv/<int:pk>', views.DSMVCreateView.as_view(), name = 'DSMV_new'),
    path('new_th/<int:pk>', views.TortureHistoryCreateView.as_view(), name = 'TH_new'),
    path('new_hp1/<int:pk>', views.HopkinsPart1CreateView.as_view(), name = 'HP1_new'),
    path('new_hp2/<int:pk>', views.HopkinsPart2CreateView.as_view(), name = 'HP2_new'),
    path('new_gh/<int:pk>', views.GeneralHealthCreateView.as_view(), name = 'GH_new'),
    path('htq/<int:pk>', views.HTQDetailView.as_view(), name = 'HTQ_detail'),
    path('dsmv/<int:pk>', views.DSMVDetailView.as_view(), name = 'DSMV_detail'),
    path('th/<int:pk>', views.TortureHistoryDetailView.as_view(), name = 'TH_detail'),
    path('hp1/<int:pk>', views.HopkinsPart1DetailView.as_view(), name = 'HP1_detail'),
    path('hp2/<int:pk>', views.HopkinsPart2DetailView.as_view(), name = 'HP2_detail'),
    path('htq/<int:pk>/pdf', views.HTQPDF.as_view(), name = 'HTQ_pdf'),
    path('dsmv/<int:pk>/pdf', views.DSMVPDF.as_view(), name = 'DSMV_pdf'),
    path('th/<int:pk>/pdf', views.THPDF.as_view(), name = 'TH_pdf'),
    path('hp1/<int:pk>/pdf', views.HP1PDF.as_view(), name = 'HP1_pdf'),
    path('hp2/<int:pk>/pdf', views.HP2PDF.as_view(), name = 'HP2_pdf'),
    path('gh/<int:pk>/pdf', views.GHPDF.as_view(), name = 'GH_pdf'),
]