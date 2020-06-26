from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CustomUserUpdateForm, DoctorUpdateForm
from .models import Doctor, Patient
from django.views.generic import DetailView



@login_required
def doctor_info(request):
    if request.method == 'POST':
        u_form = CustomUserUpdateForm(request.POST, instance=request.user)
        d_form = DoctorUpdateForm(request.POST,
                                  request.FILES,
                                  instance=request.user.doctor)
        if u_form.is_valid() and d_form.is_valid():
            u_form.save()
            d_form.save()
            messages.info(request, ("Your account has been updated!"))
            return redirect('doctor_info')

    else:
        u_form = CustomUserUpdateForm(instance=request.user)
        d_form = DoctorUpdateForm(instance=request.user.doctor)

    context = {
        'u_form': u_form,
        'd_form': d_form
    }
    return render(request, 'pages/doctor_info.html', context)


class DoctorDetailView(LoginRequiredMixin, DetailView):
    model = Doctor
    fields = ['full_name', 'gender', 'location', 'certification', 'place_of_work', 'image', 'speciality', 'bio']
    template_name = 'pages/doctor_detail.html'

    def get_object(self):
        return get_object_or_404(Doctor, user__username=self.kwargs['username'])


@login_required
def patient(request):
    context = {
        'patient': Patient.objects.all()
    
    }
    return render(request, 'pages/patient.html', context)
