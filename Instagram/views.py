from django.contrib.messages import success
from django.core.checks import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Images, Profile, Comment
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    name = 'instagram app'
    images = Images.objects.all()
    comments = Comment.objects.all()
    
    return render(request, 'instagram/index.html', {"name":name, "images":images, "comments":comments})
def image_detail(request, image_id):
    try:
        image = Images.objects.get(id = image_id)
        image_likes = image.like.count()
        
    except Images.DoesNotExist:
        raise Http404()

    return render(request,"instagram/image.html", {"image":image, "image_likes":image_likes})


