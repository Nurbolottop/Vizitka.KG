from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized.forms import ResizedImageField 
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер",
        blank=True,null=True
    )
    agree = models.BooleanField(
        default=False,
        
    )
    profile_image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='profile_image/',
        verbose_name="Фотография",
        blank = True, null = True)
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес - город",
        blank=True,null=True
    )
    def __str__(self):
        return self.username 
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"