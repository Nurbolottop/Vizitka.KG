from django.shortcuts import render,redirect
from datetime import datetime
from django.core.paginator import Paginator
from django.core.mail import send_mail
from apps.telegram_bot.views import get_text

# my imports
from apps.users.models import Subscriber,ServiceMagazineForm,ServiceSiteForm
from apps.index import models
from apps.blog.models import Blog,BigAdvert,NormalAdvert,SmallAdvert,Category,Site,Magazine
from apps.all_categories import blogs_detail
from apps.secondary.models import Stories
from apps.index.parsing import get_weather_data
from asgiref.sync import async_to_sync

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
    temperature, weather_condition = async_to_sync(get_weather_data)()

    # < end temperature>
    paginator = Paginator(blog, 5)  # Показывать по 5 блогов на каждой странице
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    if request.method == 'POST':
        email = request.POST.get('email') 
        if not Subscriber.objects.filter(email=email).exists():
            # Если не подписан, создаем новую запись в базе данных
            subscriber = Subscriber(email=email)
            subscriber.save()
            get_text(f"""
                            ✅Пользователь подписался на рассылку
                                    
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                        
Почта пользователя: {email}
            """)
            get_text(f"""
                            ✅Пользователь подписался на рассылку
                                    
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                        
Почта пользователя: {email}
            """)
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
    temperature, weather_condition = async_to_sync(get_weather_data)()
    category = Category.objects.all().order_by("?")[:]
    # category in blog detail
    d1 = blogs_detail.d1_method()
    d2 = blogs_detail.d2_method()
    d3 = blogs_detail.d3_method()
    
    if request.method == 'POST':
        email = request.POST.get('email') 
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            get_text(f"""
                            ✅Пользователь подписался на рассылку
                                    
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                        
Почта пользователя: {email}
            """)
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request, 'detail/page-single-post-creative.html', locals())


def magazine_detail(request, id):
    setting = models.Settings.objects.latest('id')
    magazine = Magazine.objects.get(id=id)
    current_date = datetime.now()
    temperature, weather_condition = async_to_sync(get_weather_data)()
    category = Category.objects.all().order_by("?")[:]
    # category in blog detail
    if request.method == 'POST':
        email = request.POST.get('email') 
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            get_text(f"""
                            ✅Пользователь подписался на рассылку
                                    
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                        
Почта пользователя: {email}
            """)
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request, 'servise/magazine_servise.html', locals())

def service_magazine_form(request, id):
    setting = models.Settings.objects.latest('id')
    magazine = Magazine.objects.get(id=id)
    if request.method =="POST":
        if "service_form" in request.POST:
            service = magazine.title
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            ServiceMagazineForm.objects.create(service = service,name = name,phone = phone,email = email,message = message)
            send_mail(
                f'{message}',

                f'Здравствуйте {name},Спасибо за обратную связь, Мы скоро свами свяжемся.Ваще сообщение: {message} Ваша почта: {email}',
                "noreply@somehost.local",
                [email])
            get_text(f"""
                            ✅Пользователь оставил заявку
                                    
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                        
Название услуги: {service}
Имя пользователя: {name}
Почта пользователя: {email}
Тел.ном пользователя: {phone}
Сообщение пользователя: {email}

            """)
            return redirect('banner')
    
    return render(request, 'servise/service_magazine_form.html', locals())


def site_detail(request, id):
    setting = models.Settings.objects.latest('id')
    magazine = Site.objects.get(id=id)
    current_date = datetime.now()
    temperature, weather_condition = async_to_sync(get_weather_data)()
    category = Category.objects.all().order_by("?")[:]
    # category in blog detail
    if request.method == 'POST':
        email = request.POST.get('email') 
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            get_text(f"""
                            ✅Пользователь подписался на рассылку
                                    
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                        
Почта пользователя: {email}
            """)
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request, 'servise/site_servise.html', locals())

def service_site_form(request, id):
    setting = models.Settings.objects.latest('id')
    magazine = Site.objects.get(id=id)
    if request.method =="POST":
        if "service_form" in request.POST:
            service = magazine.title
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            ServiceSiteForm.objects.create(service = service,name = name,phone = phone,email = email,message = message)
            send_mail(
                f'{message}',
                f'Здравствуйте {name},Спасибо за обратную связь, Мы скоро свами свяжемся.Ваще сообщение: {message} Ваша почта: {email}',
                "noreply@somehost.local",
                [email])
            get_text(f"""
                            ✅Пользователь оставил заявку
                                    
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                        
Название услуги: {service}
Имя пользователя: {name}
Почта пользователя: {email}
Тел.ном пользователя: {phone}
Сообщение пользователя: {email}

            """)
            return redirect('banner')
    
    return render(request, 'servise/service_site_form.html', locals())

