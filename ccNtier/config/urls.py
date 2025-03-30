from django.urls import path
from hospital.api.views.patient_views import PatientView
from hospital.api.views.dashboard_view import DashboardView

urlpatterns = [
    path('patients/<int:patient_id>/', PatientView.as_view()),
    path('dashboard/', DashboardView.as_view()),
]