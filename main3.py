# pip install requests

import requests

url = "https://swapi.dev/api/" # Сайт со звёздными войнами.

response = requests.get(url).json()

#print(response['starships'])

# people_api = response['people'] # Ссылка на БД с персонажами
planets_api = response['planets'] # Ссылка на БД с планетами
starships_api = response["starships"]#response['starships']
vehicles_api = response["vehicles"]
# #Вывод информации о 5 персонажах
# #'https://swapi.dev/api/people/1'

# def check_people(url):
#     for i in range(1, 6):
#         response = requests.get(url + str(i)).json()
#         print(response['name'], response['height'])

def check_planets(url):
    for i in range(1, 6):
        response = requests.get(url + str(i)).json()
        print(response['name'], response['diameter'])

# def check_starships(url):
#     for i in range(1,6):
#         response = requests.get(starships_api +str(i)).json()
#         print(response["name"], response['max_atmosphering_speed'])

# def check_vehicles(url):
#     for i in range(1,6):
#         response = requests.get(vehicles_api +str(i)).json()
#         print(response["name"],)

# check_people(people_api)
check_planets(planets_api)
# check_starships(starships_api)
#check_vehicles(vehicles_api)
# print(people_api)
# print(people_api['results'])
# print(people_api['results'][0])
# print(people_api['results'][0]['name'])

#