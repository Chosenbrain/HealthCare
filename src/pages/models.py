from django.db import models
from config.utils import unique_slug_generator
from users.models import Doctor
from django.urls import reverse
from PIL import Image
from django.db.models.signals import pre_save



class Lab(models.Model):
    title = models.CharField(max_length=100)
    subheading = models.CharField(max_length=200)
   
    

    def __str__(self):
        return self.title



    
class Category(models.Model):
    category= models.CharField(max_length=50)


    def __str__(self):
        return self.category



class Blog(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    image = models.ImageField()
    summary = models.TextField(max_length=150)
    slug = models.SlugField(max_length=100, null=True, blank=True)

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
                return reverse('blog-detail', kwargs={'pk': self.slug})




def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Blog)



   


class Pricing(models.Model):
    plans = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    service = models.CharField(max_length=250)

  
    def __str__(self):
        return self.plans

class Pricingservice(models.Model):
    pricing = models.ForeignKey(Pricing, default=None, on_delete=models.CASCADE)
    services = models.CharField(max_length=250)

    

    def __str__(self):
        return self.pricing.plans






