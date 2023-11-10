from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized.forms import ResizedImageField 
from django.core.mail import send_mail

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер",
        blank=True,null=True
    )
    agree = models.BooleanField(
        default=False,
        
    )
    profile_image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='profile_image/',
        verbose_name="Фотография",
        blank = True, null = True)
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес - город",
        blank=True,null=True
    )
    def __str__(self):
        return self.username 
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        

class Subscriber(models.Model):
    email = models.EmailField(unique=True)  # Поле для хранения email подписчика
    subscribed_at = models.DateTimeField(auto_now_add=True)  # Поле для хранения времени подписки

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Подписчики рассылки"
        verbose_name_plural = "Подписчики рассылки"
        
class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    
    def __str__(self):
        return f"{self.name} - {self.email} - {self.message} "
    
    class Meta:
        verbose_name = "Обратные связи"
        verbose_name_plural = "Обратная связь"
        

class Newsletter(models.Model):
    subject = models.CharField(
        max_length=200,
        verbose_name="Заговолок")
    message = models.TextField(
        verbose_name="Сообщение"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # вызываем оригинальный метод save
        # отправляем рассылку после сохранения объекта
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            send_mail(
                self.subject,
                self.message,
                'from@example.com',
                [subscriber.email],
                fail_silently=False,
            )

    class Meta:
        verbose_name = "Отправить рассылку"
        verbose_name_plural = "Отправить рассылку"
        