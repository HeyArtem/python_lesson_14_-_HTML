import requests
from bs4 import BeautifulSoup
''''
Изучаю парсинг с
https://www.youtube.com/watch?v=ks64MvZJe0w
код на github: https://github.com/pythontoday/scrap_tutorial

Шаг 1
Спарсим сайт и сохраним ссылки в фаил  "index.html"
'''

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# headers = {
#     "accept": "*/*",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
# }
# ''''
# Как и где и для чего headers?
# Делаетс это для того, что бы немного показать сайту, что мы не бот.
# ОТкрываем хром - Ctr+shift+i - Network - XHR - В столбике Name, открываем get запрос, скрол вниз до accept и копируем это,
# обернув в кавычки, и скролл ниже до user-agent, тоже вставляем, обернув в апострофы
# '''
#
# reg = requests.get(url, headers = headers)
# src = reg.text
# #print(src)
#
# ''''
# Сохраним страницу в фаил, ибо многие сайты не любят, когда их парсят и можно получить бан.
# После созранения в фаил, код записи коментю, потому что он не нужен
# '''
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)



''''
Шаг 2
После того, как соскрабили, записали фаил в переменную и закоментили
Пишем код, который открывает фаил и схр в перемен
'''

with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

all_products_hrefs = soup.find_all(class_= "mzr-tc-group-item-href")
for item in all_products_hrefs:
    print(item) # пробная распечатка полученных ссылок и названий - Божественно!!!
# Обучение парсингу на Python #2 | Парсинг сайтов | Выполняем заказ на фрилансе Продолжить с 5:45