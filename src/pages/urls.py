from django.urls import path

from .views import HomePageView, AboutPageView, appointment, lab, contact, doctor, blog
from users import views as user_views
from .views import BlogCreateView,BlogDetailView,BlogUpdateView,BlogDeleteView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('appointment/', appointment, name='appointment'),
    path('lab/', lab, name='lab'),
    path('contact/', contact, name='contact'),
    path('doctor/', doctor, name='doctor'),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog'),
    path('blog/<int:pk>/update', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/new/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog-delete'),
    path('profile/', user_views.profile, name='profile'),

]