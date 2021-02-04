import re

""""
14.1 Регулярные выражения
"""

string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

pattern = r'it'
'''' Допустим хотим найти выражение, именно в таком регистре "it" '''

#findall
print(re.findall(pattern, string)) #указываем шаблон "что ищем" и "где ищем"
print('Количество it:', len(re.findall(pattern, string)))

pattern_1 = r"was"
print('Количество was:',len(re.findall(pattern_1, string)))

pattern_2 = r"It"
print('Количество IT:', len(re.findall(pattern_2, string)))



pattern_abc = r'[abc]' # использую [ ]
print(re.findall(pattern_abc, string))

pattern_a = r'[a]' # использую [ ]
print('a:', len(re.findall(pattern_a, string)))



# --------- [   ] -----

pattern_az = r"[a-zA-Z0-9]"
'''' Задача посчитать все строчные и Заглавные буквы и числа'''
print("\na-zA-Z0-9:", (re.findall(pattern_az, string)))
print("a-zA-Z0-9:", len(re.findall(pattern_az, string)))


pattern_az_2 = r"[a-z0-9]"
'''' Задача посчитать все строчные  буквы и числа'''
print("\na-z0-9:", (re.findall(pattern_az_2, string)))
print("a-z0-9:", len(re.findall(pattern_az_2, string)))


pattern_az_3 = r"[,]"
'''' Задача посчитать все строчные  буквы и числа'''
print("\nЗапятых:", (re.findall(pattern_az_3, string)))
print("Запятых:", len(re.findall(pattern_az_3, string)))




#----------------( . )---------

pattern_w_ = r"[w].."
'''' Задача найти слово в длину не > трех символов, начинающееся с w. Точка также может заменяться пробелом'''
print("\n[w]..:", (re.findall(pattern_w_, string)))
print("[w]..:", len(re.findall(pattern_w_, string)))




#------------( Поиск специальных символов )---------

# \w - все, кроме спец.знаков, т.е. все символы
# \W - это отрицание, того, что значит с маленькой буквы. Все спец. знаки

pattern_w_ = r'\w'
print("\n\w:", (re.findall(pattern_w_, string)))
print("\w:", len(re.findall(pattern_w_, string)))


pattern_W_ = r'\W' # найдет все спец символы и пробелы
print("\n\W:", (re.findall(pattern_W_, string)))
print("\W:", len(re.findall(pattern_W_, string)))





# \d - Любая цифра [0-9]
# \D - все, кроме цифры

pattern_d_ = r'\d'
print("\n\d:", (re.findall(pattern_d_, string)))
print("\d:", len(re.findall(pattern_d_, string)))

pattern_D_ = r'\D'
print("\n\D:", (re.findall(pattern_D_, string)))
print("\D:", len(re.findall(pattern_D_, string)))






# \d{n} - найти количесво цифр, встречающееся n-раз (например номер телефона)
# \d{n, } - найти количесво цифр, встречающееся БОЛЕЕ n-раз
# \d{n,m} - найти количесво цифр, встречающееся в диапазоне от n до m раз (не менее n цифр, но не более ь количество цифр)

pattern_az2 = r'[a-zA-z]{2}' # найти все словосочетания с длиной два символа
print("\n[a-zA-z]{2} Все словосочетания длиной ДВА:", (re.findall(pattern_az2, string)))
print("[a-zA-z]{2} Все словосочетания длиной ДВА::", len(re.findall(pattern_az2, string)))

pattern_2az2 = r'\W[a-zA-z]{2}\W' # найти все словосочетания с длиной два символа
print("\n\W[a-zA-z]{2}\W Все слова длиной ДВА:", (re.findall(pattern_2az2, string)))
print("\W[a-zA-z]{2}\W Все слова длиной ДВА::", len(re.findall(pattern_2az2, string)))

pattern_2az2_2 = r'\W\w{2}\W' # тоже самое, что '\W[a-zA-z]{2}\W'-все словосочетания с длиной два символа
print("\n\W\w{2}\W Все слова длиной ДВА:", (re.findall(pattern_2az2_2, string)))
print("\W\w{2}\W Все слова длиной ДВА::", len(re.findall(pattern_2az2_2, string)))

pattern_2_4 = r'\W\w{2,4}\W' # словосочетания с длиной от двух до 4 символов. Поиск слов заданной длины!
print("\nсловосочетания с длиной от 2ух до 4 символов:", (re.findall(pattern_2_4, string)))
print("словосочетания с длиной от 2ух до 4 символов:", len(re.findall(pattern_2_4, string)))








#------------( Метод search)---------

pattern_s_2_4 = r'\W\w{2,4}\W' #возвращает первое вхождение патерна в строку и указывает его позиции
print("\nпатерн Search:", (re.search(pattern_s_2_4, string)))



#------------( Метод sub-замена)---------
pattern_sub = r'\W\w{2,4}\W' #замеим на **** (4 звездочки)
print("\nпатерн sub:", (re.sub(pattern_sub, r'****', string)))
print("патерн sub:", len(re.sub(pattern_sub, r'****', string)))


pattern_sub_s = r'\W\w{2,4}\W' # можно поменять на ничто
print("\nпатерн sub_s:", (re.sub(pattern_sub_s, r'', string)))
print("патерн sub_s:", len(re.sub(pattern_sub_s, r'', string)))
