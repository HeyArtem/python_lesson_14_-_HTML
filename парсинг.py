from bs4 import BeautifulSoup

''''
Изучаю прасинг с
https://www.youtube.com/watch?v=7hn1_t2ZtJQ&list=PLqGS6O1-DZLprgEaEeKn9BWKZBvzVi_la&index=3

https://github.com/pythontoday/scrap_tutorial

Буду парсить страницу index.html
'''

with open("blank/index.html") as file:
    src = file.read()
# print(src)

# Скормим код сраницы бьютифол супу для извлечения информации
# или гооря научно должны преобразовать код в дерево объктов python

soup = BeautifulSoup(src, 'lxml')
''''
переменной soup присвоили Объект класса BeautifulSoup с параметрами переменная src и и парсером lxml
'''


# выведем тег заголовок страницы
# title = soup.title
# print(title)
#
# # выведем содержимое тега заголовок страницы
# print(title.text)
#
# # способ II
# print('способ II', title.string)

''''
Методы find() и find_all() будут решать 90% задач
Метод find находит и выводит данный из первого попавшегося указанного заголовка
'''
page_h1 = soup.find('h1')
# print('Метод find =', page_h1)


''''
А метод find_all() заберет все подходящие нашему запросу элементы и сохранит их в список
'''
# page_all_h1 = soup.find_all('h1')
# print('Метод find_all:', page_all_h1)
# ''''Который мы далее можем перебрать в цикле'''
# for item in page_all_h1:
#     print(item.text)



''''
По мимо поиска по тегу, мы можем конкретизировать наш запрос указывая атрибут тега
Получим имя пользователя, котрое лежит тег span, в нутри тега div с классом user__name
'''
user_name = soup.find('div', class_ = "user__name")
# print('\nПо атрибуту тега:', user_name)
''''
Хоть полученный результат и выглябит, как кусок кода html 
на самом деле это обьект супа и мы можем применять к нему разлтчные методы
Например применим метод text
'''
# print('\nПо атрибуту тега с text:', user_name.text)

''''
т.к. это строка, обежем пробелы методом strip'''
# print('\nобрежем пробелы:', user_name.text.strip())

''''
Шагаем в глубь по коду
После того, как мы нашли нужный нам блок кода с именем user__name
продолжаем поиск и используя метод find сообщаем, что ищем тег span и применим метод text'''
user_name_2 = soup.find('div', class_="user__name").find('span').text
# print('user_name_2:', user_name_2)


''''
Так же, мы могли бы не укзывать, что ищем нужный нам класс
в теге div и код бы все равно работал, если только данный класс один на странице
'''
user_name_3 = soup.find(class_="user__name").find('span').text
# print('user_name_3 БЕЗ div:', user_name_2)




# ''''
# Вторым способ задания атрибутов для фильтрации поиска является передача словаря
# В котором с помощью пар ключ:значение мы указываем параметры отбора
# '''
# user_name_dict = soup.find("div", {"class":"user__name"}).find("span").text
# print(' Задание атрибутов через словарь:',user_name_dict)
# ''''
# Удобство в том, что если нужны жесткие требования отбора, то мы через запятую,
# мы можем передать доп.параметры, например в виде id
# user_name_dict = soup.find("div", {"class":"user__name", "id":"aaa"}).find("span").text
# '''
#
# ''''
# Теперь попробуем собрать все span теги из class= "user__info"
# '''
# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(' Все span теги из user__info:', find_all_spans_in_user_info )
# ''''и пробежимся по нему циклом, напечатав текст внутри каждого блока span'''
# for item in find_all_spans_in_user_info:
#     print(item.text)
#
# ''''т.к. это обычный список, мы можем обращаться к его элемнетам по индексу'''
# print('по индексу [0]:', find_all_spans_in_user_info[0])
# '''' и можем применять методы'''
# print('по индексу + метод:', find_all_spans_in_user_info[2].text)
#
#
#
#
#
# ''''
# Теперь спарсим ссылки на соц.сети пользователя
# I способ
# '''
# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# print('\nссылки на соц.сети, I способ:', social_links)
#
#
# ''''
# II способ
# Но если будет еще какая то ссылка с тегом a, то получим и ее
# '''
# social_links_II = soup.find_all("a")
# print('ссылки на соц.сети, II способ:', social_links_II)
# ''''
# Что бы выдернуть ссылку и текст, создадим цикл
# Cсылка всегда хранится в атрибуте href  и мы можем ее забрать применив метод get'''
# for item in social_links_II:
#     item_url = item.get("href")
#     print(item_url)
#
# '''а теперь так же, но спрарсим текст-имя ссылки'''
# for item in social_links_II:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}:{item_url}")
#
#
#
#
# ''''
# Для перемещения по дом-дереву есть методы
# .find_parent() и .find_parents()
# они ищут родителя или родителей элемента.
# Поднимаются по структуре СНИЗУ В ВЕРХ
# т.е. как find и find_all, но снизу вверх'''
# post_div = soup.find(class_="post__text").find_parent()
# print('\nРаботаем с find_parent:\n', post_div)
# '''
# Мы забрали блок не целиком, а до первого родителя которым является <div class="user__post__info">
# '''
#
#
# ''''
# В find_parent мы также можем передовать пар-ры поиска.
# Если мы не укажем ничего, то получим первого попавшегося родителя (как было выше,)
# если укажем второго родителя, т.е. того, кто по иерархии расположен выше, получим соответственно его
# '''
# post_div_II = soup.find(class_="post__text").find_parent("div", "user__post")
# print('\n C указанием второго родителя:\n', post_div_II)


''''
А метод    .find_parents() 
поднимается по иерархии до самого body и html тег '''
# post_divs = soup.find(class_="post__text").find_parents()
# print('\nМетод  .find_parents:\n', post_divs)
''''
!!! у меня выводится какое то говно!!! абзацы повторяются и включены блоки с соц сетью и днями рождения и городами..
НЕ ПОНИМАЮ'''

# '''' Мы так же можем ставить ограничения или фильтры на поиск'''
# post_divs_II = soup.find(class_="post__text").find_parents("div", "user__post")
# print('\nfind_parents c ограничениями:\n', post_divs_II) # это уже чистенько



''''
Элементы  .next_element  и   .previous_element
'''
# next_el = soup.find(class_="post__title").next_element.next_element.text
# ''''next_element написан два раза, т.к. если один раз, то он выведет пустоту, потому что след элемент перенос строки'''
# print('\nметод  .next_el:\n',next_el)

''''
Есть похожий метод find_next, который сразу вернет следующий элемент
'''
# next_el_find = soup.find(class_="post__title").find_next().text
# print(next_el_find)

''''
Метод   .previous_element     является противоположностью next_element
и работает с низу вверх
 '''







''''
Методы    .find_next_sibling()      .find_previous_sibling()
ищут следующий и предыдущий элементы внутри искомого  тега 
Блоки post__title, post__text братья и мы можем перемещаться между ними
'''
# next_sib = soup.find(class_="post__title").find_next_sibling().text
# print('\nПробую next_sibling:\n',next_sib)

'''' Так же все методы имеют множественное число, 
которые будут искать все указанные теги
'''



''''
Применяем комбиниованные методы
# '''
# links = soup.find(class_="some__links").find_all("a")
# print('Применяем комбиниованные методы:\n', links)
#
# for link in links:
#     link_href_attr = link.get("href")
#     link_data_attr = link.get("data-attr")
#     print(link_href_attr)
#     print(link_data_attr)
#
# ''''
# !!! парсить атрибуты, мы можем и без get'''
#
# for link in links:
#     link_href_attr_notGet = link["href"]
#     link_data_attr_notGet = link["data-attr"]
#     print('БЕЗ get:', link_href_attr_notGet)
#     print('БЕЗ get:',link_data_attr_notGet)





''''
А если мы хотим искать элементы передвая в параметр текст?'''
find_a_by_text = soup.find("a", text="Одежда")
print(find_a_by_text) # ответ None

find_a_by_text_II = soup.find("a", text="Одежда для взрослых")
print(find_a_by_text_II) # Опять None, т.к. бютифул суп в одиночку не справляется с этой задачей

''''
Добввим модуль регулярных выражений   re c крутым методом compile'''

# find_a_by_text_re_compile = soup.find("a", text=re.compile("Одежда"))
# print(find_a_by_text_re_compile)
# '''' Это была ХИТРОСТЬ, но у меня она не работает... почему то?'''


''''
Попробуем собрать все элементы одежда, причем они будут написаны с прописной и ЗАглавной буквы
т.е. укажем, что бы поиск был в нескольких регистрах'''
# find_a_by_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
# print(find_a_by_clothes) # почему то у меня re не хочет работать. NameError: name 're' is not defined
