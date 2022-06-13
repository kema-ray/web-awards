from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    technologies = models.CharField(max_length=200, blank = True)
    image = models.ImageField(upload_to = 'images/',blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='',null=True ,related_name='author')


    def save_project(self):
        self.save()

    @classmethod
    def all_projects(cls) :
        projects = cls.objects.all()
        return projects
        
    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    def __str__(self):
        return self.title

class Profile(models.Model):
    image = models.ImageField(upload_to = 'profile/',blank = 'True',default='default.png')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=200,null=True,blank=True,default='')
    date = models.DateField(auto_now_add=True)

    def save_profile(self):
        self.save
    
    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):

        if created:
            Profile.objects.create(user=instance)

class Rating(models.Model):
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    ratings=((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10',))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    post = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)
    design = models.IntegerField(choices=ratings, default=0, blank=True)
    usability = models.IntegerField(choices=ratings, blank=True, default=0)
    content = models.IntegerField(choices=ratings, blank=True,default=0)
    score = models.FloatField(default=0, blank=True)
    
    def save_rating(self):
        self.save()
    
    def __str__(self):
        return f'{self.post} Rating'
    
    @classmethod
    def get_rating(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings
