from django.shortcuts import render,redirect
import requests
# my imports
from apps.index import models
from apps.blog.models import Blog
from datetime import datetime
from apps.advert.models import BigAdvert

# Create your views here.

def index(request):
    blog = Blog.objects.all()
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    latest_news = Blog.objects.order_by('-created_at')[:5]
    latest_new = Blog.objects.order_by('-created_at')[:1]
    popular_posts = Blog.objects.order_by('-views')[:3]
    popular_post = Blog.objects.order_by('-views')[:1]
    big_advert = BigAdvert.objects.latest('id')
    api_url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        # Проверяем наличие ключа 'rates' в ответе
        if 'rates' in data:
            usd_rate = data['rates']['USD']
            rub_rate = data['rates']['RUB']
            eur_rate = data['rates']['EUR']
    
    return render(request, 'base/home-default.html', locals())

def contact(request):
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    return render(request, 'base/page-contact.html', locals())