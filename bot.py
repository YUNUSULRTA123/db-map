import telebot
import sys
import os
sys.path.append(os.getcwd())
from config import *
from logic import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот, который показывает города на карте 🌍\n"
        "Напиши /help, чтобы узнать, что я умею."
    )


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(
        message.chat.id,
        "📌 Доступные команды:\n"
        "/start — приветствие\n"
        "/help — список команд\n"
        "/show_city <город> — показать город на карте\n"
        "/remember_city <город> — сохранить город в список\n"
        "/show_my_cities — показать карту с твоими городами\n"
    )


@bot.message_handler(commands=['show_city'])
def handle_show_city(message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        bot.send_message(message.chat.id, "❗ Укажи город: `/show_city London`")
        return

    city_name = parts[1]
    user_id = message.chat.id

    try:
        manager.create_graph(f'{user_id}.png', [city_name])
        with open(f"{user_id}.png", "rb") as photo:
            bot.send_photo(user_id, photo)
    except Exception as e:
        bot.send_message(message.chat.id, f"Не удалось показать город 😢\nОшибка: {e}")


@bot.message_handler(commands=['remember_city'])
def handle_remember_city(message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        bot.send_message(message.chat.id, "❗ Укажи город: `/remember_city Paris`")
        return

    city_name = parts[1]
    user_id = message.chat.id

    if manager.add_city(user_id, city_name):
        bot.send_message(message.chat.id, f"Город **{city_name}** успешно сохранён! ✔")
    else:
        bot.send_message(
            message.chat.id,
            "Такого города я не знаю ❌\nУбедись, что он написан на английском."
        )


@bot.message_handler(commands=['show_my_cities'])
def handle_show_visited_cities(message):
    user_id = message.chat.id
    cities = manager.select_cities(user_id)

    if not cities:
        bot.send_message(message.chat.id, "У тебя пока нет сохранённых городов 🤷‍♂️")
        return

    try:
        manager.create_graph(f'{user_id}.png', cities)
        with open(f"{user_id}.png", "rb") as photo:
            bot.send_photo(user_id, photo)
    except Exception as e:
        bot.send_message(message.chat.id, f"Не удалось построить карту 😢\nОшибка: {e}")


if __name__ == "__main__":
    manager = DB_Map(DATABASE)
    bot.polling(none_stop=True)
