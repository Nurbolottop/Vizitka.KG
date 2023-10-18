from django.db import models

# Create your models here.
class BigAdvert(models.Model):
    image = models.ImageField(
        upload_to="images_advert",
        verbose_name="Фотографии"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    sub_title = models.CharField(
        max_length=255,
        verbose_name="Подзаголовок"
    )
    url_booking = models.URLField(
        verbose_name="Ссылка"
    )
    
    def __str__(self):
        return f"{self.title} - {self.sub_title}"
    
    class Meta:
        verbose_name = "Большая реклама"
        verbose_name_plural = "Большие рекламы"
        
class NormalAdvert(models.Model):
    image = models.ImageField(
        upload_to="normaladvert_image",
        verbose_name="Баннер в размере 970х90 - 1200х120"
    )
    url_booking = models.URLField(
        verbose_name="Ссылка"
    )
    
    class Meta:
        verbose_name = "Cредняя реклама"
        verbose_name_plural = "Средние рекламы"

class SmallAdvert(models.Model):
    image = models.ImageField(
        upload_to="smalladvert_image",
        verbose_name="Баннер в размере 250x250"
    )
    url_booking = models.URLField(
        verbose_name="Ссылка"
    )
    
    class Meta:
        verbose_name = "Маленькая реклама"
        verbose_name_plural = "Маленькие рекламы"