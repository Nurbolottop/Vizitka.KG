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
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='service/',
        verbose_name="Баннер в размере 267х189",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название услуги'
    )        
    price = models.CharField(
        max_length=255,
        verbose_name="Цена"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    
    def __str__(self):
        return f"{self.title} - {self.price}"
    
    class Meta:
        verbose_name = "Услуга Журнала"
        verbose_name_plural = "Услуги Журнала"
        
class MagazineImage(models.Model):
    settings = models.ForeignKey(Magazine, related_name='magazine_image', on_delete=models.CASCADE)
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='service/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    class Meta:
        unique_together = ('settings', 'image')
        verbose_name = "Дополнительная фотограя баннера в размере 267х189"
        verbose_name_plural = "Дополнительная фотограя баннера в размере 267х189"

################################################################################################################################################################################

class Site(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='service/',
        verbose_name="Баннер в размере 267х189",
        blank = True, null = True
    )
    title = models.CharField(   
        max_length=255,
        verbose_name='Название услуги'
    )        
    price = models.CharField(
        max_length=255,
        verbose_name="Цена"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    def __str__(self):
        return f"{self.title} - {self.price}"
    
    class Meta:
        verbose_name = "Услуга Сайта"
        verbose_name_plural = "Услуги Сайта"

class SiteImage(models.Model):
    settings = models.ForeignKey(Site, related_name='site_image', on_delete=models.CASCADE)
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='service/',
        verbose_name="Фотография ",
        blank = True, null = True
    )
    class Meta:
        unique_together = ('settings', 'image')
        verbose_name = "Дополнительная фотограя сайта"
        verbose_name_plural = "Дополнительная фотограя баннера"

################################################################################################################################################################################

class Banner(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='banner/',
        verbose_name="Баннер в размере ",
        blank = True, null = True
    )
    url = models.URLField(
        verbose_name="Ccылка"
    )
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Баннер на главной странице"
        verbose_name_plural = "Баннеры на главной странице"

