from django.db import models
from django_resized.forms import ResizedImageField 
from ckeditor.fields import RichTextField
# Create your models here.
# Category - Категории
class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        
# News - Новости
class Blog(models.Model):
    category = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="blog_category",
        verbose_name="Категории",
        blank=True,null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок "
    )
    sub_title = models.CharField(
        max_length=255,
        verbose_name="Подзаголовок",
        blank=True,null=True
    )
    info_text = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    video = models.FileField(
        upload_to="video_blog/",
        verbose_name="Видео материал",
        blank=True,null=True
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='blog_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True, null=True
    )
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.title} - {self.category}"
    
    def increase_views(self):
        self.views += 1
        self.save()
        
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


        
# Adverts
class BigAdvert(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='bigadvert_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        blank = True, null = True
        
    )
    sub_title = models.CharField(
        max_length=255,
        verbose_name="Подзаголовок",
        blank = True, null = True
        
    )
    url_booking = models.URLField(
        verbose_name="Ссылка",
        blank = True, null = True
        
    )
    
    def __str__(self):
        return f"{self.title} - {self.sub_title}"
    
    class Meta:
        verbose_name = "Добавить рекламу большого масштаба"
        verbose_name_plural = "Добавить рекламу большого масштаба"

        
        
class NormalAdvert(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='normadvert_image/',
        verbose_name="Баннер в размере 970х90 - 1200х120",
        blank = True, null = True
    )
    url_booking = models.URLField(
        verbose_name="Ссылка",
        blank = True, null = True
        
    )
    
    class Meta:
        verbose_name = "Добавить рекламу среднего масштаба "
        verbose_name_plural = "Добавить рекламу среднего масштаба"

class SmallAdvert(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='smalladvert_image/',
        verbose_name="Баннер в размере 250x250",
        blank = True, null = True
    )
    url_booking = models.URLField(
        verbose_name="Ссылка",
        blank = True, null = True
        
    )
    
    class Meta:
        verbose_name = "Добавить рекламу маленького масштаба"
        verbose_name_plural = "Добавить рекламу маленького масштаба"

class Magazine(models.Model):
    image = models.ImageField(
        upload_to="service_magazine",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название услуги'
    )        
    price = models.CharField(
        max_length=255,
        verbose_name="Цена"
    )

    def __str__(self):
        return f"{self.title} - {self.price}"
    
    class Meta:
        verbose_name = "Журнал"
        verbose_name_plural = "Журналы"
        
class Site(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название услуги'
    )        
    price = models.CharField(
        max_length=255,
        verbose_name="Цена"
    )
    
    def __str__(self):
        return f"{self.title} - {self.price}"
    
    class Meta:
        verbose_name = "Сайт"
        verbose_name_plural = "Сайты"

class Banner(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    image = models.ImageField(
        max_length=255,
        verbose_name="Фотография"
    )
    url = models.URLField(
        verbose_name="Ccылка"
    )
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Баннер на главной странице"
        verbose_name_plural = "Баннеры на главной странице"