from django.db import models

# Create your models here.
class Magazine(models.Model):
    title  = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    document = models.FileField(
        verbose_name="Журнал"
    )
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Журналы"
        verbose_name_plural = "Журнал"