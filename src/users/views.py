from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Doctor

@login_required
def profile(request):
    doctor = Doctor.objects.all()
    image = Doctor.objects.all()
    email = Doctor.objects.all()
    bio = Doctor.objects.all()
    speciality = Doctor.objects.all()
    context ={
        'image':image,
        'email':email,
        'bio':bio,
        'speciality':speciality
    }
    return render(request, 'pages/profile.html', context)