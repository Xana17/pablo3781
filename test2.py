# from tkinter import *
# import time
# window = Tk()
# window.geometry('800x600')
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
# canvas.create_rectangle(100,100,350,350,fill='black', outline='')

#Добавьте новый атрибут, self.is_good_employee, который может принимать значения True или False. 
#Сделайте так, чтобы это значение можно было передать в конструктор класса в качестве параметра (как в предыдущем задании)
#Создайте список из пяти сотрудников (класс Employee), где параметр is_good_employee – у четверых будет True, а у одного False.
#После этого пройдитесь циклом по всему списку и увольте плохого работника, у которого значение self.is_good_employee = False.

# class Employee:
#     def __init__(self, name, salary,on_vacation,is_good_employee):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = on_vacation 
#         self.is_good_employee = is_good_employee
#     def get_info(self):
#         print(f" {self.name} получает в месяц {self.salary} руб. В отпуске? - {self.on_vacation}. Он хороший сотрудник? - {self.is_good_employee}")
 
#     def check_employee(self):
#         if self.is_good_employee == False:
#             print("Ты уволен")
#             employee_list.remove(employee)
#         else:
#             print("ты хороший сотрудник!")




# employee_list = [Employee('Даниил', 200_000,False,True), Employee('Олег', 150_000,True,True), Employee('Никита', 180_000,True,True), Employee("Виктор",175_000,False,True), Employee("Василий",190_000,True,False)]

# for employee in employee_list:
#     employee.get_info()
#     employee.check_employee()




# start = time.time()
# number_list = [i ** 2 for i in range(1_000_000)]
# end = time.time()
# print(f"{round(end - start , 2)}сек")
# start_1 = time.time()
# number_tuple = (i ** 2 for i in range(1_000_000))
# print(number_tuple)
# end_1 = time.time()
# print(f"{round(end_1 - start_1, 2)}сек")
# def gen_lazzy():
#     for i in range(1_000_000):
#         yield i ** 2

# number_list = [i ** 2 for i in range(1_000_000)]
# number_tuple = (i ** 2 for i in range(1_000_000))
# def gen_lazzy():
#     for i in range(1_000_000):
#         yield i ** 2
# print(number_list)
# print(number_tuple)
# print(gen_lazzy)


# import requests
# import contextlib
# from bs4 import BeautifulSoup
# from datetime import datetime

# url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
# today = datetime.today()
# today = today.strftime("%d/%m/%Y")
# payload = {"date_req" : today}
# @contextlib.contextmanager
# def get_course(id_valute):
#     try:
#         responce = requests.get(url , params=payload)
#         xml = BeautifulSoup(responce.content, "lxml")
#         valute = xml.find("valute", {"id" : id_valute})
#         valute_name = valute.find("name").text
#         valute_value = valute.find("value").text
#         valute_nominal = valute.find("nominal").text
#         yield f" ({valute_nominal} шт.) {valute_name} стоит(ят) {valute_value} рублей"
#     except Exception:
#         yield f"Не нашел"

# with get_course("R01060") as f:
#     print(f)

# class Item:
#     def __init__(self,price,brand):
#         self.price = price
#         self.brand = brand
#     def __repr__(self):
#         return self.brand
# items_list = [
#     Item(1000,"Apple"),
#     Item(1200,"Apple"),
#     Item(900,"Samsung"),
#     Item(700,"Samsung"),
#     Item(660,"Xiaomi"),


# apple_list = filter(lambda x: x.brand == 'Apple', items_list)
# print(list(apple_list))
# apple_list = filter(lambda item: item[]== "Apple", items_list)
# print(list(apple_list))


# names_list = ['данил', 'артём', 'никита', 'влад']
# names_map = map(lambda project: project+project.capitalize(),names_list)
# print(list(names_map))

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
#     def __add__(self,other):
#         if isinstance(other,Wind):
#             return Aroma
# class Ground:
#     image = PhotoImage(file='elements/ground.png').subsample(4, 4)
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Clay
#     def __add__(self,other):
#         if isinstance(other, Wind):
#             return Dust

# class Wind:
#     image = PhotoImage(file='elements/wind.png').subsample(4, 4)
#     def __add__(self,other):
#         if isinstance(other, Wind):
#             return Dust
#     def __add__(self,other):
#         if isinstance(other,Water):
#             return Aroma

# class Clay:
#     image = PhotoImage(file='elements/free-icon-pottery-7942410.png').subsample(4, 4)

# class Aroma:
#     image = PhotoImage(file="elements/aroma.png").subsample(4,4)

# class Dust:
#     image = PhotoImage(file="elements/free-icon-dust-2396941.png").subsample(4,4)




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


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     @property
#     def name(self): 
#         return self.__name

#     @property
#     def age(self):
#         return self.__age

#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name

#     @age.setter
#     def age(self, new_age):
#         if new_age <= 0:
#             raise ValueError('Вы еще не родились')
#         self.__age = new_age
    
#     @name.deleter
#     def name(self):
#         del self.__name

#     @age.deleter
#     def age(self):
#         del self.__age

# person = Person('Иван', 25)
# person.age = 50
# del person.name 
# del person.age

# class MyFile:
#     def __init__(self,name,mode,):
#         self.name = name
#         self.mode = mode
    
#     def __enter__(self):
#         file = open(name, mode)

#     def __exit__(self):
#         f.close

class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __add__(self,other):
        if isinstance(other,Item):
            return self.price + other.price
        elif isinstance(other,int):
            return self.price + other
        
    def __sub__(self, other):
        if isinstance(other,Item):
            return self.price - other.price
        elif isinstance(other,int):
            return self.price + other

    def __mul__(self,other):
        if isinstance(other,Item):
            return self.price * other.price
        elif isinstance(other,int):
            return self.price * other
        
    def __truediv__(self,other):
        if isinstance(other,Item):
            return self.price / other.price
        elif isinstance(other,int):
            return self.price / other
        
item1 = Item("Процессор", 15000)
item2 = Item("Видеокарта", 20000)
print(item1 / 8)