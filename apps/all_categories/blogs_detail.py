from apps.blog.models import Blog
from apps.all_categories import models

# Create your views here.

def d1_method():
    blog = Blog.objects.all().order_by("?")[:]
    firstnews = models.D1Blog.objects.latest('id')  
    result_blog = []
    print(result_blog)
    n = 0
    for blogs in blog:
        if firstnews.first == blogs.category:
            result_blog.append(blogs)
            n += 1
            if n == 3:
                return result_blog
                break

def d2_method():
    blog = Blog.objects.all().order_by("?")[:]
    B1Blog = models.D2Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if B1Blog.second ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break

def d3_method():
    blog = Blog.objects.all().order_by("?")[:]
    B1Blog = models.D3Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if B1Blog.third ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break