from bs4 import BeautifulSoup
import requests
import re
#from requests.auth import HTTPBasicAuth, HTTPDigestAuth
''''
При парсинге html документов, случается, что инфа доступна только 
зарегистрированным пользователям
Если нужно зарешаться, то используют методы авторизации 
HTTPBasicAuth, HTTPDigestAuth
Зарегался я заранее, необходимо авторизоваться
Для этого необходимо отправить спец запрос в котором укажу параметры авторизации
HTTPBasicAuth - протокол который передается без шифрования (возможно. со слов препода
HTTPDigestAuth - более сложый алгоритм аутентификации, рекомендуется использовать его
'''

#response = requests.get('url', auth = HTTPBasicAuth('your_login, your_password')) # в скобках логин и пароль
''''ПРимер запроса авторизации'''


''''
Лекция 14.4
Парсинг html с помощью Beautiful Soup
'''

URL = 'https://www.drom.ru/reviews/volvo/v40/5kopeek/'

page = requests.get(URL)

print('Статус:', page.status_code)
# print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')

#Найдём все div с отзывами
reviews = soup.find_all('div', class_='b-fix-wordwrap') # "b-fix-wordwrap" я скопировал со страницы в нужном месте

print('Посмотрим количество отзывов:', len(reviews) )
# for rev in reviews:
#     print(rev)
''''
Получим список отзывов, 1 изи 3 - плюсы., 2 изи3 - минусы, 3 из 3 вывод.
Поэтому допилим сортировку
'''

rev_plus = []
rev_minus = []
i = 0
for rev in reviews:
    if i%3 == 0:
        rev_plus.append(rev.text)
        i+=1
    elif i%3 == 1:
        rev_minus.append(rev.text)
        i+=1
    else:
        i+=1
print('\nДолжны быть плюсы:', rev_plus)
print('\nДолжны быть МИНУСЫ:', rev_minus)

# Почему код не выводит одни плюсы?