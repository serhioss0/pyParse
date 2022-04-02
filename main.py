import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot = telebot.TeleBot(token="5081203527:AAEW_OyeTo9x52-dXx1ltrnGTQl_atdrFjs")


# Команда СТАРТ
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """Hey! I am a bot that will allow you to quickly find a car in <b><a href="https://auto.ria.com/">AutoRia</a></b>
To receive a info, enter it's name in the field...""",
                           parse_mode="html", disable_web_page_preview=1)
# ПАРСЕР
@bot.message_handler(content_types=['text'])
def parsing(message):
    url = "https://auto.ria.com/car/" + message.text
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")

    all_data = soup.find_all("div", class_="content-bar")
    for data in all_data:
        name = data.find("span", class_="blue bold").get_text(strip=True)
        price = data.find("span", class_="bold green size22").get_text(strip=True)
        date = data.find("div", class_="footer_ticket").get_text(strip=True)
        url = data.find("a", class_="address").get("href")

        bot.send_message(message.chat.id, f'Brand: {name}\nPrice: {price}$, ad added {date}\n'
                                          f"<b>\n<a href='{url}'>Buy</a></b>", parse_mode="html", disable_web_page_preview=0)

bot.polling(none_stop=True)


