from django.db import models
from django_resized.forms import ResizedImageField 
from ckeditor.fields import RichTextField

# Create your models here.
class Team(models.Model):
    image  = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='team_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    work = models.CharField(
        max_length=255,
        verbose_name="Профессия"
    )
    
    def __str__(self):
        return f"{self.name} - {self.work}"
    
    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша комманды"
    
class History(models.Model):
    year = models.CharField(
        max_length=255,
        verbose_name="Год"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    
    def __str__(self):
        return f"{self.title} - {self.year}"
    
    class Meta:
        verbose_name = "Наша история"
        verbose_name_plural = "Наши истории"
        

class Partners(models.Model):
    image = models.ImageField(
        upload_to="partners_image",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    location = models.CharField(
        max_length = 255,
        verbose_name = "Адрес"
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = "Телефонный номер"
    )
    email = models.EmailField(
        verbose_name = "Почта"
    )
    url = models.URLField(
        verbose_name="Ссылка"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"
        
        

# Parsing
class Currency(models.Model):
    dollar = models.CharField(
        verbose_name = "Доллар",
        max_length = 255
    )
    euro = models.CharField(
        verbose_name = "Евро",
        max_length = 255
    )
    rub = models.CharField(
        verbose_name = "Рубль",
        max_length = 255
    )
    tenge = models.CharField(
        verbose_name = "Тенге",
        max_length = 255
    )
    
    
    def __str__(self):
        return self.dollar
    
    class Meta:
        verbose_name = "Курс валют"
        verbose_name_plural = "Курс валют"
        
class Weather(models.Model):
    temperature = models.CharField(
        max_length = 255,
        verbose_name = "Температура",
        null=True  # Разрешаем пустое значение
        
    )
    weather_condition = models.CharField(
        max_length=255,
        verbose_name="Погода",
        null=True  # Разрешаем пустое значение
    )

    
    class Meta:
        verbose_name = "Погода"
        verbose_name_plural = "Погода"