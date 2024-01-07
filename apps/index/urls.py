from django.urls import path
#my imports
from apps.index import views

urlpatterns = [
    path('', views.index,name = "index"),
    path('contacts', views.contact,name = "contact"),
    path('about', views.about,name = "about"),
    path('stories/<int:id>/', views.storie,name = "stories"),
    path('search', views.search,name = "search"),
    path('subscribe_done', views.subscribe_done,name = "subscribe_done"),
    path('subscribe_nodone', views.subscribe_nodone,name = "subscribe_nodone"),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('ыщ', views.team,name = "team"),
    path('banner', views.banner,name = "banner"),
]