from django.core.management.base import BaseCommand
from apps.secondary.models import Currency, Weather
from apps.index.parsing import dollar_pars, euro_pars, rub_pars, tenge_pars, get_weather_data

class Command(BaseCommand):
    help = 'Обновить данные о валюте и погоде'

    def handle(self, *args, **options):
        self.update_data()

    def update_data(self):
        # Получить данные о валюте
        dollar = dollar_pars()
        euro = euro_pars()
        rub = rub_pars()
        tenge = tenge_pars()

        # Сохранить данные о валюте в базе данных
        currency_instance, _ = Currency.objects.get_or_create(
            defaults={
                'dollar': dollar,
                'euro': euro,
                'rub': rub,
                'tenge': tenge,
            }
        )
        if not currency_instance:
            currency_instance.dollar = dollar
            currency_instance.euro = euro
            currency_instance.rub = rub
            currency_instance.tenge = tenge
            currency_instance.save()

        # Получить данные о погоде
        temperature, weather_condition = get_weather_data()

        # Сохранить данные о погоде в базе данных
        weather_instance, _ = Weather.objects.get_or_create(
            defaults={
                'temperature': temperature,
                'weather_condition': weather_condition,
            }
        )
        if not weather_instance:
            weather_instance.temperature = temperature
            weather_instance.weather_condition = weather_condition
            weather_instance.save()

        self.stdout.write(self.style.SUCCESS('Данные успешно обновлены'))


from django.utils import timezone

current_time = timezone.now()
print("Текущее время:", current_time)
