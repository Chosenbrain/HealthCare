from django.db import models
from users.models import Doctor
from django.urls import reverse
from PIL import Image



class Lab(models.Model):
    title = models.CharField(max_length=100)
    subheading = models.CharField(max_length=200)
   
    

    def __str__(self):
        return self.title



    
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
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    image = models.ImageField()
    summary = models.TextField(max_length=150)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})








