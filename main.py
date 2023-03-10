import telebot
import random
from env import TOKEN


bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1,button2)

@bot.message_handler(commands=['start','hi'])
def start_function(message):
    msg = bot.send_message(message.chat.id ,f'привет {message.chat.first_name},начнем игру?',reply_markup=keyboard)
    bot.register_next_step_handler(msg , answer_check)
    # bot.send_sticker(message.chat.id,'CAACAgQAAxkBAAJJ62OhPUdMdg9xAAG0fETiq5E52VE3qgAC-REAAhUm0FAjCj4_qMDONywE')
    # bot.send_photo(message.chat.id,'https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_960_720.jpg')
# @bot.message_handler()
# def echo_all(message):
#     bot.send_message(message.chat.id, message.text)


def answer_check(msg):
    if msg.text=='Да':
        bot.send_message(msg.chat.id,'у тебя есть 3 попытки угадать число от 1 до 10 ')
        random_number=random.randint(1,10)
        p=3
        start_game(msg,random_number,p)
    else:
        bot.send_message(msg.chat.id,'Тогда пока')

def start_game(msg, random_number,p):
    msg = bot.send_message(msg.chat.id,'Введи число от 1 до 10: ')
    bot.register_next_step_handler(msg,check_func,random_number,p-1)

def check_func(msg, random_number, p):
    if msg.text == str(random_number):
        bot.send_message(msg.chat.id,'ты угадал')
    elif p==0:
        bot.send_message(msg.chat.id, f'у тебя не осталось попыток!Числом было :{random_number} ')
    else:
        bot.send_message(msg.chat.id,f'нет,у тебя осталось {p} попыток')
        start_game(msg,random_number,p)
        

    
bot.polling()


