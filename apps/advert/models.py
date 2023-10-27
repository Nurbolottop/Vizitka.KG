from django.db import models
from django_resized.forms import ResizedImageField 

# Create your models here.
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
        verbose_name = "Большая реклама"
        verbose_name_plural = "Большие рекламы"

        
        
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
        verbose_name = "Cредняя реклама"
        verbose_name_plural = "Средние рекламы"

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
        verbose_name = "Маленькая реклама"
        verbose_name_plural = "Маленькие рекламы"