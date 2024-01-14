from django.db import models
from django_resized.forms import ResizedImageField 

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
        
class Stories(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='stories_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        blank=True, null=True
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,null=True
        )
    permissions = (
            ("can_edit_mymodel", "Can edit MyModel"),
        )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Сторис"
        verbose_name_plural = "Сторисы"

class Partners(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    image = models.ImageField(
        upload_to="partners_image",
        verbose_name="Фотография"
    )
    url = models.URLField(
        verbose_name="Ссылка"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"