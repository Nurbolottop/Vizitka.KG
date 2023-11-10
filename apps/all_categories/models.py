from django.db import models

from apps.blog.models import Category
# Create your models here.
# D - Detail
class D1Blog(models.Model):
    first = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="first_title_detail",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    
    class Meta:
        verbose_name = "Изменить категорию для D1"
        verbose_name_plural = "Изменить категорию для D1"
        
class D2Blog(models.Model):
    second = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="second_title_detail",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Изменить категорию для D2"
        verbose_name_plural = "Изменить категорию для D2"
        
       
class D3Blog(models.Model):
    third = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="third_title_detail",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    
    class Meta:
        verbose_name = "Изменить категорию для D3"
        verbose_name_plural = "Изменить категорию для D3"
        
#B - Base

class B1Blog(models.Model):
    first = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="first_title",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Изменить категорию для B1"
        verbose_name_plural = "Изменить категорию для B1"
        

class B2Blog(models.Model):
    second = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="second_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Изменить категорию для B2"
        verbose_name_plural = "Изменить категорию для B2"

class B3Blog(models.Model):
    third = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="third_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Изменить категорию для B3"
        verbose_name_plural = "Изменить категорию для B3"
        
class B4Blog(models.Model):
    four = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="four_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Изменить категорию для B4"
        verbose_name_plural = "Изменить категорию для B4"
        
class B5Blog(models.Model):
    five_one = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="five_one_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Изменить категорию для B5"
        verbose_name_plural = "Изменить категорию для B5"

class B6Blog(models.Model):
    five_two = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="five_two_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Изменить категорию для B6"
        verbose_name_plural = "Изменить категорию для B6"

class B7Blog(models.Model):
    five_three = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="five_three_category",
        verbose_name="Категория которую будете отображать",
        blank=True,null=True
    )
    class Meta:
        verbose_name = "Изменить категорию для B7"
        verbose_name_plural = "Изменить категорию для B7"