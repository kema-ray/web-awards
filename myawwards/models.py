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
    designer = models.ForeignKey(User,on_delete=models.CASCADE,default='',null=True ,related_name='author')


    def save_project(self):
        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):
    image = models.ImageField(upload_to = 'profile/',blank = 'True')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=200,null=True,blank=True,default='My Bio')
    # date_created = models.DateField(auto_now_add=True)

    def save_profile(self):
        self.save
    
    def __str__(self):
        return f'{self.user.username} Profile'
