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


def B3Blog3_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    third_blog = models.B3Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if third_blog.third ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
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
            if n ==3:
                return result_blogs
                break     

def B5Blog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    five_blog = models.B5Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if five_blog.five ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break       

def B5Blog3_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    five_blog = models.B5Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if five_blog.five ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break     

def B6Blog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    six_blog = models.B6Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if six_blog.six ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break       

def B6Blog3_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    six_blog = models.B6Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if six_blog.six ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break   

def B7Blog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    seven_blog = models.B7Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if seven_blog.seven ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break       

def B7Blog3_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    seven_blog = models.B7Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if seven_blog.seven ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break   

def B8Blog1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    eight_blog = models.B8Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if eight_blog.eight ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==1:
                return result_blogs
                break       

def B8Blog3_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    eight_blog = models.B8Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if eight_blog.eight ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==3:
                return result_blogs
                break   

def fiveone1_mtehod():
    blog = Blog.objects.all().order_by("?")[:]
    fiveone_blog = models.B9Blog.objects.latest('id')  
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
    fiveone_blog = models.B9Blog.objects.latest('id')  
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
    fivetwo_blog = models.B10Blog.objects.latest('id')  
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
    fivetwo_blog = models.B10Blog.objects.latest('id')  
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
    fivetwo_blog = models.B11Blog.objects.latest('id')  
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
    fivethree_blog = models.B11Blog.objects.latest('id')  
    result_blogs = []
    n = 0
    for blogs in blog:
        if fivethree_blog.five_three ==blogs.category:
            result_blogs.append(blogs)
            n+=1
            if n ==2:
                return result_blogs
                break    


