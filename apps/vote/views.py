from django.shortcuts import render,redirect
from apps.telegram_bot.views import get_text
from django.core.mail import send_mail

from datetime import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import F, Sum, FloatField, ExpressionWrapper
# my imports
from apps.index import models
from apps.blog.models import BigAdvert,NormalAdvert,SmallAdvert,Category
from apps.index.parsing import get_weather_data
from asgiref.sync import async_to_sync
from apps.vote.models import Nomination, Option,Vote,Advert,VotingInfo
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from apps.blog.models import Blog
from apps.users.models import Subscriber
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
    voting = VotingInfo.objects.first()
    
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

    if request.method == 'POST':
        if "message_send" in request.POST:
            email = request.POST.get('email')  # Получаем email из request.POST
            if not Subscriber.objects.filter(email=email).exists():
                subscriber = Subscriber(email=email)
                subscriber.save()
                return redirect( 'subscribe_done')
            else:
                    return redirect( 'subscribe_nodone')
            
        option_id = request.POST.get('option_id')
        option = get_object_or_404(Option, pk=option_id)
        nomination = option.nomination

        # Вычисляем текущие результаты для номинации
        total_votes = nomination.options.aggregate(total=Sum('votes'))['total'] or 0
        results = list(nomination.options.values('name', 'votes').annotate(
            percentage=ExpressionWrapper(F('votes') * 100 / total_votes, output_field=FloatField())
        ))

        # Проверяем, голосовал ли пользователь
        if Vote.objects.filter(user=request.user, nomination=nomination).exists():
            # Если пользователь уже голосовал, отправляем текущие результаты
            return JsonResponse({'already_voted': True, 'results': results})

        # Если пользователь не голосовал, учитываем его голос
        option.increment_vote()  # Увеличиваем количество голосов
        Vote.objects.create(user=request.user, option=option, nomination=nomination)

        # Пересчитываем результаты после голосования
        total_votes = nomination.options.aggregate(total=Sum('votes'))['total'] or 0
        results = list(nomination.options.values('name', 'votes').annotate(
            percentage=ExpressionWrapper(F('votes') * 100 / total_votes, output_field=FloatField())
        ))

        # Возвращаем обновленные результаты
        return JsonResponse({
            'already_voted': False,
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