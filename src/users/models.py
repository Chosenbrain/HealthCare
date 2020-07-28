from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from PIL import Image
import uuid


class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email


class Status(models.Model):
    title= models.CharField(max_length=5)


    def __str__(self):
        return self.title


class Doctor(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, related_name="doctor")
    image = models.ImageField(default='jazeera.jpg', upload_to='profile_pics')
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    speciality = models.CharField(max_length=200)
    describtion = models.CharField(max_length=100)
    status = models.ManyToManyField(Status)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    location = models.CharField(max_length=100)
    certification = models.CharField(max_length=300)
    place_of_work = models.CharField(max_length=300)
    



    def __str__(self):
        return self.user.username

    
    def save(self):
        super().save()


        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




class Patient(models.Model):
    STATE_CHOICES=(
        (True, u'Yes'),
        (False, u'No'),
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, related_name="patient")
    subscribe = models.BooleanField(default=False, choices=STATE_CHOICES)
    plan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, help_text="Unique ID for every particular patient for every profile")
   

    def __str__(self):
        return self.user.username
    


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    print("****", created)
    if instance.is_doctor:
        Doctor.objects.get_or_create(user=instance)
        
    else:
        Patient.objects.get_or_create(user=instance)
        


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    print("_-----")
    # print(instance.internprofile.bio, instance.internprofile.location)
    if instance.is_doctor:
        instance.doctor.save()
    else:
        Patient.objects.get_or_create(user=instance)








"""from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
​
​
class User(AbstractUser):
    is_intern = models.BooleanField(default=True)
​
​
class InternProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="intern_profile"
    )
    bio = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
​
​
class HRProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="hr_profile"
    )
    company_name = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
​
​
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print("****", created)
    if instance.is_intern:
        InternProfile.objects.get_or_create(user=instance)
    else:
        HRProfile.objects.get_or_create(user=instance)
​
​
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print("_-----")
    # print(instance.internprofile.bio, instance.internprofile.location)
    if instance.is_intern:
        instance.intern_profile.save()
    else:
        HRProfile.objects.get_or_create(user=instance)"""