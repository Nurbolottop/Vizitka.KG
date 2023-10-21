from apps.category import models
from apps.blog.models import Blog

# Create your views here.

def firstblog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    firstblog = models.FirstBlog.objects.latest('id')  
    result_blog = []
    n = 0
    for blogs in blog:
        if firstblog.first == blogs.category:
            result_blog.append(blogs)
            n += 1
            if n == 1:
                return result_blog
                break

def firstblog3_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    firstblog = models.FirstBlog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if firstblog.first ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break
            
def secondblog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    second_blog = models.SecondBlog.objects.latest('id')  
    result_blog = []
    n = 0
    for blogs in blog:
        if second_blog.second == blogs.category:
            result_blog.append(blogs)
            n += 1
            if n == 1:
                return result_blog
                break

def secondblog2_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    second_blog = models.SecondBlog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if second_blog.second ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==2:
                return result_blogs
                break
            
def secondblog4_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    second_blog = models.SecondBlog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if second_blog.second ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==4:
                return result_blogs
                break       

def thirdblog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    third_blog = models.ThirdBlog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if third_blog.third ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break       


def thirdblog2_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    third_blog = models.ThirdBlog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if third_blog.third ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==2:
                return result_blogs
                break       


def fourblog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    four_blog = models.FourBlog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if four_blog.four ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break       
            
def fourblog11_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    four_blog = models.FourBlog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if four_blog.four ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break       

def fourblog3_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    four_blog = models.FourBlog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if four_blog.four ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break       

def fiveone1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    fiveone_blog = models.FiveOneBlog.objects.latest('id')  
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
    fiveone_blog = models.FiveOneBlog.objects.latest('id')  
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
    fivetwo_blog = models.FiveTwoBlog.objects.latest('id')  
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
    fivetwo_blog = models.FiveTwoBlog.objects.latest('id')  
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
    fivetwo_blog = models.FiveThreeBlog.objects.latest('id')  
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
    fivethree_blog = models.FiveThreeBlog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if fivethree_blog.five_three ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==2:
                return result_blogs
                break    