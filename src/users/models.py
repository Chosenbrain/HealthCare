from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
    on_delete=models.CASCADE,
    related_name='profile')
    image = models.ImageField(default='jazeera.jpg', upload_to='profile_pics')
    bio = models.TextField()
    speciality = models.CharField(max_length=300)



    def __str__(self):
        return f'{self.user.username}'


