from django.db import models
from apps.blog.models import Category

# Create your models here.
class FirsNewsBlog(models.Model):
    first = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="firstnews_title",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Первый блог"
        verbose_name_plural = "Первый блоги"
