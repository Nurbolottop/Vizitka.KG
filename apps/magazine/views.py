from django.shortcuts import render
from datetime import datetime
from apps.index import models
from apps.blog.models import Blog,BigAdvert,SmallAdvert,NormalAdvert,Category
from apps.secondary.models import Stories
from apps.magazine.models import Magazine
from django.shortcuts import render, get_object_or_404

# Create your views here.
def magazine(request):
    blog = Blog.objects.all().order_by('?')  
    current_date = datetime.now()
    setting = models.Settings.objects.latest('id')
    popular_posts = Blog.objects.order_by('views')[:5]
    # < start advert >
    big_advert = BigAdvert.objects.reverse().first()
    normal_advert = NormalAdvert.objects.reverse().first()
    small_advert = SmallAdvert.objects.reverse().first()
    stories = Stories.objects.all()
    category = Category.objects.all().order_by("?")[:]
    magazine = Magazine.objects.all()
    return render(request,"magazine/magazine.html",locals())


def magazine_detail(request, id):
    magazine = get_object_or_404(Magazine, id=id)
    return render(request, 'magazine/magazine_detail.html', locals())
