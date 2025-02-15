from django.db import models
import os

def course_dir_name(instance, filename):
    return os.path.join('course/media/',instance.name, filename)

# Create your models here.
class course(models.Model):
    name= models.CharField(max_length=200)
    email = models.EmailField()
    phone =models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    checkbox = models.BooleanField()
    #photo = models.ImageField(upload_to='photos/', default=None, null=True)
    photo = models.ImageField(upload_to=course_dir_name, default=None, null=True)
    def __str__(self):
        return f"{self.name}"

