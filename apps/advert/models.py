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
        