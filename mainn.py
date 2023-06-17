import pyaudio # pip install pyaudio
import speech_recognition as sr #pip install speechRecognition
import pyttsx3 #pip install pyttsx3
import random
import webbrowser
import os

rec = sr.Recognizer() # Распознаватель

# print(sr.Microphone.list_microphone_names())

voice = pyttsx3.init()
voice.say('Привет! Я голосовой помощник!')
voice.runAndWait()

list_hi = ['привет', "хай", "здравствуй", "хэллоу"]

while True:
    with sr.Microphone(device_index=1) as source:
        # rec.adjust_for_ambient_noise(source, duration=3) # Команда, если выдаёт ошибку.
        print('Скажите что-нибудь...')
        audio = rec.listen(source)
    text = rec.recognize_google(audio, language='ru_RU')

    # voice.say(text + "бууээээ")
    # voice.runAndWait()
    if 'привет' in text.lower():
        voice.say(random.choice(list_hi))
        voice.runAndWait()
    elif 'как дела' in text.lower():
        voice.say("пока не родила")
        voice.runAndWait()
    elif 'youtube' in text.lower():
        webbrowser.open_new('https://www.youtube.com/')
        voice.say("ютуб запущен")
        voice.runAndWait()
    elif 'файл' in text.lower():
        os.startfile("E:\pythonProject4")
        voice.say("файл запущен")
        voice.runAndWait()


# if 'привет' in text.lower():
#     voice.say(random.choice(list_hi))
#     voice.runAndWait()
# elif 'как дела' in text.lower():
#     voice.say("пока не родила")
#     voice.runAndWait()
#speech_recognition.exceptions.UnknownValueError

# # Простая реализация

# # name = 'Даниил'
# # salary = 200_000
# #
# # print('У ' + name + ' зарплата в месяц ' + str(salary) + ' руб')
# # print('У', name, 'зарплата в месяц', salary, 'руб')
# # print(f'У {name} зарплата в месяц {salary} руб')


# # Реализация с одним сотрудником

# # employee = {
# #     'name': 'Даниил',
# #     'salary': 200_000
# # }
# #
# # print(f'У {employee["name"]} зарплата в месяц {employee["salary"]} руб')


# # Реализация в виде словаря и списка, если сотрудников много

# employee_list = [
#     {
#         'name': 'Даниил',
#         'salary': 200_000
#     },
#     {
#         'name': 'Олег',
#         'salary': 150_000
#     },
#     {
#         'name': 'Иван',
#         'salary': 180_000
#     }
# ]

# for employee in employee_list:
#     print(f'У {employee["name"]} зарплата в месяц {employee["salary"]} руб')


# # for i in range(3):
# #     print(i)

# # my_list = ['hello!', 'Привет!', 'bonjour']
# #
# # for i in my_list:
# #     print(i)

# # print(employee_list[1])
# # print(employee_list[1]['salary'])

# employee_list = [
#     {
#         'name': 'Даниил',
#         'salary': 200_000
#     },
#     {
#         'name': 'Олег',
#         'salary': 150_000
#     },
#     {
#         'name': 'Иван',
#         'salary': 180_000
#     }
# ]

# for employee in employee_list:
#     print(f'У {employee["name"]} зарплата в месяц {employee["salary"]} руб')

# print('\n ***УВОЛЬНЕНИЕ СОТРУДНИКА***')
# name = input('Введите имя сотрудника, которого будем увольнять: ')
# for employee in employee_list:
#     if employee['name'] == name:
#         employee_list.remove(employee)
#         break

# for employee in employee_list:
#     print(f'У {employee["name"]} зарплата в месяц {employee["salary"]} руб')

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = False

#     def get_info(self):
#         print(f'У {self.name} зарплата в месяц {self.salary} руб. В отпуске? - {self.on_vacation}')

# employee_list = [Employee('Даниил', 200_000), Employee('Олег', 150_000), Employee('Никита', 180_000)]

# for employee in employee_list:
#     employee.on_vacation = True
#     employee.get_info()