from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Doctor,Patient

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['image', 'speciality', 'bio']

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [ 'subscribe' ]
