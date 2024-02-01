from django.urls import path
#my imports
from apps.blog import views

urlpatterns = [
    path('blog/<int:id>/', views.blog_detail,name = "blog_detail"),
    path('copy_link_to_clipboard/', views.copy_link_to_clipboard, name='copy_link_to_clipboard'),
    path('magazine/<int:id>/', views.magazine_detail,name = "magazine_detail"),
    path('site/<int:id>/', views.site_detail,name = "site_detail"),
    path('blog', views.blog,name = "blog"),
    path('service_site_form/<int:id>/', views.service_site_form,name = "service_site_form"),
    path('service_magazine_form/<int:id>/', views.service_magazine_form,name = "service_magazine_form"),

]