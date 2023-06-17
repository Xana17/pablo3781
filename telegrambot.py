import telebot
import random

token = "5936669811:AAEB8nmEPGO3--Wc8udv2kSIF_bEFRl0_IA" # API-токен

bot = telebot.TeleBot(token) # Идентифицировали бота из ТГ



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = "Привет я флоппа"
    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(commands=['poem'])
def send_welcome(message):
    poem_text = 'pablo!'
    bot.send_message(message.chat.id, poem_text)

@bot.message_handler(commands=['cat'])
def send_cats(message):
    # cat_img = open('img/5.jpg', 'rb')
    # bot.send_photo(message.chat.id, cat_img)

    cat_number = str(random.randint(1, 9))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)


bot.polling()