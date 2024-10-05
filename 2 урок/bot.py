import confiп

import telebot



bot = telebot.TeleBot(token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@dp.message_handler(commands=['weather'])
async def weather_handler(message: types.Message):
    await bot.send_message(message.chat.id, text='Введи название города...')

    @dp.message_handler()
    async def get_city_name(message: types.Message):
        # обработка введённых данных от юзера
        pass
    
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message( ):
    bot.reply_to(message, message.text)


bot.infinity_polling()