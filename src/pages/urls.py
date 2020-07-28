from django.urls import path
from users import views as user_views

from .views import (BlogCreateView,
                    BlogDetailView,
                    BlogUpdateView,
                    PricingPageView,
                    BlogDeleteView,
                    BlogListView,
                    CustomUserBlogListView
                    
                    )
from .views import HomePageView, AboutPageView, appointment, lab, contact, doctors, chat

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('pricing/', PricingPageView.as_view(), name='pricing'),
    path('appointment/', appointment, name='appointment'),
    path('lab/', lab, name='lab'),
    path('contact/', contact, name='contact'),
    path('doctors/', doctors, name='doctors'),
    path('chat/', chat, name='chat'),
    path('doctor/info/<str:username>', user_views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('user/blog/<str:username>', CustomUserBlogListView.as_view(), name='user-blog'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<slug:slug>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/new/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('doctor_info/', user_views.doctor_info, name='doctor_info'),
    path('patient/', user_views.patient, name='patient'),
   

]