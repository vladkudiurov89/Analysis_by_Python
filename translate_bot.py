""" Телеграм - Бот для перевода слов и фраз"""
import requests
import telebot
import json
import os
from config import Yandex_API, TOKEN_BOT
import telebot

key = Yandex_API
bot = telebot.TeleBot(TOKEN_BOT)
language = {'en', 'ru'}


@bot.message_handler(commands=['start'])
def start(message):
    """Метод для начала работы с переводчиком """
    bot.send_message(message.from_user_id, 'Hello you work with yandex.translate')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    """ Метод для отравки и получения запроса с yandex_translate,
     и для отправки сообщения пользователю"""

    """ Функция для перевода:
    входные данные : Строка (разбивает ее на слова для проверки)
        _слово_ или _фраза_ "to" _язык для перевода_(проверка на наличие словоря)
       Направление перевода.
    Может задаваться одним из следующих способов:
    В виде пары кодов языков («с какого»-«на какой»), разделенных дефисом. 
    Например, en-ru обозначает перевод с английского на русский.
    В виде кода конечного языка (например ru). В этом случае сервис пытается определить исходный язык автоматически. 
    """

    text = message.text
    lang_dest = text.split()[-1] # 'en'
    if 'to' in text and len(text.split()) > 2 and check_lang(lang_dest):
        text = text.split()
        del text[-2], text[-1] # удаляем 'to' и 'en'
        text = ' '.join(text)
        r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate',
                         params={key: 'key', 'text': text, 'lang': lang_dest,
                                 'format': 'plain', 'options': '1'})
        # res = r.text.json()
        res = json.loads(r.text)
        if res['code'] != 200:
            bot.send_message(chat_id=update.message.chat_id,
                             text='Oшибка на стороне Yandex')
        else:
            bot.send_message(chat_id=update.message.chat_id, text="""Перевод [{}]: {}""".format(res['lang'], res['text']))

    else:
        bot.send_message(chat_id=update.message.chat_id, text='Ошибка ввода')
    return true


def check_lang(lang):
    """Функция на проверку наличия текста"""
    if lang.lower() in language:
        return True
    else:
        return False


bot.polling(none_stop=True)

