from apps.category_blog import models
from apps.blog.models import Blog

# Create your views here.

def firstnewsblog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    firstnews = models.FirsNewsBlog.objects.latest('id')  
    result_blog = []
    n = 0
    for blogs in blog:
        if firstnews.first == blogs.category:
            result_blog.append(blogs)
            n += 1
            if n == 2:
                return result_blog
                break


def firstnewsblog3_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    firstblog = models.FirsNewsBlog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if firstblog.first ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break