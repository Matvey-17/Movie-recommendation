import telebot

import random

import sqlite3

from api_token import API_TOKEN
from start_text import start_text
from buttons import Button
from lib_genre import genres

bot = telebot.TeleBot(API_TOKEN)


def select(genre):
    with sqlite3.connect('Films.db') as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM film WHERE genre = '{genre}'")
        arr_genre = cursor.fetchall()
        id_random = random.choice(range(0, len(arr_genre)))
        film_select = arr_genre[id_random]
    return film_select


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    markup = telebot.types.InlineKeyboardMarkup()
    bt_start = telebot.types.InlineKeyboardButton('Начать', callback_data='ready')
    markup.add(bt_start)

    bot.send_message(message.chat.id, start_text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['ready', 'more'])
def callback(call: telebot.types.CallbackQuery):
    button = Button()
    button.add_button(*button.arr_bt)

    bot.send_message(call.message.chat.id, 'Супер! Выбери жанр 🎬', reply_markup=button.markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_film(call):
    button = Button()
    button.add_button(button.bt_more)

    film = select(genres[call.data])
    bot.send_message(call.message.chat.id,
                     f'{telebot.formatting.hbold('Название:')} {film[1]}\n\n'
                     f'{telebot.formatting.hbold('Жанр:')} {film[2]}\n\n'
                     f'{telebot.formatting.hbold('Описание:')} {film[3]}\n\n'
                     f'{telebot.formatting.hlink('Ссылка', film[4])}',
                     parse_mode='HTML',
                     reply_markup=button.markup)


@bot.message_handler(content_types=['text'])
def text(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Неверная команда ❌')


if __name__ == '__main__':
    bot.infinity_polling()
