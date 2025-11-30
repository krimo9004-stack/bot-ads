import telebot

TOKEN = "8404730679:AAHSlx4Kwhxc7rhgTc9pXxAyStldlQclBN8"

bot = telebot.TeleBot(TOKEN)

# رابط الإعلان الخاص بك
ad_link = "https://ouo.io/HPS3uw"

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton(
        text="🔗 اضغط لمشاهدة الإعلان",
        url=ad_link
    )
    keyboard.add(btn)

    bot.send_message(
        message.chat.id,
        "👋 أهلاً بك!\n\nاضغط على الزر لمشاهدة الإعلان وكسب النقاط 🔥",
        reply_markup=keyboard
    )

print("Bot is running...")
bot.polling()
