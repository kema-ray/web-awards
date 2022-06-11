from django.shortcuts import render,redirect
from .models import *
from .forms import *


def new_project(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
           
            image.save()
            
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})


def home(request):
    project=Project.all_projects()
    user_projects = []
    for project in project:
        pic = Profile.objects.filter(user=project.user).first()
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
            author=project.user,
            date_posted=project.date_posted,
            technologies = project.technologies,
        )
        user_projects.append(obj)

    return render(request, 'home.html',{"user_projects":user_projects})

def search_results(request):
    if 'project' in request.GET and request.GET['project']:
        search_term =request.GET.get('project')
        searched_project = Project.search_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{"message":message,"projects":searched_project})

    else:
        message = "You haven't searched for any term"

        return render(request,'search.html',{'message':message})
