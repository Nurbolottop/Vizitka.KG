from django.db import models

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



from apps.users.models import User  # Убедитесь, что путь до модели User верный


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
