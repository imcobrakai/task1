from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.in_.models import INStateField

class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    profile_pic = models.ImageField(verbose_name=("Profile Picture"), default="default.jpg", upload_to='profile_pics')
    address1 = models.CharField(verbose_name=("Address line 1"), max_length=1000, blank=True, null=True)
    city = models.CharField(verbose_name=("City"), max_length=255, blank=True, null=True)
    state = INStateField(blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    REQUIRED_FIELDS = ['first_name', 'profile_pic']
    
