# #Задание 1
# a = int(input("Напишите число А:"))
# b = int(input("Напишите число В:"))
# c = int(input("Напишите число С:"))
# d = int(input("Напишите число D:"))
# print("Сумма чисел:",a+b+c+d)
# print("Разность чисел:",b-d)
# print("Деление чисел:",a / b)
# print("Произведение чисел:",a * b * c * d)
# print("Остаток деление чисел:",a % c)
# print("Целая часть деления чисел:",d // b)
# print("Возведение в степень:",b ** c)

# #Задание 2
# int(input("Введите значение числа A:"))
# int(input("Введите значение числа B:"))
# int(input("Введите значение числа C:"))
# print("Дискриминант:",b * b - 4 * a * c)


# def calc(a, b, op):
#     if op == '+':
#         result = a + b
#     elif op == '-':
#         result = a - b
#     elif op == "*":
#         result = a * b
#     elif op == "/":
#         result = a / b
#     else:
#         print("Ой,такой операции здесь нету")
#     return result

# num1 = int(input('Введите число 1 '))
# num2 = int(input('Введите число 2 '))
# operand = input('Введите операцию: ')
# s = calc(num1, num2, operand)
# print(s)
# fileR = open("result.txt","a")
# fileR.write(f"{s}"+ "\n")
# fileR.close()



# violator_songs = {  
#     "World in My Eyes" : 4.86,
#     "Sweetest Perfection" : 4.43,
#     "Personal Jesus" : 4.56,
#     "Halo" : 4.9,
#     "Waiting for the Night" : 6.07,
#     "Enjoy the Silence" : 4.20,
#     "Policy of Truth" : 4.76,
#     "Blue Dress" : 4.29,
#     "Clean" : 5.83
# }
# summ = 0 #
# n_s = int(input("Сколько песен выбрать?:"))
# for i in range(n_s):
#     s = input("Введите название"+str(i+1)+ "песни:")
#     time = violator_songs[s]
#     summ = summ + time
# if s in violator_songs:
#     print("Общее время звучания песен:",summ," минут")
#      #print("Общая сумма звучания песен:",sum(violator_songs[s]))
# else:
#     print("Что-то пошло не так!")



# variable_attack = {
#     "A blow from the fly" : 70 ,
#     "Throw forward" : 45 ,
#     "Fist bump" : 60
# }

# class User:
#     def __init__(self, health, attack, damage):
#         self.health = health
#         self.attack = attack
#         self.damage = damage

#     def print_health(self):
#         print('Мое здоровье сейчас:', self.health)
#     def print_attack(self):
#         print("Сейчас я использовал атаку", self.attack)  
#     def print_damage(self):
#         print("Я нанес", self.damage , "урона") 

# h =  input("Введите здоровье:")
# print(variable_attack)
# a = input("Введите способ атаки:")
# d = variable_attack[a]
# user = User( h, a, d)

# user.print_health()
# user.print_damage()

#

# from tkinter import *

# window = Tk()
# window.geometry('800x600')
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
# canvas.create_rectangle(250,200,500,400,fill='yellow', outline='')
# canvas.create_polygon(250,200,375,100,500,200, fill="red", outline ="green")
# canvas.create_polygon(250,200,125,300,250,400, fill="green", outline="yellow")
# canvas.create_polygon(250,400,375,500,500,400, fill="blue", outline="orange")
# canvas.create_polygon(500,200,625,300,500,400, fill="gray", outline="magenta")
# window.mainloop()

# class Object:
#     def __init__(self, figure, color, outline):
#         self.figure = figure
#         self.color = color
#         self.outline = outline

#     def print_figure(self):
#         print("Это" , self.figure )
#     def print_color(self):
#         print("У этой фигуры" , self.color , "цвет")
#     def print_outline(self):
#         print("У этой фигуры контур" , self.outline)

# object1 = Object("square","yellow","nope")
# object2 = Object("triangle","red","green")
# object3 = Object("triangle","green","yellow")
# object4 = Object("triangle","blue","orange")
# object5 = Object("triangle","gray","magenta")

# object5.print_figure()

# import requests 
 
# url = 'https://swapi.dev/api/starships/' 
 
# response = requests.get(url) 
# starships_data = response.json() 
 
# starships = starships_data.get('results') 
 
# for i in range(1,6): 
#     max_speed = starships[i].get('max_atmosphering_speed') 
#     name = starships[i].get('name') 
#     print(f"{name}'s max speed is {max_speed}")



# import requests  
  
# response = requests.get('https://swapi.dev/api/starships/').json()  
# starships = response.get('results')  
  
# max_speed = 0  
# ship_name = ''  
# for i in range(5):  
#     speed_str = starships[i].get('max_atmosphering_speed')  
#     if speed_str != "n/a":  
#         speed = int(speed_str)  
#         print(f"{starships[i].get('name')} - {speed}")  
#         if speed > max_speed:  
#             max_speed = speed  
#             ship_name = starships[i].get('name')  
  
# print(f"Starship with max speed is {ship_name}")

n = int(input("vekjv:"))
maximum = int(input("bkvjbv:"))
for i in range(n - 1):
   x = int(input("vjc,L:"))
   if x > maximum:
       maximum = x
print(maximum)
