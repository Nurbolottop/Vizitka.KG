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
