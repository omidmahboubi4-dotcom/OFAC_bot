import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "⛔ دسترسی غیرمجاز")
        return
    bot.reply_to(message, "🤖 ربات فعال است و فقط در اختیار شماست")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.from_user.id != OWNER_ID:
        return
    bot.reply_to(message, f"📩 پیام دریافت شد:
{message.text}")

print("ربات در حال اجراست...")
bot.infinity_polling()