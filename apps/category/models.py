from django.db import models

from apps.blog.models import Category
# Create your models here.
class FirstBlog(models.Model):
    first = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="first_title",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Первый блог"
        verbose_name_plural = "Первые блоги"
        

class SecondBlog(models.Model):
    second = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="second_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Второй блог"
        verbose_name_plural = "Вторые блоги"

class ThirdBlog(models.Model):
    third = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="third_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Третий блог"
        verbose_name_plural = "Третий блог"
        
class FourBlog(models.Model):
    four = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="four_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Четвертый блог"
        verbose_name_plural = "Четвертый блог"
        
class FiveOneBlog(models.Model):
    five_one = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="five_one_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Пятый блог - Первый пункт"
        verbose_name_plural = "Пятый блог - Первый пункт"

class FiveTwoBlog(models.Model):
    five_two = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="five_two_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Пятый блог - Второй пункт"
        verbose_name_plural = "Пятый блог - Второй пункт"

class FiveThreeBlog(models.Model):
    five_three = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="five_three_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Пятый блог - Третий пункт"
        verbose_name_plural = "Пятый блог - Третий пункт"