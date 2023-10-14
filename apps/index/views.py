from django.shortcuts import render,redirect


# my imports
from apps.index import models
from apps.blog.models import Blog
# Create your views here.

def index(request):
    setting = models.Settings.objects.latest('id')
    blog = Blog.objects.all()
    return render(request, 'base/home-default.html', locals())

def contact(request):
    setting = models.Settings.objects.latest('id')
    return render(request, 'base/page-contact.html', locals())