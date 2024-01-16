import telebot

import random

import sqlite3

from api_token import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


def select(genre):
    with sqlite3.connect('Films.db') as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM film WHERE genre = '{genre}'")
        arr_genre = cursor.fetchall()
        id_random = random.randint(0, len(arr_genre) - 1)
        film_drama = arr_genre[id_random]
    return film_drama


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    markup = telebot.types.InlineKeyboardMarkup()
    bt_start = telebot.types.InlineKeyboardButton('Начать', callback_data='ready')
    markup.add(bt_start)

    bot.send_message(message.chat.id,
                     'Добро пожаловать в мой кинотеатр 📺\n\nЯ помогу тебе выбрать фильм для вечернего просмотра. Фильмы входят в топ 50 🔝\nЭти фильмы молодости (не только) наших родителей, но очень интересные 🎥\n\nЗапасайся попкорном 🍿',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ready')
def callback(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    bt_drama = telebot.types.InlineKeyboardButton('Драма', callback_data='drama')
    bt_comedy = telebot.types.InlineKeyboardButton('Комедия', callback_data='comedy')
    bt_melodrama = telebot.types.InlineKeyboardButton('Мелодрама', callback_data='melodrama')
    markup.add(bt_drama, bt_comedy, bt_melodrama)
    bt_detective = telebot.types.InlineKeyboardButton('Детектив', callback_data='detective')
    bt_thriller = telebot.types.InlineKeyboardButton('Триллер', callback_data='thriller')
    bt_cartoon = telebot.types.InlineKeyboardButton('Мультфильм', callback_data='cartoon')
    markup.add(bt_detective, bt_thriller, bt_cartoon)

    bot.send_message(call.message.chat.id, 'Супер! Выбери жанр 🎬', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'drama')
def call_drama(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    bt_more = telebot.types.InlineKeyboardButton('Другой фильм', callback_data='more')
    markup.add(bt_more)

    film_drama = select('драма')
    bot.send_message(call.message.chat.id,
                     f'<b>Название:</b> {film_drama[1]}\n\n<b>Жанр:</b> {film_drama[2]}\n\n<b>Описание:</b> {film_drama[3]}\n\n<b>Ссылка:</b> {film_drama[4]}',
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'comedy')
def call_drama(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    bt_more = telebot.types.InlineKeyboardButton('Другой фильм', callback_data='more')
    markup.add(bt_more)

    film_drama = select('комедия')
    bot.send_message(call.message.chat.id,
                     f'<b>Название:</b> {film_drama[1]}\n\n<b>Жанр:</b> {film_drama[2]}\n\n<b>Описание:</b> {film_drama[3]}\n\n<b>Ссылка:</b> {film_drama[4]}',
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'melodrama')
def call_drama(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    bt_more = telebot.types.InlineKeyboardButton('Другой фильм', callback_data='more')
    markup.add(bt_more)

    film_drama = select('мелодрама')
    bot.send_message(call.message.chat.id,
                     f'<b>Название:</b> {film_drama[1]}\n\n<b>Жанр:</b> {film_drama[2]}\n\n<b>Описание:</b> {film_drama[3]}\n\n<b>Ссылка:</b> {film_drama[4]}',
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'detective')
def call_drama(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    bt_more = telebot.types.InlineKeyboardButton('Другой фильм', callback_data='more')
    markup.add(bt_more)

    film_drama = select('детектив')
    bot.send_message(call.message.chat.id,
                     f'<b>Название:</b> {film_drama[1]}\n\n<b>Жанр:</b> {film_drama[2]}\n\n<b>Описание:</b> {film_drama[3]}\n\n<b>Ссылка:</b> {film_drama[4]}',
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'thriller')
def call_drama(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    bt_more = telebot.types.InlineKeyboardButton('Другой фильм', callback_data='more')
    markup.add(bt_more)

    film_drama = select('триллер')
    bot.send_message(call.message.chat.id,
                     f'<b>Название:</b> {film_drama[1]}\n\n<b>Жанр:</b> {film_drama[2]}\n\n<b>Описание:</b> {film_drama[3]}\n\n<b>Ссылка:</b> {film_drama[4]}',
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'cartoon')
def call_drama(call: telebot.types.CallbackQuery):
    markup = telebot.types.InlineKeyboardMarkup()
    bt_more = telebot.types.InlineKeyboardButton('Другой фильм', callback_data='more')
    markup.add(bt_more)

    film_drama = select('мультфильмы')
    bot.send_message(call.message.chat.id,
                     f'<b>Название:</b> {film_drama[1]}\n\n<b>Жанр:</b> {film_drama[2]}\n\n<b>Описание:</b> {film_drama[3]}\n\n<b>Ссылка:</b> {film_drama[4]}',
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'more')
def call_more(call: telebot.types.CallbackQuery):
    callback(call)


@bot.message_handler(content_types=['text'])
def text(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Неверная команда ❌')


if __name__ == '__main__':
    bot.infinity_polling()
