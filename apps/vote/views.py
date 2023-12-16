from django.shortcuts import render,redirect
from datetime import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse
# my imports
from apps.index import models
from apps.blog.models import BigAdvert,NormalAdvert,SmallAdvert,Category
from apps.index.parsing import get_weather_data
from asgiref.sync import async_to_sync
from apps.vote.models import Nomination, Option
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.
def vote(request):
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    big_advert = BigAdvert.objects.reverse().first()
    normal_advert = NormalAdvert.objects.reverse().first()
    small_advert = SmallAdvert.objects.reverse().first()
    category = Category.objects.all().order_by("?")[:]

    temperature, weather_condition = async_to_sync(get_weather_data)()
    #########################################################################


    if request.method == 'POST':
        option_id = request.POST.get('option_id')
        option = get_object_or_404(Option, pk=option_id)
        option.increment_vote()

        # Подсчет результатов для номинации
        total_votes = sum(o.votes for o in option.nomination.options.all())
        results = [{
            'name': opt.name,
            'votes': opt.votes,
            'percentage': round(opt.votes / total_votes * 100, 2)  # Округление до двух знаков после запятой
        } for opt in option.nomination.options.all()]

        # Возвращаем JSON с результатами
        return JsonResponse({
            'results': results,
            'total_votes': total_votes
        })

    # Если это не POST запрос, просто отобразите страницу с формами
    nominations = Nomination.objects.all()

    return render(request, 'vote/vote.html', locals())