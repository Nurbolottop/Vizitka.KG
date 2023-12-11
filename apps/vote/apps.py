from django.apps import AppConfig


class VoteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.vote'
    verbose_name = "Голосование"