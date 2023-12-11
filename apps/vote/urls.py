from django.urls import path
#my imports
from apps.vote import views

urlpatterns = [
    path("vote", views.vote,  name="vote")
]