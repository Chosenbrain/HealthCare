from django.views.generic import TemplateView
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Blog,Lab,Pricing,Pricingservice
from users.models import Doctor,CustomUser




class HomePageView(ListView):
    model = Pricing
    template_name = 'pages/home.html'
    
  
class PricingPageView(ListView):
    model = Pricing
    template_name = 'pages/pricing.html'
    





class AboutPageView(TemplateView):
    template_name = 'pages/about.html'



@login_required
def appointment(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_service = request.POST.get('message_service', False)
        message_plan = request.POST['message_plan']
        message_date = request.POST['message_date']
        message_time = request.POST['message_time']
        message = request.POST['message']

        send_mail(
            'message from ' + message_name,
            message,
            message_service,
            message_plan,
            message_date,
            message_time,
            message_email,
            ['exactmusty1994@gmail.com', 'jazeera@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'pages/appointment.html', {'message_name': message_name})
    else:
    
        return render(request, 'pages/appointment.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']

        send_mail(
            'messge from ' + message_name,
            message,
            message_email,
            ['exactmusty1994@gmail.com', 'jazeera@gmail.com'],
        )
        return render(request, 'pages/contact.html', {'message_name': message_name})
    else:
        return render(request, 'pages/contact.html', {})


def doctor(request):
    context = {
        'doctor':Doctor.objects.all()
        
    }
    return render(request, 'pages/doctor.html', context)



@login_required
def chat(request):
    return render(request, 'pages/chat.html', {})






def blog(request):
    context={
        'blog_post':  Blog.objects.all()
    }

    return render(request, 'pages/blog.html', context)
       

class BlogListView(ListView):
    model = Blog
    template_name = 'pages/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'blog_post'
    ordering = ['-timestamp']
    paginate_by = 5


class BlogDetailView(DetailView):
    model = Blog
    




class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'categories', 'overview', 'image', 'summary']

    def form_valid(self, form):
        form.instance.doctor = Doctor.objects.get(user=self.request.user)
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'categories', 'overview', 'image', 'summary']

    def form_valid(self, form):
        form.instance.doctor = Doctor.objects.get(user=self.request.user)
        return super().form_valid(form)


    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.doctor.user:
            return True
        return False




class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog')

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.doctor.user:
            return True
        return False




class CustomUserBlogListView(ListView):
    model = Blog
    template_name = 'pages/user_blog.html' 
    context_object_name = 'blog_post'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
        return Blog.objects.filter(doctor=user.doctor).order_by('-timestamp')
      


def lab(request):
    context = {
        'all_lab_test':Lab.objects.all(),
   
    }
    return render(request, 'pages/lab.html', context)




