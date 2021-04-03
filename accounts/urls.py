from django.contrib.auth import views
from django.urls import path

from .views import Registration

urlpatterns = [
    path("registration/", Registration.as_view(), name="registration"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]