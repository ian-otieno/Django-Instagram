from django.contrib.messages import success
from django.core.checks import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Images, Profile, Comment
from .forms import EditProfileForm, ImageForm, CommentForm, ProfileUpdateForm
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

@login_required(login_url='/accounts/login/')
def like_image(request, image_id):
    image = Images.objects.get(id =image_id)
    image.like.add(request.user.profile)
    image.save()
    return HttpResponseRedirect(reverse('image_detail', args=[str(image_id)]))

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user =request.user
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.profile = current_user
            image.save()
            return redirect("index")

    else:
        form = ImageForm()
    return render (request, 'new_image.html', {"form":form})

@login_required(login_url='/accounts/login/')
def delete_image(request, image_id):
    item = Images.objects.get(id =image_id)
    if request.method =='POST':
        item.delete() 
        return redirect('/')
    return render(request, 'instagram/delete.html', {"item":item})
   

@login_required(login_url='/accounts/login/')
def update_image(request, image_id):
    image = Images.objects.get(id=image_id)
    update_form = ImageForm(instance=image)
    context = {"update_form": update_form}
    if request.method =="POST":
        update_form = ImageForm(request.POST, instance = image)
        if update_form.is_valid():
            update_form.save()
            return redirect("/")

    return render (request, 'instagram/update_image.html', context)
 
@login_required(login_url='/accounts/login/')
def search(request):
  if 'user' in request.GET and request.GET['user']:
    search_term = request.GET.get('user')
    searched_users = Profile.search_profile(search_term)
    return render(request, 'instagram/search.html', {'users':searched_users})

  else: 
    return render(request, 'instagram/search.html')
    


