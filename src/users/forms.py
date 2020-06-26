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



class CustomUserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['email']


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'gender', 'location', 'certification', 'place_of_work', 'image', 'speciality', 'bio']

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [ 'subscribe' ]
