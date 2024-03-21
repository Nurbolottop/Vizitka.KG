from django.urls import path
#my imports
from apps.index import views

urlpatterns = [
    path('', views.index,name = "index"),
    path('contacts', views.contact,name = "contact"),
    path('about', views.about,name = "about"),
    path('search', views.search,name = "search"),
    path('subscribe_done', views.subscribe_done,name = "subscribe_done"),
    path('subscribe_nodone', views.subscribe_nodone,name = "subscribe_nodone"),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('wooow', views.team,name = "team"),
    path('banner', views.banner,name = "banner"),
    path('partners', views.partners,name = "partners"),
    path('partners_detail/<int:id>/', views.partners_detail,name = "partners_detail"),
    
    
]