#bs4 - библиотека для парсинга страниц
import requests
from bs4 import BeautifulSoup # Красивый суп

url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='

day = input('Введите день (Например, 01): ')
month = input('Введите месяц (Например, 01): ')
year = input('Введите год (Например, 2021): ')

url = url + day + '/' + month + '/' + year

response = requests.get(url).content #Каша, в котрой ничего нельзя вытащить отдельно

xml = BeautifulSoup(response, 'html.parser')#Распарсили кашу и получили красивый суп,
                                            # в котором есть отдельный элементы
id = input("Введите ID валюты (RO1235 - USD,RO1335 - KTG,RO1239 - EUR)")

res = xml.find('valute', {'id': id})

# print(response)
# print(xml)
print('Курс на ' + day + '.' + month + '.' + year)
print(res.CharCode.text + ': ' + res.Value.text)