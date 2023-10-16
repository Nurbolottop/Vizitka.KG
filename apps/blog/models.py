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
    image = models.ImageField(
        upload_to="Image_blog/",
        verbose_name="Фотография"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True, null=True
    )
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.title} - {self.info_text}"
    
    def increase_views(self):
        self.views += 1
        self.save()
        
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
