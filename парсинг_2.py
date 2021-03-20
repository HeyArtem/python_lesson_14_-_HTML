import requests
import random
from time import sleep
from bs4 import BeautifulSoup
import json
import csv


''''
Изучаю парсинг с
https://www.youtube.com/watch?v=ks64MvZJe0w
код на github: https://github.com/pythontoday/scrap_tutorial

Шаг 1
Спарсим сайт и сохраним ссылки в фаил  "index.html"
'''

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}
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
#
# with open("index.html", encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
#
# all_products_hrefs = soup.find_all(class_= "mzr-tc-group-item-href")
# for item in all_products_hrefs:
#     print(item) # пробная распечатка полученных ссылок и названий - Божественно!!! Закоментил, т.к. дальше написал ещё божественней

# Обучение парсингу на Python #2 | Парсинг сайтов | Выполняем заказ на фрилансе Продолжить с 5:45

''''
Создадим две переменные, одна будет 
с названием категории, item_text  а другая
с сылкой на нее item_href
Текстовый элемент мы можем получить с помощью 
метода text, а ссылку с помощью
метода get в который передаем название атрибута href
'''

# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href") # https://health-diet.ru вставка, что бы извлекаемая ссылка была с доменным именем
#     print(f"{item_text}:{item_href}") # закоментил, потому что дальше я все сохраню в словарь






''''
Сделаем тоже самое, но сохраним в словарь, а словарь в json фаил

!!!!                 ВНИМАНИЕ  пример ЗАПИСИ в json фаил   !!!!!!
'''
# all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")
#
#     all_categories_dict[item_text] = item_href
#
# with open("all_categories_dict.json", "w", encoding="utf-8") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False) # закоментил, т.к. дальше буду загружать созхраненый фаил




''''
Создадим цикл, на каждой т\иетрации которого, мы будем заходить 
на новую страницу категории собирать с нее данные 
о товарах и химическом составе и записывать в фаил
-Каждую старницу будем сохранять под именем категрии
- каждую запятую, пробел и дефис будем заменять на нижний слэш'''

with open("all_categories_dict.json", encoding="utf-8") as file:
    all_categories = json.load(file)
# print('Наш словарь Имя:ссылка->', all_categories) # контрольная распечатка


''''
Переменная в которую положим количество страниц категорий'''
iteration_count = int(len(all_categories))-1

count = 0
print(f"Всего итераций: {iteration_count}")
for category_name, category_href in all_categories.items():
    # ВНИМНИЕ код реплейса - код замены СИМВОЛОВ!!!

    rep = [",", " ", "-", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")
    # print(category_name)

# Переходми к запросам на странице
# я раскоментю загоовки стр.16, что бы использовать их в запросе


    reg = requests.get(url=category_href, headers=headers)
    src = reg.text

    with open(f"data/{count}_{category_name}.html", "w", encoding="utf-8") as file:
        '''сохраним нашу страницу под именем категории, будем сохранять ее
            в папке data и добавим счетчик (перемен.count)
        '''
        file.write(src) # вуаля папка с первой стр. готова


    with open(f"data/{count}_{category_name}.html", encoding="utf-8") as file:
        '''' ОТкроем и сохраним код страницы в переменную '''
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    ''''
    ПРоверка страницы, на наличие таблицы  с продуктами.
    
    Перед тем, как запустить код, котор пройдет по всем ссылкам, нужно внести коректировку
    т.к. страница DANONE пуста и не несет ссылки и код завершиться с ошибкой
    Скопируем класс alert  и напишем условие
    '''
    alert_block = soup.find(class_="uk-alert-danger") # если данный класс присутствует на странице, то переходим к следующей итерации
    if alert_block is not None:
        continue




    '''' Первым делом найдем заголовки для наших данных в таблице '''
    # соберем все заголовки таблицы
    table_head = soup.find(class_ = "mzr-tc-group-table").find("tr").find_all("th")
    # print(table_head) # распечатаем полученный СПИСОК
    # print(table_head[0]) # можно обращаться по индексу

    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text
    # print(carbohydrates, calories)

    with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file) # writer-наш писатель,  у модуля csv вызываем метод writer, предав ему наш фаил
        '''' 
        Дальше укажем нашему писателю, что записывать в фаил. метод writerow- запифет фаил в cтроку
        Метод принимает один аргумент, но нам нужно записать 5, поэтому мы можем обьединить наши аргументы в кортеж или список
        
        !!! ПОЧЕМУ в csv у меня кодировка не славянская и не по столбцам записано ??????
        '''
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    # собираем данные продуктов
    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

    ''''
    Будем так же создавать третий фаил, который будет в формате json. 
    В него мы будем собирать все данные из категорий в виде словаря
    Т.е. будет один в фаил в csv, а второй в json
    Создадим product_info и после получения данных 
    будем каждую итерацию пополнять его новым объектом
    '''
    product_info = []
    for item in products_data: # в цикле соберем все td теги в tr
        product_tds = item.find_all("td")

        title = product_tds[0].find("a").text # выводим названия
        # print(title) # контр.распеч. названия


        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text
        # print(proteins) # контр. распеч., например белки

        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )

        with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(
                file)  # writer-наш писатель,  у модуля csv вызываем метод writer, предав ему наш фаил

            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )
    with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)



    count += 1
    '''' После каждой итерации будем выводить print, что бы не скучать'''
    print(f"# Итерация {count}. {category_name} записан...")
    iteration_count = iteration_count -1

    ''''
    На последней итерации будет выводиться принт - осталось итераций ноль
    что бы такого не было напишем условие:'''
    if iteration_count == 0:
        print("Работа завершена")
        break

    print(f"осталось итераций: {iteration_count}")
    sleep(random.randrange(1, 2)) # небольшая зандомная пауза между итерациями


