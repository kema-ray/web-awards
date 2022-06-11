from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    technologies = models.CharField(max_length=200, blank = True)
    image = models.ImageField(upload_to = 'images/',blank = True)


    def save_project(self):
        self.save()

    def __str__(self):
        return self.title
