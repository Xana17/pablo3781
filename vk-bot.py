import vk_api
import requests

#url = "https://swapi.dev/api/planets/"
url = 'https://swapi.dev/api/starships/'

response = requests.get(url) 
planets_data = response.json() 
planets = planets_data.get('results') 

#response = requests.get(url) 
starships_data = response.json() 
starships = starships_data.get('results') 
 
token = "vk1.a.BdIrrBoIXcGyzuTpisqEQuKmMRUeed0X0uUEmhePmlU6DANGn5LGqGqJ1kGzCHRLTudXgZ61yC9VDwFaCKLAQelsRYR3UjLfL--6F_Wro3zFD6f3t7dfq3CEvnTROuyxJXTjBOswXNTlVzvRIaRkdg0o5aun1_0KDOSNj27T-D8CKYsngZJzjkxw-iQNLIx95uuIJnxieSC2bomPHCCEPg"

vk_session = vk_api.VkApi(token=token)

vk = vk_session.get_api()

#messages = vk.messages.getConversations(count=20, filter='unanswered')

##print(messages)
starships_list = []
planets_list = []
while True:
    messages = vk.messages.getConversations(count=20, filter='unanswered') # выгрзука всех диалгов
    if messages['count'] >= 1:
        message_text = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['random_id']
        if message_text.lower() == 'привет':
            vk.messages.send(user_id=user_id, random_id=message_id, message='Привет!!! Как твои дела?')
        # if message_text.lower() == "планеты":
        #     for i in range(0,8):
        #         diameter = planets[i].get('diameter') 
        #         name = planets[i].get('name')
        #         planets_list.append(diameter)
        #         planets_list.sort(reverse=True)
        #     max_diameter = planets_list[0]
        #     max_diameters = max(planets_list)
            #vk.messages.send(user_id=user_id, random_id=message_id, message= (f"{name}'s diameter is {diameter}"))
            #vk.messages.send(user_id=user_id, random_id=message_id, message= ( max_diameter))
        if message_text.lower() == "корабли":
            for i in range(0,12): 
                maximum_speed = starships[i].get('max_atmosphering_speed') 
                name = starships[i].get('name')
                starships_list.append(maximum_speed)
                #starships_list.sort(reverse=True)
                #maxs_speed = max(starships_list)
                #maxi_speed = starships_list[0]
                #vk.messages.send(user_id=user_id, random_id=message_id, message= (f"{name}'s max speed is {max_speed}"))
                vk.messages.send(user_id=user_id, random_id=message_id, message= (starships_list))
                print(starships_list)