import telebot


 
from telebot import types
 
bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def welcome(message):
    
    
 
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    item3 = types.KeyboardButton("Интересно")
    item4 = types.KeyboardButton("Познавательно")
    item5 = types.KeyboardButton("Увлекательно")
    item6 = types.KeyboardButton("👏")
    item7 = types.KeyboardButton("Не очень")
    item8 = types.KeyboardButton("Отлично")
    item9 = types.KeyboardButton("Креативно")
    item10 = types.KeyboardButton("Скучно")
    item11= types.KeyboardButton("👍")
    item12= types.KeyboardButton("Оригинально")
    item13= types.KeyboardButton("Потрясающе")
    item14= types.KeyboardButton("Эмоционально")
    item15= types.KeyboardButton("👎")
    item16 = types.KeyboardButton("Наглядно") 
    item17 = types.KeyboardButton("Утомительно")
    item18 = types.KeyboardButton('🤝')
    item19 = types.KeyboardButton('😀')
    item20 = types.KeyboardButton('🔥')

    
    
    
 
    markup.add(item5, item14, item16, item4, item12, item8, item9, item3, item10, item7, item13, item17, item11, item19, item6,item18, item15, item20)
 
    bot.send_message(message.chat.id, 'Приветствую, {0.first_name}!\nПонравилась ли Вам игра-викторина "Ты в наших сердцах, Сталинград - навсегда!"? '.format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 

@bot.message_handler(content_types=['text'])
def lalala(message):
    chat = ["message.chat.id"]
    if message.text=="👍":
        bot.send_message(chat, "👍")
    if message.text=="👏":
        bot.send_message(chat, "👏")
    if message.text=="👎":
        bot.send_message(chat, "👎")
    if message.text=="Интересно":
        bot.send_message(chat, "Интересно")
    if message.text=="Познавательно":
        bot.send_message(chat, "Познавательно")
    if message.text=="Увлекательно":
        bot.send_message(chat, "Увлекательно")
    
    if message.text=="Не очень":
        bot.send_message(chat, "Не очень")
    if message.text=="Отлично":
        bot.send_message(chat, "Отлично")
    if message.text=="Креативно":
        bot.send_message(chat, "Креативно")
    if message.text=="Скучно":
        bot.send_message(chat, "Скучно")
    
    if message.text=="Оригинально":
        bot.send_message(chat, "Оригинально")
    if message.text=="Потрясающе":
        bot.send_message(chat, "Потрясающе")
    if message.text=="Эмоционально":
        bot.send_message(chat, "Эмоционально")
    
    if message.text=="Наглядно":
        bot.send_message(chat, "Наглядно")
    if message.text=="Утомительно":
        bot.send_message(chat, "Утомительно")
    
    if message.text=='🔥':
        bot.send_message(chat, '🔥')
    if message.text=='😀':
        bot.send_message(chat, '😀')
    if message.text=='🤝':
        bot.send_message(chat, '🤝')
    
    

   




bot.polling(none_stop=True)


