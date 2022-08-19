from accounts.views import Index, RegisterDoctor, RegisterPatient
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("register/doctor", RegisterDoctor.as_view(), name='register-doctor'),
    path("register/patient", RegisterPatient.as_view(), name='register-patient'),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", logout_then_login, name="logout"),
]