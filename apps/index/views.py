from django.shortcuts import render,redirect
from django.db.models import Q
# my imports
from apps.index import models
from apps.blog.models import Blog,Stories
from datetime import datetime
from apps.advert.models import BigAdvert,NormalAdvert,SmallAdvert
from apps.category.models import FirstBlog
# from apps.index.parsing import dollar_pars,euro_pars,rub_pars,tenge_pars,get_weather_data,get_followers_count
from apps.index import blogs 
# Create your views here.
def index(request):
    #< start basic info >
    setting = models.Settings.objects.latest('id')
    team = models.Team.objects.all()
    stories = Stories.objects.all()
    #< end basic info >
    
    #< start extra >
    current_date = datetime.now()
    #< end extra >
    
    #< start news/blogs >
    blog = Blog.objects.all().order_by("?")[:]
    latest_news = Blog.objects.order_by('-created_at')[:5]
    latest_new = Blog.objects.order_by('-created_at')[:1]
    popular_posts = Blog.objects.order_by('-views')[:3]
    popular_post = Blog.objects.order_by('-views')[:1]
    #< end news/blogs >
    
    # < start advert >
    big_advert = BigAdvert.objects.latest('id')
    normal_advert = NormalAdvert.objects.latest('id')
    small_advert = SmallAdvert.objects.latest('id')
    # < end advert >

    #< start change categories >
    first_blog1 = blogs.firstblog1_mtehod()
    first_blog3 = blogs.firstblog3_mtehod()
    second_blog1 = blogs.secondblog1_mtehod()
    second_blog2 = blogs.secondblog2_mtehod()
    second_blog4 = blogs.secondblog4_mtehod()
    third_blog1 = blogs.thirdblog1_mtehod()
    four_blog1 = blogs.fourblog1_mtehod()
    four_blog11 = blogs.fourblog11_mtehod()
    four_blog2 = blogs.fourblog3_mtehod()
    fiveone_blog1 = blogs.fiveone1_mtehod()
    fiveone_blog2 = blogs.fiveone2_mtehod()
    fivetwo_blog1 = blogs.fivetwo1_mtehod()
    fivetwo_blog2 = blogs.fivetwo2_mtehod()
    fivethree_blog1 = blogs.fivethree1_mtehod()
    fivethree_blog2 = blogs.fivethree2_mtehod()
    
    #< утв change categories >
                
    # <start parsing >
    # dollar = dollar_pars()
    # euro = euro_pars()
    # rub = rub_pars()
    # tenge = tenge_pars()
    # temperature, weather_condition = get_weather_data()
    # username = 'vizitka_kg'
    # followers_count = get_followers_count(username)
    # < end parsing >

    return render(request, 'base/home-default.html', locals())

def storie(request,id):
    # stories_all = Stories.objects.all()
    stories_all = Stories.objects.exclude(id=id)
    stories = Stories.objects.get(id=id)
    
    # print(stories)
    
    # for stories_ap in stories_all:
    #     if stories_ap == stories:
    #         stories_ap.delete(stories)
    #     print(stories_ap)
    return render(request, 'base/stories.html', locals())

def contact(request):
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    # temperature, weather_condition = get_weather_data()
    return render(request, 'base/page-contact.html', locals())


def search(request):
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    # temperature, weather_condition = get_weather_data()
    
    query = request.POST.get('query', '')
    blog_results = []

    if query:
        # Используйте Q-объекты для выполнения поиска в моделях Shop и Product
        blog_results = Blog.objects.filter(Q(title__icontains=query) | Q(sub_title__icontains=query))
    return render(request, 'secondary/search_result.html', locals())