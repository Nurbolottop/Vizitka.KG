from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.core.paginator import Paginator
# my imports
from apps.users.models import Subscriber
from apps.index import models
from apps.blog.models import Blog,BigAdvert,NormalAdvert,SmallAdvert,Category
from apps.all_categories import blogs_detail
from apps.secondary.models import Stories
from apps.index.parsing import get_weather_data

# Create your views here.


def blog(request):
    blog = Blog.objects.all().order_by('?')  
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    popular_posts = Blog.objects.order_by('-views')[:5]
    # < start advert >
    big_advert = BigAdvert.objects.reverse().first()
    normal_advert = NormalAdvert.objects.reverse().first()
    small_advert = SmallAdvert.objects.reverse().first()
    stories = Stories.objects.all()
    category = Category.objects.all().order_by("?")[:]
    
    # < end advert >
    temperature, weather_condition = get_weather_data()
    # < end temperature>
    paginator = Paginator(blog, 5)  # Показывать по 5 блогов на каждой странице
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST

        # Проверяем, не подписан ли уже пользователь с таким email
        if not Subscriber.objects.filter(email=email).exists():
            # Если не подписан, создаем новую запись в базе данных
            subscriber = Subscriber(email=email)
            subscriber.save()
            # Затем отправляем подтверждение подписчику
            # send_subscription_email(email)  # Расскомментируйте, если есть функция отправки письма

            return redirect( 'subscribe_done')
        else:
            # Подписчик с таким email уже существует
                return redirect( 'subscribe_nodone')
    return render(request, 'base/page-blog.html', locals())

def blog_detail(request, id):
    setting = models.Settings.objects.latest('id')
    blog = Blog.objects.get(id=id)
    popular_posts = Blog.objects.order_by('-views')[:5]
    current_date = datetime.now()
    temperature, weather_condition = get_weather_data()
    category = Category.objects.all().order_by("?")[:]
    # category in blog detail
    d1 = blogs_detail.d1_method()
    d2 = blogs_detail.d2_method()
    d3 = blogs_detail.d3_method()
    
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST

        # Проверяем, не подписан ли уже пользователь с таким email
        if not Subscriber.objects.filter(email=email).exists():
            # Если не подписан, создаем новую запись в базе данных
            subscriber = Subscriber(email=email)
            subscriber.save()
            # Затем отправляем подтверждение подписчику
            # send_subscription_email(email)  # Расскомментируйте, если есть функция отправки письма

            return redirect( 'subscribe_done')
        else:
            # Подписчик с таким email уже существует
                return redirect( 'subscribe_nodone')
    return render(request, 'detail/page-single-post-creative.html', locals())


        