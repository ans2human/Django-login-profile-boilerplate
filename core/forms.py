
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'photo', 'ph_no', 'company', 'designation', 'birth_date', 'website')

