from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import *

class NewProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('title', 'url', 'description', 'technologies','image','user',)

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design','usability','content','score',]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
 
    class Meta:
        model = User
        fields = ['username', 'email']
 
 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio',]