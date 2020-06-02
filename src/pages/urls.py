from django.urls import path

from .views import HomePageView, AboutPageView, appointment, lab, contact, doctor, blog


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('appointment/', appointment, name='appointment'),
    path('lab/', lab, name='lab'),
    path('contact/', contact, name='contact'),
    path('doctor/', doctor, name='doctor'),
    path('blog/', blog, name='blog'),
    

]