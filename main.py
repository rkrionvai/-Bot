import telebot

API_TOKEN = "8538589891:AAFMHtGeJP0-1DcZaRaCwqM5hoKSDX96tWg"
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True, content_types=['text', 'photo', 'sticker', 'video', 'animation', 'audio', 'voice', 'document'])
def react_to_all(message):
    try:
        bot.set_message_reaction(message.chat.id, message.message_id, [telebot.types.ReactionTypeEmoji("❤️")])
    except Exception as e:
        print(f"Error: {e}")

bot.infinity_polling(timeout=20, long_polling_timeout=10)
