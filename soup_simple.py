from bs4 import BeautifulSoup
import requests
import re

''''
Лекция 14.3.
Парсинг html с помощью BeautifulSoup 
'''



URL = 'https://www.drom.ru/reviews/volvo/v40/5kopeek/'

page = requests.get(URL)

print(page.status_code)
print(page.text)

soup = BeautifulSoup(page.text, 'html.parser') # написал html.parser - потому что можно еще прасить xml документы
print('\nТип объекта:', type(soup))

# Посмотрим заголовок документа
print(soup.title) # вернет объект с первым тегом soup.teg

print('\n',soup.title.string)
print('Тип soup.title.string:', type(soup.title.string))
''''
объект не строка <class 'bs4.element.NavigableString'>
Это объект со специальными возможностями
'''


# если хотим тип Строка, пишем слово text
print('\n', soup.title.text)
print('Тип title.text:', type(soup.title.text))


# Выведем все ссылки с данной html страницы

#получим первую ссылку
print('\n','Первая ссылка:\n',soup.a)
print('Первая ссылка + text:\n',soup.a.text) # вроде должно быть, то что между тегами, но здесь ни чего, поэтому выведется пустота


#что бы получить ссылку, есть спец. метод get
print('ссылка через метод get:\n',soup.a.get('href')) # обращение к атрибуту тега
print('тип метода get:\n', type(soup.a.get('href'))) #<class 'str'>

#возмем все ссылки на данной странице. Метод fine_all
