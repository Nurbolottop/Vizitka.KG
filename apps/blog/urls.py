from django.urls import path
#my imports
from apps.blog import views

urlpatterns = [
    path('blog/<int:id>/', views.blog_detail,name = "blog_detail"),
    path('blog', views.blog,name = "blog"),
    
]