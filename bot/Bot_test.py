import telebot
token = '335134502:AAEFvsBH_icdljXBfimaG3h0_zT2cYtGZ6U'


bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    print(message.chat.id)

if __name__ == '__main__':
     bot.send_message(321732078, "kurwa")
     bot.polling(none_stop=True)
