from apps.all_categories import models
from apps.blog.models import Blog

# Create your views here.

def B1Blog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    B1Blog = models.B1Blog.objects.latest('id')  
    result_blog = []
    n = 0
    for blogs in blog:
        if B1Blog.first == blogs.category:
            result_blog.append(blogs)
            n += 1
            if n == 1:
                return result_blog
                break

def B1Blog3_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    B1Blog = models.B1Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if B1Blog.first ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break
            
def B2Blog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    second_blog = models.B2Blog.objects.latest('id')  
    result_blog = []
    n = 0
    for blogs in blog:
        if second_blog.second == blogs.category:
            result_blog.append(blogs)
            n += 1
            if n == 1:
                return result_blog
                break

def B2Blog2_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    second_blog = models.B2Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if second_blog.second ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==2:
                return result_blogs
                break
            
def B2Blog4_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    second_blog = models.B2Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if second_blog.second ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==4:
                return result_blogs
                break       

def B3Blog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    third_blog = models.B3Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if third_blog.third ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break       


def B3Blog2_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    third_blog = models.B3Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if third_blog.third ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==2:
                return result_blogs
                break       


def B4Blog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    four_blog = models.B4Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if four_blog.four ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break       

def B4Blog3_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    four_blog = models.B4Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if four_blog.four ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==4:
                return result_blogs
                break       

def fiveone1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    fiveone_blog = models.B5Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if fiveone_blog.five_one ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break    
def fiveone2_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    fiveone_blog = models.B5Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if fiveone_blog.five_one ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==2:
                return result_blogs
                break    
            
def fivetwo1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    fivetwo_blog = models.B6Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if fivetwo_blog.five_two ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break    
def fivetwo2_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    fivetwo_blog = models.B6Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if fivetwo_blog.five_two ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==2:
                return result_blogs
                break    
            
def fivethree1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    fivetwo_blog = models.B7Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if fivetwo_blog.five_three ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break    
            
def fivethree2_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    fivethree_blog = models.B7Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if fivethree_blog.five_three ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==2:
                return result_blogs
                break    