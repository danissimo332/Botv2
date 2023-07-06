import os

from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
TOKEN=os.getenv('TOKEN')
bot=AsyncTeleBot(TOKEN)
bot=AsyncTeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['help','start'])
async def send_welcome(message):
    await bot.reply_to(message, 'Приветствую тебя новый пользователь! \nПодобрать видео на YouTube для вас: /search')
    print(message)



def generate_reply_keyboard(list_buttons, row):
    markup=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*list_buttons, row_width=row)
    return markup


@bot.message_handler(commands=['search'])#клавиатура
async def send_welcome(message):
    chat_id = message.chat.id
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Видеоигры')
    markup.add('Спорт')
    await bot.send_message(chat_id,'Выберите категорию видео: \nНачать заново:/again', reply_markup=markup)




@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    chat_id = message.from_user.id
    text_message = message.text
    text_message = text_message.lower()
    if 'спорт' in text_message:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add('Футболл')
        markup.add('Баскетболл')
        await bot.send_message(chat_id, 'Выберите вид спорта:', reply_markup=markup)
    elif '2 вариант' in text_message or 'анекдот' in text_message:
        await bot.reply_to(message, 'i')
    elif 'again' in text_message:
        await bot.reply_to(message, 'Приветствую тебя новый пользователь! \nПодобрать видео на YouTube для вас: /search')
    else:
        await bot.reply_to(message, 'я не понимаю')















import asyncio

asyncio.run(bot.polling())
