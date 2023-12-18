from django.shortcuts import render,redirect
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from django.http import JsonResponse
# my imports
from apps.index import models
from apps.blog.models import BigAdvert,NormalAdvert,SmallAdvert,Category
from apps.index.parsing import get_weather_data
from asgiref.sync import async_to_sync
from apps.vote.models import Nomination, Option,Vote,Advert,Voting
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from apps.blog.models import Blog
# Create your views here.
def vote(request):
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    advert = Advert.objects.latest('id')
    big_advert = BigAdvert.objects.reverse().first()
    normal_advert = NormalAdvert.objects.reverse().first()
    small_advert = SmallAdvert.objects.reverse().first()
    category = Category.objects.all().order_by("?")[:]
    popular_posts = Blog.objects.order_by('-views')[:5]
    temperature, weather_condition = async_to_sync(get_weather_data)()
    #########################################################################
    voting = Voting.objects.first()
    
    # Проверяем, что объект существует и имеет установленное время окончания
    if voting and voting.end_time:
        end_time = voting.end_time
    else:
        # Если объект голосования не найден, можно установить временное значение
        # или обработать эту ситуацию как ошибку
        end_time = datetime.now()  # Это просто пример

    # Передаем в шаблон строку в формате ISO
    context = {'end_time': end_time.isoformat()}
    #########################################################################

    # Логика подсчета
    if request.method == 'POST':
        option_id = request.POST.get('option_id')
        option = get_object_or_404(Option, pk=option_id)
        option.increment_vote()
        nomination = option.nomination
        Vote.objects.create(user=request.user, option=option,nomination=nomination)
        total_votes = sum(o.votes for o in option.nomination.options.all())
        results = [{
            'name': opt.name,
            'votes': opt.votes,
            'percentage': round(opt.votes / total_votes * 100, 2)  
        } for opt in option.nomination.options.all() 
        ]

        return JsonResponse({
            'results': results,
            'total_votes': total_votes
        })

    nominations = Nomination.objects.all()


    # Пагинация 
    nominations_list = Nomination.objects.all()
    paginator = Paginator(nominations_list, 3)  

    page_number = request.GET.get('page')
    nominations = paginator.get_page(page_number)

    return render(request, 'vote/vote.html', locals())