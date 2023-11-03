from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from datetime import datetime
# my imports
from apps.index import models
from apps.blog.models import Blog
from apps.advert.models import BigAdvert,NormalAdvert,SmallAdvert
from apps.category_blog import blogs
from apps.blog import blogs_detail

# Create your views here.
# def get_weather_data():
#     url = 'https://yandex.ru/pogoda/bishkek'
#     response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Найти элементы с данными о погоде
#     temperature_element = soup.find('span', class_='temp__value')
#     weather_condition_element = soup.find('div', class_='link__condition')
#     # Другие данные о погоде также можно найти по аналогии

#     # Извлечь текст из элементов
#     temperature = temperature_element.text.strip() if temperature_element else None
#     weather_condition = weather_condition_element.text.strip() if weather_condition_element else None
#     # Другие данные о погоде также могут быть извлечены по аналогии


def blog(request):
    blog = Blog.objects.all().order_by('-views')  
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    popular_posts = Blog.objects.order_by('-views')[:5]
    popular_post = Blog.objects.order_by('-views')[:1]
    # < start advert >
    big_advert = BigAdvert.objects.reverse().first()
    normal_advert = NormalAdvert.objects.reverse().first()
    small_advert = SmallAdvert.objects.reverse().first()
    # < end advert >
    # < start category >
    firstnews1 = blogs.firstnewsblog1_mtehod()
    firstnews3 = blogs.firstnewsblog3_mtehod()
    print(firstnews1)
    # < start temperature>
    # temperature, weather_condition = get_weather_data()
    # < end temperature>
    
    return render(request, 'base/page-blog.html', locals())

def blog_detail(request, id):
    setting = models.Settings.objects.latest('id')
    blog = Blog.objects.get(id=id)
    popular_posts = Blog.objects.order_by('-views')[:5]
    current_date = datetime.now()
    # temperature, weather_condition = get_weather_data()
    
    # category in blog detail
    categoryblogdetail1 = blogs.firstnewsblog1_mtehod()
    categoryblogdetail2 = blogs_detail.firstnewsblogdetail2_mtehod()
    categoryblogdetail3 = blogs_detail.firstnewsblogdetail3_mtehod()
    return render(request, 'detail/page-single-post-creative.html', locals())
        