from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
# my imports
from apps.index import models
from datetime import datetime

from apps.blog.models import Blog
from apps.advert.models import BigAdvert

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
    blog = Blog.objects.all()  
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    popular_posts = Blog.objects.order_by('-views')[:5]
    popular_posts = Blog.objects.order_by('-views')[:5]
    
    big_advert = BigAdvert.objects.latest('id')
    # temperature, weather_condition = get_weather_data()
    return render(request, 'base/page-blog.html', locals())

def blog_detail(request, id):
    setting = models.Settings.objects.latest('id')
    blog = Blog.objects.get(id=id)
    popular_posts = Blog.objects.order_by('-views')[:5]
    current_date = datetime.now()
    # temperature, weather_condition = get_weather_data()
    return render(request, 'detail/page-single-post-creative.html', locals())
        