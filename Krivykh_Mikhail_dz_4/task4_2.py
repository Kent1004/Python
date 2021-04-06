import requests
from datetime import date
from datetime import datetime

"""Функция вывода курса введенной валюты и даты выставления курса валюты """
def currency_rates (currency):
   """Делаем запрос валют на сайт ЦБ РФ"""
   r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
   """Получаем дату выставления курса ЦБ РФ через поиск и срез"""
   dateRequest = r.text[r.text.find('Date="'):]
   currencyData = datetime.strptime((dateRequest[(dateRequest.find('Date') + 6):(dateRequest.find('Date') + 16)]), "%d.%m.%Y").date()
   """Получаем курс валюты  через поиск и срез"""
   currencyRequest = r.text[r.text.find(currency.upper()):]
   currencyRequest = round(float(currencyRequest[(currencyRequest.find('<Value>')+7):(currencyRequest.find('</Value>'))].replace(',','.')),2)
   print (f'{currencyRequest} , {currencyData}')



currency_rates('usd')
currency_rates ('gbp')
