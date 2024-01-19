import telebot


class Button:
    def __init__(self):
        self.markup = telebot.types.InlineKeyboardMarkup()
        self.bt_drama = telebot.types.InlineKeyboardButton('Драма', callback_data='drama')
        self.bt_comedy = telebot.types.InlineKeyboardButton('Комедия', callback_data='comedy')
        self.bt_melodrama = telebot.types.InlineKeyboardButton('Мелодрама', callback_data='melodrama')
        self.bt_detective = telebot.types.InlineKeyboardButton('Детектив', callback_data='detective')
        self.bt_thriller = telebot.types.InlineKeyboardButton('Триллер', callback_data='thriller')
        self.bt_cartoon = telebot.types.InlineKeyboardButton('Мультфильм', callback_data='cartoon')
        self.bt_more = telebot.types.InlineKeyboardButton('Другой фильм', callback_data='more')

    def add_button(self, *args):
        self.markup.add(*args)
