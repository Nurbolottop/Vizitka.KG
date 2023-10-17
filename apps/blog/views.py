from django.shortcuts import render

# my imports
from apps.index import models
from datetime import datetime

from apps.blog.models import Blog
from apps.advert.models import BigAdvert

# Create your views here.
def blog(request):
    blog = Blog.objects.all()  
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    popular_posts = Blog.objects.order_by('-views')[:5]
    popular_posts = Blog.objects.order_by('-views')[:5]
    big_advert = BigAdvert.objects.latest('id')
    return render(request, 'base/page-blog.html', locals())

def blog_detail(request, id):
    setting = models.Settings.objects.latest('id')
    blog = Blog.objects.get(id=id)
    popular_posts = Blog.objects.order_by('-views')[:5]
    current_date = datetime.now()
    return render(request, 'detail/page-single-post-creative.html', locals())
        