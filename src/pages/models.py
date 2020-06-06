from django.db import models
from users.models import Doctor
from django.urls import reverse




    


    
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
    user = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    slug = models.CharField(max_length=20)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog', kwargs={'pk': self.pk})