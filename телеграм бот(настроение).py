import telebot
import emoji
from telebot import types
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
import constants
from enum import Enum   



API_TOKEN = '1708518024:AAFUZMDfSBZo_mBM8YnhXtHcMzi0NTQNLpM'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def welcom_text(message):
    bot.send_message(message.chat.id, 'как дела?')

good = ['😀','😃','😄','😁','😆','😂','😊','🤩','🥳']
norm = ['🤨,😕,🙁,☹️,😟,😔,😞,😒,😖,😩,😫']
gru = ['😡,🤬,🤯,👿,👺,😐,😬,😤']

@bot.message_handler(content_types=['text'])
def good_text(message):
    if message.text.lower() == (good):    
        bot.send_message(message.chat.id, 'Хорошечненько,приходите к нам')
    elif message.text.lower() == (norm):
        bot.send_message(message.chat.id, 'норма,тогда купи слона....просто так надо.')
    elif message.text.lower() == (gru):
        bot.send_message(message.chat.id, 'оувоу пологче, глянь ютюбчик, зацени смешные видосики "<a href= https://www.youtube.com/results?search_query=%D1%81%D0%BC%D0%B5%D1%88%D0%BD%D1%8B%D0%B5+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE>YouTube</a>"')


bot.polling()
