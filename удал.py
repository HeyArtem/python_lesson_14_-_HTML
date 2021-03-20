# scraper.py
'''
Изучаю парсинг
https://pythonru.com/biblioteki/parsing-na-python-s-beautiful-soup

Beautiful Soup — это библиотека Python для извлечения данных из файлов HTML и XML.
Она работает с вашим любимым парсером, чтобы дать вам естественные способы навигации,
поиска и изменения дерева разбора. Она обычно экономит программистам часы и дни работы.

Beautiful Soup поддерживает парсер HTML, включенный в стандартную библиотеку Python,
а также ряд сторонних парсеров на Python. Одним из них является парсер lxml.

'''
import requests
from bs4 import BeautifulSoup

# '''
# Спарсил всю страницу целиком
# '''
#
# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# # print(soup)
#
#
#
#
# url = 'https://quotes.toscrape.com/'
# '''
# Спарсю все цитаты N1
# Здесь будет не удобочитаемый вывод текста
# '''
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('span', class_='text')
# print('Спарсю все цитаты N1:', quotes)
#
#
#
#
#
#
# url = 'https://quotes.toscrape.com/'
# '''
# Спарсю все цитаты N2
# Здесь цикл и при выводе к переменной прибавил  text
# '''
# print('\nСпарсю все цитаты N2')
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('span', class_='text')
# for quote in quotes:
#     print(quote.text)
#
#
#
#
# ''''
# Спарсю авторов
# '''
# url = 'https://quotes.toscrape.com/'
#
# print('\nСпарсю авторов:')
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('small', class_='author')
# for quote in quotes:
#     print(quote.text)
#
#
#
# ''''
# Спарсю одновременно цитаты и авторов
# И самому не получилось!!
# '''
# url = 'https://quotes.toscrape.com/'
#
# print('\nСпарсю Циататы + авторов САМ:')
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('span', class_='text')
# quotes_2 = soup.find_all('small', class_='author')
# for quote in quotes:
#     print(quote.text)
#
# for quote_2  in quotes_2:
#     print(quote_2.text)
#
#
#
#
# ''''
# Спарсю одновременно цитаты и авторов
#
# '''
# url = 'https://quotes.toscrape.com/'
#
# print('\nСпарсю Циататы + авторов:')
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_='author')
#
# for i in range(0, len(quotes)):
#     print(quotes[i].text)
#     print('---', authors[i].text)
#
#
#
#
# ''''
# Спарсю теги сам
#
# '''
# url = 'https://quotes.toscrape.com/'
#
# print('\nСпарсю Спарсю ТЕГИ сам:')
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# tags = soup.find_all('div', class_='tags')
# for tag in tags:
#     print(tag.text)



#
# ''''
# Спарсю Цитату, Автора, Теги
# Моё решение
# '''
# url = 'https://quotes.toscrape.com/'
#
# print('\n - Спарсю Цитату, Автора, Теги (Моё решение):')
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_='author')
# tags = soup.find_all('div', class_='tags')
#
# for i in range(0, len(quotes)):
#     print(quotes[i].text)
#     print('---', authors[i].text)
#     print(tags[i].text)
#     print('\n')
#
#
#
#
# ''''
# Спарсю Цитату, Автора, Теги
#
# '''
# url = 'https://quotes.toscrape.com/'
#
# print('\n - Спарсю Цитату, Автора, Теги:')
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_='author')
# tags = soup.find_all('div', class_='tags')
#
# for i in range(0, len(quotes)):
#     print(quotes[i].text)
#     print('---', authors[i].text)
#     tagsforsquote = tags[i].find_all('a', class_='tag')
#     for tag_forsquote in tagsforsquote:
#         print(tag_forsquote.text)
#     print('\n')



''''  ----    ПРобую другую страницу    ----'''

''''
Нужно извлечь -Название элемента  -Его цену

'''
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

# Моя попытка. Не могу выдернуть цену???
# response =requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# name_elements = soup.find_all('h4', class_= 'card-title')
# for nameElement in name_elements:
#     print(nameElement.text)
#
# price_elements = soup.find_all('div', class_ = 'card-body')
# price_elements_2 = price_elements.find_all('h5')
# for priceElement in price_elements_2:
#     print(priceElement.text)

#
# response =requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

# for n,i in enumerate(items, start=1):
#     itemName = i.find('h4', class_='card-title').text.strip()
#     itemPrice = i.find('h5').text
#     print(f'{n}: {itemPrice} за {itemName}')


''''
Попробую переписать без функции enumerate
Работать код будет
'''
# for i in items:
#     itemName = i.find('h4', class_='card-title').text.strip()
#     itemPrice = i.find('h5').text
#     print(f'{itemPrice} за {itemName}')




''''
Скрапинг с учетом пагинации (спарсит все страницы)
'''
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

for n, i in enumerate(items, start=1):
    itemName = i.find('h4', class_='card-title').text.strip()
    itemPrice = i.find('h5').text
    print(f'{n}:  {itemPrice} за {itemName}')

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        hrefval = link.get('href')
        urls.append(hrefval)

for slug in urls:
    newUrl = url.replace('?page=1', slug)
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for n, i in enumerate(items, start=n):
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}:  {itemPrice} за {itemName}')







''''
Вопросы:
-i.find('h4', class_='card-title').text.strip(). Что такое i.find, 
-не могу интерпритировать text.strip()
-почему иногда выводится тарабарщина <h1>РЎСЂР°РЅРёС†Р° РїРѕР»СЊР·РѕРІР°С‚РµР»СЏ Mr. Anderson</h1>
-почему у меня не работает модуль регулярных выражений re с методом compile
   find_a_by_text_re_compile = soup.find("a", text=re.compile("Одежда"))
   print(find_a_by_text_re_compile)
   
- Что за параметры у записи:
with open("all_categories_dict.json", "w") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)


'''


