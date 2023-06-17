import vk_api #vk-api
from vk_api.longpoll import VkLongPoll

token = 'vk1.a._YsLFsJ7MI4HbAFd_-lz0NqeX0fxfx58EUrpnKTh7HwgMAAqzHOaBgU6LacKih47KTid4_UE2RVUtJ8QBEkoS6zK0RvbZIOqTEQFVXopUL4A9Cmf1QsOAVd5B19I6HFKl6teAZdbmGchK7xfZ91zAfVYo2aqMQH5iq2ALXKCMfj7XR6cAI9L0PRg2pJX_vqHkvv7psIS_Rnox7ugwts9wg'

vk_session = vk_api.VkApi(token=token) # Авторизация как владельца сообщества

vk = vk_session.get_api() # Получение API VK

longpoll = VkLongPoll(vk_session) # Создали длинный запрос

for event in longpoll.listen():
    if event.type == 4 and event.to_me:
        text = event.text
        user_id = event.user_id
        message_id = event.message_id
        if text.lower() == 'привет':
            vk.messages.send(user_id=user_id, random_id=message_id, message='Привет дорогой!!!')
        else:
            vk.messages.send(user_id=user_id, random_id=message_id, message='Я тебя не понимаю!')
