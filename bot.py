import telebot

bot = telebot.TeleBot("8404730679:AAHSlx4Kwhxc7rhgTc9pXxAyStldlQclBN8")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "  https://ouo.io/YOUR_SHORT_LINK:\n\nhttps://ouo.io/YOUR_SHORT_LINK")

bot.polling()
