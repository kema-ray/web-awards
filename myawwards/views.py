from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    project=Project.all_projects()
    user_projects = []
    for project in project:
        pic = Profile.objects.filter(user=project.designer.id).first()
        if pic:
            pic = pic.profile_pic.url
        else:
            pic = ''
        obj = dict(
            title=project.title,
            url=project.url,
            image=project.image,
            avatar=pic,
            description=project.description,
            author=project.designer.username,
            date_posted=project.date_posted,
            technologies = project.technologies,
        )
        user_projects.append(obj)

    return render(request, 'home.html',{"user_projects":user_projects})
