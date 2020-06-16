from django.urls import path
from users import views as user_views

from .views import (BlogCreateView,
                    BlogDetailView,
                    BlogUpdateView,
                    BlogDeleteView,
                    BlogListView,
                    CustomUserBlogListView
                    )
from .views import HomePageView, AboutPageView, appointment, lab, contact, doctor

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('appointment/', appointment, name='appointment'),
    path('lab/', lab, name='lab'),
    path('contact/', contact, name='contact'),
    path('doctor/', doctor, name='doctor'),
    path('doctor/info/<str:username>', user_views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('user/blog/<str:username>', CustomUserBlogListView.as_view(), name='user-blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/new/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('doctor_info/', user_views.doctor_info, name='doctor_info'),
    path('patient/', user_views.patient, name='patient'),
   

]