from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
