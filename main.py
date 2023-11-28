import telebot
from telebot import types
from datetime import datetime
import random

bot = telebot.TeleBot('6570901773:AAHX6j0tPmjqRwXiQHaEQxMlswpe4YCGsA8')


def get_coin_side():
    return 'Орел' if random.randint(0, 1) == 0 else 'Решка'


def get_random_number():
    return random.randint(0, 100)


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Подбросить монетку")
    item2 = types.KeyboardButton("Случайное число")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Привет! Что нужно сделать?", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_commands(message):
    if message.text == "Подбросить монетку":
        coin_inline_keyboard = types.InlineKeyboardMarkup()
        coin_inline_keyboard.add(types.InlineKeyboardButton("Подбросить еще раз", callback_data='flip_a_coin'))
        bot.send_message(message.chat.id, get_coin_side(), reply_markup=coin_inline_keyboard)
    elif message.text == "Случайное число":
        number_inline_keyboard = types.InlineKeyboardMarkup()
        number_inline_keyboard.add(types.InlineKeyboardButton("Сгенерировать новое", callback_data='random_number'))
        bot.send_message(message.chat.id, str(get_random_number()), reply_markup=number_inline_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == 'flip_a_coin':
        bot.edit_message_text(f"{get_coin_side()}\nОтредактировано: {datetime.now().isoformat()}", call.message.chat.id,
                              call.message.message_id)
    elif call.data == 'random_number':
        bot.edit_message_text(f"{get_random_number()}\nОтредактировано: {datetime.now().isoformat()}",
                              call.message.chat.id, call.message.message_id)


if __name__ == "__main__":
    bot.polling(none_stop=True)
