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
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Сторис"
        verbose_name_plural = "Сторисы"