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
print('page.text:',page.text)

soup = BeautifulSoup(page.text, 'html.parser') # написал html.parser - потому что можно еще прасить xml документы
print('\nТип объекта:', type(soup))

# Посмотрим заголовок документа
print(soup.title) # вернет объект с первым тегом soup.teg

print('\n',soup.title.string)
print('Тип soup.title.string:', type(soup.title.string))
''''
объект не строка <class 'bs4.element.NavigableString'>
Это строка со специальными возможностями
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
a_tags = soup.find_all('a')
print("\n Все ссылки на данной странице., soup.find_all('a'):",  a_tags)
print('Тип a_tags:',type(a_tags))
print('Количество ссылок:', len(a_tags))


print('\nВсе ссылки аккуратненько:')
for ref in a_tags:
    print(ref.get('href'))



# Решим эту задачу с помощью регулярных выражений ( без бьютисупа, обрабатывать будем page.text)
pattern = r'https?://[\S]+' # знак вопроса т.к. кроме http, есть https, т.е. s может быть, а может не быть. [\s]+любой непробельный символ с плюсом
ref_all = re.findall(pattern, page.text)

print('\nРаспечатаем ref_all:', ref_all)
print(len(ref_all))

print('\nВторой вариант вывода ссылок')
for ref in ref_all:
    print(ref) # Вывовд: с помощью бьтифул суп выборка чище




# найдём все блоки div
div_tags = soup.find_all('div')
print('\nКоличество div_tags:', len(div_tags))
#print('Распечатаю все div_tags:', div_tags)