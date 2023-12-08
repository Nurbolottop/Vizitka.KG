import aiohttp
from bs4 import BeautifulSoup
import asyncio

# Асинхронная функция для получения содержимого страницы
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

# Асинхронные функции парсинга для каждой валюты
async def dollar_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/dollar/'
    content = await fetch(url)
    soup = BeautifulSoup(content, 'html.parser')
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    h2_element = div_element.find('h2') if div_element else None
    return h2_element.text.strip() if h2_element else None

async def euro_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/euro/'
    content = await fetch(url)
    soup = BeautifulSoup(content, 'html.parser')
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    h2_element = div_element.find('h2') if div_element else None
    return h2_element.text.strip() if h2_element else None

async def rub_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/ruble/'
    content = await fetch(url)
    soup = BeautifulSoup(content, 'html.parser')
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    h2_element = div_element.find('h2') if div_element else None
    return h2_element.text.strip() if h2_element else None

async def tenge_pars():
    url = 'https://www.akchabar.kg/ru/exchange-rates/tenge/'
    content = await fetch(url)
    soup = BeautifulSoup(content, 'html.parser')
    div_element = soup.find('div', class_='nbkr_tabs_wrapper')
    h2_element = div_element.find('h2') if div_element else None
    return h2_element.text.strip() if h2_element else None

# Асинхронная функция парсинга погоды
async def get_weather_data():
    url = 'https://yandex.ru/pogoda/bishkek'
    content = await fetch(url)
    soup = BeautifulSoup(content, 'html.parser')
    temperature_element = soup.find('span', class_='temp__value')
    weather_condition_element = soup.find('div', class_='link__condition')
    temperature = temperature_element.text.strip() if temperature_element else None
    weather_condition = weather_condition_element.text.strip() if weather_condition_element else None
    return temperature, weather_condition
