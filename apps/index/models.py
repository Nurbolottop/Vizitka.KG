from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField 

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип для темного фона"
    )
    logo_white = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип для темного фона"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Телефон номер'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта'
        )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    whatsapp = models.URLField(
        verbose_name='Whatspp URL',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram URL',
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name='Youtube URL',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook URL',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Основная настройка"
            verbose_name_plural = "Основные настройки"
            

class About(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='about_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    date = models.CharField(
        max_length=255,
        verbose_name="С какого года начали работать ?"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Добавить о нас"
        verbose_name_plural = "Добавить о нас"
        
class Banner(models.Model):
    
    title = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Рекламодателям"
        verbose_name_plural = "Рекламодателям"
        
