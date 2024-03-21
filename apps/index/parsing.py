import requests
from bs4 import BeautifulSoup
from apps.secondary.models import Currency, Weather

def fetch(url):
    response = requests.get(url)
    return response.text

def parse_currency():
    dollar = dollar_pars()
    euro = euro_pars()
    rub = rub_pars()
    tenge = tenge_pars()
    
    currency, created = Currency.objects.get_or_create(
        defaults={
            'dollar': dollar,
            'euro': euro,
            'rub': rub,
            'tenge': tenge,
        }
    )
    if not created:
        currency.dollar = dollar
        currency.euro = euro
        currency.rub = rub
        currency.tenge = tenge
        currency.save()

def parse_weather():
    temperature, condition = get_weather_data()
    
    weather, created = Weather.objects.get_or_create(
        defaults={
            'title': f"{temperature}°C, {condition}",
        }
    )
    if not created:
        weather.title = f"{temperature}°C, {condition}"
        weather.save()

def dollar_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/dollar/'
    content = fetch(url)
    soup = BeautifulSoup(content, 'html.parser')
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    h2_element = div_element.find('h2') if div_element else None
    return h2_element.text.strip() if h2_element else None

def euro_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/euro/'
    content = fetch(url)
    soup = BeautifulSoup(content, 'html.parser')
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    h2_element = div_element.find('h2') if div_element else None
    return h2_element.text.strip() if h2_element else None

def rub_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/ruble/'
    content = fetch(url)
    soup = BeautifulSoup(content, 'html.parser')
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    h2_element = div_element.find('h2') if div_element else None
    return h2_element.text.strip() if h2_element else None

def tenge_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/tenge/'
    content = fetch(url)
    soup = BeautifulSoup(content, 'html.parser')
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    h2_element = div_element.find('h2') if div_element else None
    return h2_element.text.strip() if h2_element else None

def get_weather_data():
    url = 'https://yandex.ru/pogoda/bishkek'
    content = fetch(url)
    soup = BeautifulSoup(content, 'html.parser')
    temperature_element = soup.find('span', class_='temp__value')
    weather_condition_element = soup.find('div', class_='link__condition')
    temperature = temperature_element.text.strip() if temperature_element else None
    weather_condition = weather_condition_element.text.strip() if weather_condition_element else None
    return temperature, weather_condition
