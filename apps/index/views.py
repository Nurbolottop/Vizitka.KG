from django.shortcuts import render,redirect


# my imports
from apps.index import models
from apps.blog.models import Blog
# Create your views here.

def index(request):
    setting = models.Settings.objects.latest('id')
    blog = Blog.objects.all()
    latest_news = Blog.objects.order_by('-created_at')[:5]
    latest_new = Blog.objects.order_by('-created_at')[:1]
    popular_posts = Blog.objects.order_by('-views')[:3]
    popular_post = Blog.objects.order_by('-views')[:1]
    
    return render(request, 'base/home-default.html', locals())

def contact(request):
    setting = models.Settings.objects.latest('id')
    return render(request, 'base/page-contact.html', locals())