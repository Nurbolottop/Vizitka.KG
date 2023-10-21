from django.urls import path
#my imports
from apps.index import views

urlpatterns = [
    path('', views.index,name = "index"),
    path('contacts', views.contact,name = "contact"),
    path('stories/<int:id>/', views.storie,name = "stories"),
]