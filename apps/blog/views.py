from django.shortcuts import render

# my imports
from apps.index import models
from apps.blog.models import Blog

# Create your views here.
def blog(request):
    setting = models.Settings.objects.latest('id')
    blog = Blog.objects.all()  
    popular_posts = Blog.objects.order_by('-views')[:5]
    popular_posts = Blog.objects.order_by('-views')[:5]
    
    return render(request, 'base/page-blog.html', locals())

def blog_detail(request, id):
    setting = models.Settings.objects.latest('id')
    blog = Blog.objects.get(id=id)
    popular_posts = Blog.objects.order_by('-views')[:5]
    
    return render(request, 'detail/page-single-post-creative.html', locals())
        