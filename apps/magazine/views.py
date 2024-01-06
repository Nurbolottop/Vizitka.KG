from django.shortcuts import render,redirect
from datetime import datetime
from apps.index import models
from apps.users.models import Subscriber,Contact
from apps.blog.models import Blog,BigAdvert,SmallAdvert,NormalAdvert,Category
from apps.secondary.models import Stories
from apps.magazine.models import Magazine
from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from apps.index.parsing import get_weather_data
from asgiref.sync import async_to_sync

# Create your views here.
def magazine(request):
    blog = Blog.objects.all().order_by('?')  
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    popular_posts = Blog.objects.order_by('views')[:5]
    temperature, weather_condition = async_to_sync(get_weather_data)()


    # < start advert >
    big_advert = BigAdvert.objects.reverse().first()
    normal_advert = NormalAdvert.objects.reverse().first()
    small_advert = SmallAdvert.objects.reverse().first()
    stories = Stories.objects.all()
    category = Category.objects.all().order_by("?")[:]
    magazines = Magazine.objects.all()
    for magazine in magazines:
        # Используем новый метод для получения URL первой страницы
        magazine.first_page_image_url = magazine.get_first_page_image_url()
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем email из request.POST
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            return redirect( 'subscribe_done')
        else:
                return redirect( 'subscribe_nodone')
    return render(request,"magazine/magazine.html",locals())


def magazine_detail(request, id):
    # try:
        magazine = get_object_or_404(Magazine, id=id)
        
        # Попытка получить URL изображений из кэша
        cache_key = f'magazines_images_{magazine.id}'
        image_urls = cache.get(cache_key)
        
        if not image_urls:
            # Генерация изображений, если они не в кэше
            image_urls = magazine.get_images()
            # Кэширование URL изображений
            cache.set(cache_key, image_urls, timeout=60*60*24)  # Кэш на 24 часа

        # Отрендериваем страницу с изображениями
        return render(request, 'magazine/my_magazine_templates.html', {
            'magazine': magazine,
            'image_urls': image_urls
        })
    # except Exception as e:
    #     # Логирование ошибки или отправка уведомления
    #     # logger.error('Error generating magazine images', exc_info=e)
    #     return HttpResponse('Ошибка при обработке вашего запроса.', status=500)