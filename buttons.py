import telebot
from lib_genre import genres


class Button:
    def __init__(self):
        self.markup = telebot.types.InlineKeyboardMarkup()
        self.arr_bt = []

        for genre, name in genres.items():
            self.arr_bt.append(telebot.types.InlineKeyboardButton(text=name, callback_data=genre))

        self.bt_more = telebot.types.InlineKeyboardButton('Другой фильм', callback_data='more')

    def add_button(self, *args):
        self.markup.add(*args, row_width=2)
