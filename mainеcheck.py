

# *** Переменные и типы данных ***

#  a = 10
#  b = 'Hello world!'
#  c = True


# *** Ввод и вывод + "Чепуха" ***

# likes_number = input('Введите число: ')
#
# print(likes_number)

# object = input('Кто?')
# action = input('Что сделал?')
# place = input('Где это произошло?')
#
# # Сложение строк
# s = object + action + place
# print(s)

# print(object, action, place)

# print('Вы ввели число: ')
# print(a)


# *** Простой калькулятор и операции ***


# Строки
# a = '1'
# b = '2'

# Целочисленный тип данных
# d = 1
# e = 2

# a = int(input('Введите число А: '))
# b = int(input('Введите число B: '))
#
# print('Сумма чисел:', a + b)
# print('Разность чисел:', a - b)
# print('Произведение чисел:', a * b)
# print('Деление чисел:', a / b)
# print('Остаток деления чисел:', a % b)
# print('Целая часть деления чисел:', a // b)
# print('Возведение в степень: ', a ** b)




# *** Списки ***
# https://tproger.ru/articles/spiski-v-python-osnovy-i-metody/



# some_films = ['Кот в сапогах', 'Человек паук', 'Дюна', 'Т-34']

# print(some_list[-1]) # Обращение к последнему эл-ту в списке
# print(some_films[2])

#some_list = [5, 3, 1, -2, 3, -50, 8, 586]

#a = [1, 'Hello!', True, [5, 85, 1]]

#print(a[3][2])

#favorite_films = []
# # print(favorite_films)
# # favorite_films.append(5)
# # favorite_films.append('hello!')
# # print(favorite_films)
#film_1 = input('Введите фильм: ')
#film_2 = input('Введите фильм: ')
#film_3 = input('Введите фильм: ')
#favorite_films.append(film_1)
#favorite_films.append(film_2)
#favorite_films.append(film_3)
#print(favorite_films[1])

#score = [5, 3, 2, 1, 5, 5]
#avg = sum(score) / len(score)
#print(min(score))
#print(len(score))

# Циклы

# for переменная-счётчик in range(начало, конец, шаг)
# for переменная-элемент in список

# score = ['Шрек', "Бойцовский клуб", "Пятый элемент"]
# for i in score:
#     print(i)


#for i in range(100, 10, -2):
#     print()
#     print(i)

# favorite_films = []
#
# for i in range(3):
#     film = input('Введите фильм: ')
#     favorite_films.append(film)
#
# for film in favorite_films:
#     print('Я люблю ' + film )

# film_1 = input('Введите фильм: ')
# film_2 = input('Введите фильм: ')
# film_3 = input('Введите фильм: ')
# favorite_films.append(film_1)
# favorite_films.append(film_2)
# favorite_films.append(film_3)
#
# for i in range(1, 5):
#
#     print(i)
#
#for i in range(3):
#     print(i)

#i = 1
#while i != 10:
#     print(i)
#     i += 1 # i = i + 1

# Библотеки

#import random

#facts = ['Слава - рыба', "Георгий - ленивый", "2+2 = 4", "майнкрафт - топ"]

#print(random.choice(facts))

#for i in range(random.randint(5, 50)):
#   print(random.randint(1, 1024))


# a = []
# for i in range(7):
#     temp = int(input('Введите температуру сегодня: '))
#     a.append(temp)
# print('Средняя температура равна', sum(a)/len(a))


# = - присвоение
# == - сравнение


# favorite_actor = 'Райан Гослинг'
# rating = int(input('Какой рейтинг у фильма?'))
#
# actor = input('Кто играет главную роль в этом фильме?')
#
# if actor == favorite_actor and rating > 7:
#     print('Этот фильм точно стоит смотреть!')
# elif actor == favorite_actor or rating > 7:
#     print('Должен быть неплохим!')
# else:
#     print('Я бы не стал тратить время')

#a = 5
#b = 19
#
#if a == 5 and b == 1:
#    print('ok!')
#else:
#    print('no!')

#num = int(input('Введите число: '))
#if num % 2 == 0:
#     print('Число чётное')
#else:
#     print('Число нечётное')

# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# else:
#     print(b)

# import random
#
# computer_number = random.randint(1, 10)
# flag = False
#
# while flag == False:
#     user_number = int(input('Угадай, какое число я загадал! '))
#     if computer_number == user_number:
#         print('Поздравляю! Вы угадали число!')
#         flag = True
#     elif computer_number-user_number == 1 or computer_number-user_number == -1:
#         print('Почти угадал!')
#     else:
#         print('Ничего, в следующий раз повезёт')

#import random

#computer_number = random.randint(1, 10)

#while True:
#    user_number = int(input('Угадай, какое число я загадал! '))
#    if computer_number == user_number:
#        print('Поздравляю! Вы угадали число!')
#       break
    # elif computer_number-user_number == 1 or computer_number-user_number == -1:
        # print('Почти угадал!')
    # else:
        # print('Ничего, в следующий раз повезёт')

# Словари
# ключ: значение

# english_dict = {
#     'яблоко': 'apple',
#     'молоко': 'milk',
#     'кот': 'cat'
# }
#
# word = input('Введите слово на русском языке: ')
# if word in english_dict:
#     print(word, 'на английском языке будет:', english_dict[word])
# else:
#     print('Я не знаю такого слова')


#
#
# films_dict = {
#     # 'название фильма': 'главный актёр'
#     'Начало': 'Леонардо Ди Каприо',
#     'На грани': 'Эд Харрис',
#     'Драйв': 'Райан Гослинг',
#     'Пираты Карибского моря': "Джонни Депп"
# }
#
# print(films_dict['Начало'])
#
# favorite_actor = 'Джонни Депп'
#
# film = input('Какой фильм Вы хотите посмотреть? ')
#
# if film in films_dict:
#     if favorite_actor == films_dict[film]:
#         print('Фильм бомба!!!!!!!!')
#     else:
#         print('Фильм отстой!!!!!!!')
# else:
#     print('Я такого фильма не знаю')


# w - write
# r - read
# a - add

# file = open('test.txt', 'w')
# file.write('fsdfsdfsdfsdfsdf')
# file.close()

# fileR = open('test.txt', 'r')
# s = fileR.read()
# print(s)
# fileR.close()

# name = input('Введите своё имя: ')
# fileA = open('test.txt', 'a')
# fileA.write(name + ' hello!' + '\n')
# fileA.close()

# ctrl + / - комментарий


# def summ(a, b): # def - ключевое слово, что это ф-я, summ - название функции, a,b - аргументы
#     s = a + b
#     return s # Возвращаемое значение
#
#
#
# print(summ(5, 1))
# print(summ(1, 4))
# print(summ(2, 8))





# def calc(num1, num2, op):
#     result = 0
#     if op == '+':
#         result = num1 + num2
#     elif op == '-':
#         result = num1 - num2
#     return result

# num1 = int(input('Введите число 1 '))
# num2 = int(input('Введите число 2 '))
# op = input('Введите операцию: ')

# s = calc(num1, num2, op)
# print(s)

# from tkinter import *
# # import tkinter

# window = Tk()

# window.geometry('800x600')

# canvas = Canvas(window, width=800, height=600, bg='white') #Холст создали

# canvas.pack() #Поставили холст на мальберт

# # canvas.create_rectangle(100,100,350,350,fill='black', outline='')

# # canvas.create_rectangle(120, 120, 140, 140,fill='red', outline='')
# # canvas.create_rectangle(150, 150, 190, 190,fill='blue', outline='')
# # canvas.create_rectangle(200, 200, 260, 260,fill='green', outline='')
# #
# # canvas.create_polygon(10, 50, 50, 10, 90, 50, fill='yellow', outline='')

# # canvas.create_polygon(10, 260, 60, 200, 110, 260, fill='green', outline='black')
# # canvas.create_rectangle(20, 260, 100, 360, fill='red', outline='black')
# #
# #
# #
# #
# # window.mainloop()


# class User:
#     def __init__(self, name, phone, img):
#         self.name = name
#         self.phone = phone
#         self.img = img

#     def print_hello(self):
#         print('Привет! Меня зовут', self.name)


# user1 = User('Masha', '999', './img/123.jpg')
# user2 = User('Lena', '888', './img/222.jpg')
# user3 = User('Vanya', '779', './img/1113.jpg')

# user1.print_hello()
# user3.print_hello()

# import random

# # facts = ['Слава - рыба', "Георгий - ленивый", "2+2 = 4", "майнкрафт - топ"]

# # print(random.choice(facts))

# # for i in range(random.randint(5, 50)):
# #     print(random.randint(1, 1024))
# # Списки

# # favorite_films = []
# # # print(favorite_films)
# # # favorite_films.append(5)
# # # favorite_films.append('hello!')
# # # print(favorite_films)
# # film_1 = input('Введите фильм: ')
# # film_2 = input('Введите фильм: ')
# # film_3 = input('Введите фильм: ')
# # favorite_films.append(film_1)
# # favorite_films.append(film_2)
# # favorite_films.append(film_3)
# # print(favorite_films[1])

# # score = [5, 3, 2, 1, 5, 5]
# # avg = sum(score) / len(score)
# # print(min(score))

# # Библотеки


# # Циклы

# # for переменная-счётчик in range(начало, конец, шаг)
# # for переменная-элемент in список

# # score = ['Шрек', "Бойцовский клуб", "Пятый элемент"]
# # for i in score:
# #     print(i)


# # for i in range(100, 10, -2):
# #     print()
# #     print(i)

# # favorite_films = []
# #
# # for i in range(3):
# #     film = input('Введите фильм: ')
# #     favorite_films.append(film)
# #
# # for film in favorite_films:
# #     print('Я люблю ' + film )

# # film_1 = input('Введите фильм: ')
# # film_2 = input('Введите фильм: ')
# # film_3 = input('Введите фильм: ')
# # favorite_films.append(film_1)
# # favorite_films.append(film_2)
# # favorite_films.append(film_3)
# #
# # for i in range(1, 5):
# #
# #     print(i)
# #
# # for i in range(3):
# #     print(i)

# # i = 1
# # while i != 10:
# #     print(i)
# #     i += 1 # i = i + 1


# # def calc(a,b, operand):
# #     if operand == '+':
# #         res = a + b
# #     elif operand == '-':
# #         res = a - b
# #     elif operand == '*':
# #         res = a * b
# #     elif operand == '/':
# #         res = a / b 
# #     else:
# #         res = 'Извините, но такой операции нет в калькуляторе.'
# #     return res

# # num1 = int(input('Введите число:'))
# # num2 = int(input('Введите число:'))
# # opel = input('введите операцию:')
# # toga= calc(num1, num2, opel)
# # print(toga)

# # file = open('calculations.txt', 'a')
# # file.write(f'{toga}' + '\n')

# violator_songs = { 
#     'World in My Eyes': 4.86, 
#     'Sweetest Perfection': 4.43, 
#     'Personal Jesus': 4.56, 
#     'Halo': 4.9, 
#     'Waiting for the Night': 6.07, 
#     'Enjoy the Silence': 4.20, 
#     'Policy of Truth': 4.76, 
#     'Blue Dress':4.29, 
#     'Clean': 5.83 
# } 
 
# summ = 0
# n = int(input("Сколько песен выбрать? ")) 
# for i in range(n): 
#     name = input("Название "+str(i+1)+" песни: ") 
#     time = violator_songs[name] 
#     summ = summ + time 
# print("Общее время звучания песен:",summ," минут")



# my_iter = [x for x in range(1, 100_000_000)] # Строгие вычисления
#
# print(my_iter)

# my_iter = (x for x in range(1, 100_000_000))
#
# for elem in my_iter:
#     print(elem)


# my_iter = []
# for x in range(1,100_000):
#     my_iter.append(x)

# def f(a):
#     print('start')
#     return a
#     print('end')

# a = []
# for i in range(10):
#     a.append(i)
#
# print(a)

# def my_lazy_gen():
#     for x in range(10):
#         print('до', x)
#         yield x
#         print('после', x)
#
# for i in my_lazy_gen():
#     print(i)




# file = open('file.txt', 'w')
# file.write('Hello!!?????!')

# lst = []
# for i in range(10000):
#     lst.append(open('file.txt', 'w'))

# lst = []
# for i in range(10000):
#     f = open('file.txt', 'w')
#     f.write([12, 15])
#     lst.append(f)
#     f.close()


# with open('file.txt', 'w') as f:
#     f.write('111')
#     print(f.closed)
# print(f.closed)



# import time
# class Timer:
#     def __init__(self):
#         self.timer_start = None
#     def __enter__(self):
#         print("Марш")
#         self.timer_start = time.time()
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         print("Финиш")
#         timer_stop = time.time()
#         print(f"{timer_stop - self.timer_start}")

#     with Timer() as t:
#         my_list = [i ** 2 for i in range(1_000_000)]
#         print(my_list[-1])


# class Range:
#     def __init__(self,start,limit):
#         self.start = start
#         self.limit = limit
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.limit == 0:
#             print("Ого")
#         else:
#             self.limit -= -1
#             return self.limit

# my_range = Range(start=0,limit=10)
# my_iter = iter(my_range)
# for i in my_range:
#     print(i)

# class Range:
#     def __init__(self,start,limit):
#         self.start = start
#         self.limit = limit
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.limit == 0:
#             raise StopIteration
#         else:
#             self.limit -= -1
#             self.start += 1
#             return self.limit

# my_range = Range(start=0,limit=10)
# my_iter = iter(my_range)
# for i in my_range:
#     print(i)

# class Year:
#     def __init__(self, days):
#         self.days = days
    
#     @property
#     def days(self):
#         return self.__days
    
#     @days.setter
#     def days(self,days):
#         if days > 364:
#             self.__days = days
#         else:
#             #raise Exception("К сожалению,столько дней в году не бывает")
#             print("pablo")

# year = Year(364)

# year.days = 365
# print(year.days)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             raise Exception('Вы ещё не родились')

# person = Person('Иван', 25)

# person.age = -50

# print(person.age)


# from tkinter import *
# import random

# window = Tk()
# window.geometry('600x600')

# class Fire:
#     image = PhotoImage(file='elements/free-icon-fire-9509865.png').subsample(4, 4)
#     def __add__(self, other):
#         if isinstance(other, Ground):
#             return Clay

# class Water:
#     image = PhotoImage(file='elements/free-icon-water-drop-4246703.png').subsample(4, 4)

# class Ground:
#     image = PhotoImage(file='elements/ground.png').subsample(4, 4)
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Clay

# class Wind:
#     image = PhotoImage(file='elements/wind.png').subsample(4, 4)

# class Clay:
#     image = PhotoImage(file='elements/free-icon-pottery-7942410.png').subsample(4, 4)



# canvas = Canvas(window, width=600, height=600)
# canvas.pack()

# elements = [Fire(), Ground(), Water(), Wind()]

# for elem in elements:
#     img = canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)

# def move(event):
#     images_id = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)
#     canvas.coords(images_id, event.x, event.y)
#     if len(images_id) == 2:
#         element1 = elements[images_id[0]-1]
#         element2 = elements[images_id[1]-1]
#         new_element = element1+element2
#         if new_element not in elements:
#             canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=new_element.image)
#             elements.append(new_element)

# window.bind('<B1-Motion>', move)

# window.mainloop()


# class Item:
#     def __init__(self, name, brand, price):
# 
# 
# item1 = 
# item2 = 
# item3 = 
# goods = [item1, item2, item3]

# goods = [
#     {
#         'name': 'Iphone 14',
#         'brand': 'Apple',
#         'price': 1400
#     },
#     {
#         'name': 'Iphone 11',
#         'brand': 'Apple',
#         'price': 600
#     },
#     {
#         'name': 'Samsung Galaxy A23',
#         'brand': 'Samsung',
#         'price': 700
#     },
#     {
#         'name': 'Xiaomi mi8 lite',
#         'brand': 'Xiaomi',
#         'price': 300
#     }
# ]

# def item_price(item):
#     return item['name']

# print(sorted(goods, key=lambda item: item['price']))

# apple_list = filter(lambda item: item['brand']=='Apple' , goods)
# print(list(apple_list))

# a = ['1', '2']
# numbers = ['1', '2', '3']
# number_map = map(lambda a: a+'s', numbers, a)
# print((number_map))

# for item in goods:
#     print(item)

# for index, item in enumerate(goods):
#     print(index, item)

# names = ["Иван", "Вася", "Петр", "Олег"]
# surnames = ['Петров', "Иванов", "Васильич"]
# a = ['Кружочек', "Квадратик", "Треугольник"]

# for name, surname, figure in zip(names, surnames, a):
#     print(name, surname, figure)

# import sqlite3

# class User:
#     def __init__(self,name,surname,gender):
#         self.name = name
#         self.surname = surname 
#         self.gender = gender

# def create_table_users(data_base):
#     command = """
#         CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         surname TEXT,
#         gender TEXT
#         );
#     """
#     data_base.execute(command)

# def add_user(data_base,user):
#     command = """
#         INSERT INTO users (name,surname,gender)
#         VALUES (?,?,?)
#     """
#     data_base.execute(command, (user.name,user.surname,user.gender))

# def get_users_list(data_base,):
#     command = """
#         SELECT gender FROM Users
#         if gender = "Мужчина
#     """
#     results = data_base.execute(command,)
#     print(list(results))

# def delete_users(data_base,user_id):
#     command = """
#         DELETE FROM users
#         Where id = ?
#     """
#     data_base.execute(command,(user_id))

# def update_users(data_base,name,user_id):
#     command = """
#         UPDATE users
#         SET name = ?
#         Where id = ?
#     """
#     data_base.execute(command,(name,user_id))

# with sqlite3.connect("data.db") as data_base:
#     create_table_users(data_base)
#     add_user(data_base,User("Иван","Иванов","Мужчина"))
#     get_users_list(data_base,"Мужчина")
#     # delete_users(data_base,1)
#     # update_users(data_base,"Димон",2)

# import os

# current_path = os.path.abspath(__file__)
# parent_path = os.path.join(current_path,"..")

# def get_all_files(path):
#     for name in os.listdir(path):
#         new_path = os.path.join(path,name)
#         if os.path.isdir(new_path):
#             print("Папка",name)
#             get_all_files(new_path)
#         else:
#             print("-",name)

# get_all_files(parent_path)


# def recurs(count):
#     print(count)
#     if count == 100:
#         return
#     recurs(count + 1)
# recurs(0)

# def strcounter(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym,counter)

# s = "afvcbcaalv"
# strcounter(s)

def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0) + 1
    print(syms_counter)

strcounter("afcc")