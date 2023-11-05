
from apps.blog.models import Blog

# Create your views here.

def firstnewsblogdetail1_mtehod():
    blog = models.Blog.objects.all().order_by("?")[:]
    firstnews = models.FirstBlogDetail.objects.latest('id')  
    result_blog = []
    print(result_blog)
    n = 0
    for blogs in blog:
        if firstnews.first == blogs.category:
            result_blog.append(blogs)
            n += 1
            if n == 2:
                return result_blog
                break

def firstnewsblogdetail2_mtehod():
    blog = models.Blog.objects.all().order_by("?")[:]
    firstblog = models.SecondBlogDetail.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if firstblog.second ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break

def firstnewsblogdetail3_mtehod():
    blog = models.Blog.objects.all().order_by("?")[:]
    firstblog = models.ThirdBlogDetail.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if firstblog.third ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break