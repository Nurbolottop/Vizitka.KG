#Libraryes
from django.shortcuts import render,redirect
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator
from django.core.mail import send_mail
#Files
from apps.index import models

# Classes
from apps.blog.models import Blog,BigAdvert,NormalAdvert,SmallAdvert,Category,Site,Magazine,Banner
from apps.users.models import Subscriber,Contact
from apps.secondary.models import Team,History,Stories,Partners
# Functions

from apps.index.parsing import dollar_pars,euro_pars,rub_pars,tenge_pars,get_weather_data
from apps.blog import blogs 
from asgiref.sync import async_to_sync

# Create your views here.
def index(request):
    current_date = datetime.now()
    dollar_rate = async_to_sync(dollar_pars)()
    euro_rate = async_to_sync(euro_pars)()
    ruble_rate = async_to_sync(rub_pars)()
    tenge_rate = async_to_sync(tenge_pars)()
    temperature, weather_condition = async_to_sync(get_weather_data)()

    setting = models.Settings.objects.latest('id')
    category = Category.objects.all().order_by("?")[:]
    
    team = Team.objects.all()
    stories = Stories.objects.all()
    big_advert = BigAdvert.objects.reverse().first()
    normal_advert = NormalAdvert.objects.reverse().first()
    small_advert = SmallAdvert.objects.reverse().first()
    banner = Banner.objects.all()

    blog = Blog.objects.all().order_by("?")[:]
    latest_news = Blog.objects.order_by('-created_at')[:5]
    latest_new = Blog.objects.order_by('-created_at')[:1]
    popular_posts = Blog.objects.order_by('-views')[:3]
    popular_post = Blog.objects.order_by('-views')[:1]

    first_blog1 = blogs.B1Blog1_mtehod()
    first_blog3 = blogs.B1Blog3_mtehod()
    second_blog1 = blogs.B2Blog1_mtehod()
    second_blog2 = blogs.B2Blog2_mtehod()
    second_blog4 = blogs.B2Blog4_mtehod()
    third_blog1 = blogs.B3Blog1_mtehod()
    four_blog1 = blogs.B4Blog1_mtehod()
    four_blog2 = blogs.B4Blog3_mtehod()
    fiveone_blog1 = blogs.fiveone1_mtehod()
    fiveone_blog2 = blogs.fiveone2_mtehod()
    fivetwo_blog1 = blogs.fivetwo1_mtehod()
    fivetwo_blog2 = blogs.fivetwo2_mtehod()
    fivethree_blog1 = blogs.fivethree1_mtehod()
    fivethree_blog2 = blogs.fivethree2_mtehod()
    
                

    
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request, 'base/home-default.html', locals())

def category_view(request, category_id):
    current_date = datetime.now()
    temperature, weather_condition = async_to_sync(get_weather_data)()
    setting = models.Settings.objects.latest('id')
    category = Category.objects.all().order_by("?")[:]
    

    big_advert = BigAdvert.objects.reverse().first()
    normal_advert = NormalAdvert.objects.reverse().first()
    small_advert = SmallAdvert.objects.reverse().first()
    stories = Stories.objects.all()
    
    categorys = Category.objects.get(id=category_id)
    popular_posts = Blog.objects.order_by('-views')[:5]
    blog = Blog.objects.filter(category=categorys)
    paginator = Paginator(blog, 5)  # Показывать по 5 блогов на каждой странице
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request, 'secondary/category.html',locals())

def storie(request,id):
    category = Category.objects.all().order_by("?")[:]
    setting = models.Settings.objects.latest('id')
    
    stories_all = Stories.objects.exclude(id=id)
    stories = Stories.objects.get(id=id)
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request, 'base/stories.html', locals())

def contact(request):
    current_date = datetime.now()
    temperature, weather_condition = async_to_sync(get_weather_data)()
    setting = models.Settings.objects.latest('id')
    category = Category.objects.all().order_by("?")[:]
    if request.method =="POST":
        if "contact_send" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            Contact.objects.create(name = name,email = email,message = message)
            send_mail(
                f'{message}',

                f'Здравствуйте {name},Спасибо за обратную связь, Мы скоро свами свяжемся.Ваще сообщение: {message} Ваша почта: {email}',
                "noreply@somehost.local",
                [email])
            
            return redirect('index')
        context = {
            "setting":setting
        }
        if "message_send" in request.POST:
            email = request.POST.get('email')  # Получаем email из request.POST
            if not Subscriber.objects.filter(email=email).exists():
                subscriber = Subscriber(email=email)
                subscriber.save()
                return redirect( 'subscribe_done')
            else:
                    return redirect( 'subscribe_nodone')
    return render(request, 'base/page-contact.html', locals())

def about(request):
    current_date = datetime.now()
    temperature, weather_condition = async_to_sync(get_weather_data)()
    
    setting = models.Settings.objects.latest('id')
    about = models.About.objects.latest('id')
    history = History.objects.all()
    team = Team.objects.all()
    partner = Partners.objects.all()
    category = Category.objects.all().order_by("?")[:]
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request,'base/page-about.html', locals())

def search(request):
    current_date = datetime.now()
    temperature, weather_condition = async_to_sync(get_weather_data)()
    setting = models.Settings.objects.latest('id')
    category = Category.objects.all().order_by("?")
    
    popular_posts = Blog.objects.order_by('-views')[:5]
    
    query = request.GET.get('query', '')
    blogs = []
    if query:
        blog_results = Blog.objects.filter(
            Q(title__icontains=query) | 
            Q(sub_title__icontains=query) | 
            Q(category__title__icontains=query)
        )
        paginator = Paginator(blog_results, 5)
        page = request.GET.get('page')
        blogs = paginator.get_page(page)
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request, 'secondary/search_result.html', locals())

def subscribe_done(request):
    current_date = datetime.now()
    temperature, weather_condition = async_to_sync(get_weather_data)()
    category = Category.objects.all().order_by("?")[:]
    setting = models.Settings.objects.latest('id')
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request, 'subscribe/subscribe_done.html', locals())

def subscribe_nodone(request):
    current_date = datetime.now()
    temperature, weather_condition = async_to_sync(get_weather_data)()
    category = Category.objects.all().order_by("?")[:]
    setting = models.Settings.objects.latest('id')
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request, 'subscribe/subscribe_nodone.html', locals())


def team(request):
    # current_date = datetime.now()
    # temperature, weather_condition = get_weadher_data()
    category = Category.objects.all().order_by("?")[:]
    setting = models.Settings.objects.latest('id')
    team = Team.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request,'base/page-team.html', locals())

def banner(request):
    current_date = datetime.now()
    temperature, weather_condition = async_to_sync(get_weather_data)()
    setting = models.Settings.objects.latest('id')
    category = Category.objects.all().order_by("?")[:]
    
    magazine = Magazine.objects.all()
    site = Site.objects.all()
    
    banner = models.Banner.objects.latest("id")
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request,"secondary/banner.html", locals())