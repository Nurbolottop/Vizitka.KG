from django.apps import AppConfig


class SecondaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.secondary'
    verbose_name = "B) Дополнительные параметры"
