
import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به ربات خوش اومدی 🤖")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"📩 پیام دریافت شد")

bot.infinity_polling()
