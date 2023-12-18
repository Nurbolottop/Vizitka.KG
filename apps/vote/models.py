from django.db import models
from django_resized.forms import ResizedImageField 
from django.utils import timezone
from apps.users.models import User  # Убедитесь, что путь до модели User верный
from ckeditor.fields import RichTextField

class Nomination(models.Model):
    name = models.CharField(max_length=200, verbose_name="Номинация")
    start_date = models.DateField(verbose_name="Начало")
    end_date = models.DateField(verbose_name="Окончание")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    order = models.IntegerField(default=100, verbose_name="Порядок / Сортировка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Номинация"
        verbose_name_plural = "Номинации"

class Option(models.Model):
    nomination = models.ForeignKey(Nomination, related_name='options', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 

    def increment_vote(self):
        self.votes += 1
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"

class Vote(models.Model):
    nomination = models.ForeignKey(Nomination, on_delete=models.CASCADE, verbose_name='Номинация', related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    option = models.ForeignKey(Option, on_delete=models.CASCADE, verbose_name='Опция')
    date_voted = models.DateTimeField(auto_now_add=True, verbose_name='Дата голосования')

    class Meta:
        unique_together = ('user', 'option')  # Один пользователь может голосовать за опцию только один раз
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'

    def __str__(self):
        return f"{self.user.username} голосовал за {self.option.name} в номинации {self.nomination.name}"

class Advert(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='blog_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    url = models.URLField(
        verbose_name = "Ссылка",
        blank = True,null = True
    )
    
    def __str__(self):
        return f"{self.url} - {self.image}"
    
    class Meta:
        verbose_name = "Рекалама"
        verbose_name_plural = "Рекаламы"

class Voting(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    end_time = models.DateTimeField('Время окончания голосования')

    def __str__(self):
        return f"Голосование до {self.end_time}"
    
    @property
    def has_ended(self):
        return timezone.now() >= self.end_time