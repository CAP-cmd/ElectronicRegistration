from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class DoctorListView(ListView):
    model = models.Doctor
    template_name = "doctor_list.html"


class DoctorDetailView(DetailView):
    model = models.Doctor
    template_name = "doctor_detail.html"
