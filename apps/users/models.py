from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized.forms import ResizedImageField 
from django.core.mail import EmailMessage
from ckeditor.fields import RichTextField
from django.core.mail import send_mail
from apps.blog import models as blog_models
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(
        blank = True, null = True
    )
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
    subject = models.CharField(max_length=200, verbose_name="Заголовок")
    message = RichTextField(verbose_name="Сообщение")
    image = models.ImageField(upload_to='newsletter_images/', blank=True, null=True, verbose_name="Изображение")
    attachment = models.FileField(upload_to='newsletter_attachments/', blank=True, null=True, verbose_name="Вложение")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Вызываем оригинальный метод save
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            email = EmailMessage(
                self.subject,
                self.message,
                'from@example.com',
                [subscriber.email]
            )
            # Прикрепляем изображение, если оно есть
            if self.image:
                email.attach(self.image.name, self.image.read(), 'image/jpeg')
            
            # Прикрепляем другое вложение, если оно есть
            if self.attachment:
                email.attach(self.attachment.name, self.attachment.read(), self.attachment.file.content_type)
            
            email.send(fail_silently=False)

    class Meta:
        verbose_name = "Отправить рассылку"
        verbose_name_plural = "Отправить рассылку"

class ServiceSiteForm(models.Model):
    service = models.CharField(
        max_length=255,
        verbose_name="Название услуги"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
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
        verbose_name = "Заявки на услуги cайта"
        verbose_name_plural = "Заявка на услугу cайта"

class ServiceMagazineForm(models.Model):
    service = models.CharField(
        max_length=255,
        verbose_name="Название услуги"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
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
        verbose_name = "Заявки на услуги магазина"
        verbose_name_plural = "Заявка на услугу магазина"

class Lohi(models.Model):

    name  = models.CharField(
        max_length=255,
        verbose_name="Название услуги"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    def __str__(self):
        return f"{self.post} - {self.name} - {self.message} "
    
    class Meta:
        verbose_name = "Жалобы пользователей"
        verbose_name_plural = "Жалобы пользователей"