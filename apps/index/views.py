from django.shortcuts import render,redirect


# my imports
from apps.index.models import Settings
# Create your views here.

def index(request):
    setting = Settings.objects.latest('id')
    return render(request, 'base/home-default.html', locals())

def contact(request):
    setting = Settings.objects.latest('id')
    return render(request, 'base/page-contact.html', locals())