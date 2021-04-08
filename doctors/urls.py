from django.urls import path
from django.views.decorators.http import require_POST

from . import views
from . import forms

urlpatterns = [
    path("", views.DoctorListView.as_view(), name="doctor_list"),
    path("<int:pk>/", views.DoctorDetailView.as_view(), name="doctor_detail"),
]