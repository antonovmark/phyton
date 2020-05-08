import TeleBot
bot = TeleBot.TeleBot("1119302081:AAEPZl9Y5gAwP4apFuhET2Aa_qlSrZn8gUQ")


@bot.message_handler(contet_types=['text'])
def send_echo(message):
    bot.reply_to(message, message.text)
    bot.send_message()
