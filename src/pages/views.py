from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Blog
from users.models import Doctor




class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'



@login_required
def appointment(request):
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
    return render(request, 'pages/doctor.html', {})


def blog(request):
    blog_post = Blog.objects.all()
    ordering = ['-timestamp']
    paginator = Paginator(blog_post, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(2)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) 
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var
        
    }

    return render(request, 'pages/blog.html', context)



class BlogDetailView(DetailView):
    model = Blog
    template_name = 'pages/blog.html'
    context_object_name = 'blog_post'
    




class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'categories', 'overview']

    def form_valid(self, form):
        form.instance.user = Doctor.objects.get(user=self.request.user)
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'categories', 'overview']

    def form_valid(self, form):
        form.instance.user = Doctor.objects.get(user=self.request.user)
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.user:
            return True
        return False


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.user:
            return True
        return False


        

def lab(request):
    return render(request, 'pages/lab.html', {})




