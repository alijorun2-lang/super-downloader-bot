import telebot
from telebot import types

TOKEN = "8298758056:AAHfwz7hLN8e4vZbu3so2_sv1cXNvne2jQI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً! أرسل أي فيديو / ملف صوتي / صورة وسأقوم بتنزيله لك 😊")

@bot.message_handler(content_types=['video', 'photo', 'audio', 'document'])
def handle_files(message):
    file_info = bot.get_file(message.document.file_id if message.document else
                             message.video.file_id if message.video else
                             message.photo[-1].file_id if message.photo else
                             message.audio.file_id)
    file = bot.download_file(file_info.file_path)
    bot.send_message(message.chat.id, "تم استلام الملف بنجاح ✔️")

bot.polling()
