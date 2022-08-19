from accounts.models import CustomUser
from accounts.forms import CreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from localflavor.in_.in_states import STATE_CHOICES

class RegisterDoctor(CreateView):
    form_class = CreationForm
    model = CustomUser
    template_name = "accounts/register_doctor.html"
    success_url = reverse_lazy("accounts:login")

class RegisterPatient(CreateView):
    form_class = CreationForm
    model = CustomUser
    template_name = "accounts/register_patient.html"
    success_url = reverse_lazy("accounts:login")

class Index(LoginRequiredMixin, View):
    login_url = reverse_lazy("accounts:login")

    def get(self, request):
        context = {
            "user":request.user,
            "state": dict(STATE_CHOICES).get(request.user.state, None),
        }
        return render(request, "accounts/index.html", context)
