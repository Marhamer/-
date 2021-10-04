import telebot

BOT_TOKEN = '1740057462:AAExBv7ssXjuiKugi6A5gIpLA2R3m-jA514'

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def handle_message(message):
    bot.reply_to(message, 'Привет')

@bot.message_handler(content_types=['text'])
def handle_message(message):
    bot.reply_to(message,message.text)

bot.polling()
