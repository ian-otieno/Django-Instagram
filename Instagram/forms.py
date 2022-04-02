from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.db.models import fields
from django.db.models.base import Model
from .models import Images, Comment, Profile
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        exclude = ['profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude=['images', 'commented_at','name']
        
