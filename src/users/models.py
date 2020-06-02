from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email

class Doctor(models.Model):
    doctor = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    image = models.ImageField(default='jazeera.jpg', upload_to='profile_pic')
    email = models.EmailField()
    bio = models.TextField()
    speciality = models.CharField(max_length=300)



    def __str__(self):
        return f'{self.doctor.username} Doctor'


class Category(models.Model):
    title= models.CharField(max_length=50)


    def __str__(self):
        return self.title



class Blog(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    categories = models.ManyToManyField(Category)
    timestamp = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default = 0)
    doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title