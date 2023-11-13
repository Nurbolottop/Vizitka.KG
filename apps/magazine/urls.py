from django.urls import path
#my imports
from apps.magazine import views

urlpatterns = [
    path("magazine", views.magazine, name="magazine"),
    path("magazine_detail/<int:id>/", views.magazine_detail, name="magazine_detail"),

    
]