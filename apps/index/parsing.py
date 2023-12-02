import requests
from bs4 import BeautifulSoup
# Create your views here.
def dollar_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/dollar/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Найти <h2> внутри <div> с классом 'nbkr_tabs_wrapper'
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    if div_element:
        h2_element = div_element.find('h2')
        if h2_element:
            h2_text = h2_element.text.strip()
            return h2_text
    return None

def euro_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/euro/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Найти <h2> внутри <div> с классом 'nbkr_tabs_wrapper'
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    if div_element:
        h2_element = div_element.find('h2')
        if h2_element:
            h2_text = h2_element.text.strip()
            return h2_text
    return None

def rub_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/ruble/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Найти <h2> внутри <div> с классом 'nbkr_tabs_wrapper'
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    if div_element:
        h2_element = div_element.find('h2')
        if h2_element:
            h2_text = h2_element.text.strip()
            return h2_text
    return None

def tenge_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/tenge/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Найти <h2> внутри <div> с классом 'nbkr_tabs_wrapper'
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    if div_element:
        h2_element = div_element.find('h2')
        if h2_element:
            h2_text = h2_element.text.strip()
            return h2_text
    return None

def get_weather_data():
    url = 'https://yandex.ru/pogoda/bishkek'
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, 'html.parser')

    # Найти элементы с данными о погоде
    temperature_element = soup.find('span', class_='temp__value')
    weather_condition_element = soup.find('div', class_='link__condition')
    # Другие данные о погоде также можно найти по аналогии

    # Извлечь текст из элементов
    temperature = temperature_element.text.strip() if temperature_element else None
    weather_condition = weather_condition_element.text.strip() if weather_condition_element else None
    # Другие данные о погоде также могут быть извлечены по аналогии

    return temperature, weather_condition


