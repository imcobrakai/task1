from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
class CreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'profile_pic', 'username', 'email', 'password1', 'password2', 'address1', 'city', 'state', 'pincode', 'is_patient', 'is_doctor')