import telebot
from telebot import types  

         
bot = telebot.TeleBot('5667974668:AAEMfaxn20wwSgknSa8fjQKBM38FG_QBPrI')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет! Нажми кнопку, чтобы поздороваться!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Почему у чау-чау язык синий?')
        btn2 = types.KeyboardButton('Что означают три звезды на небе?')
        btn3 = types.KeyboardButton('Показать котика? ^.^')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup)

    elif message.text == 'Почему у чау-чау язык синий?':
        bot.send_message(message.from_user.id, 'Есть одна китайская сказка, в ней говориться о том, что Всевышний создал многообразие зверей, заселив ими планету, после чего принялся за сотворение небес. Когда он распределял звезды по небесам, какой-то из кусочков отделился, упав на землю. Звери испугались и спрятались, но только один бесстрашный пес подошел к нему и облизал, после чего язык у собаки чау-чау приобрел синий цвет. Пес в этой сказке, само собой, предок современного чау-чау.\nПолный текст можно прочитать по ' +
                         '[ссылке](https://decordog.ru/chau-chau/opisanie-porody-chau-chau/pochemu-u-chau-chau-sinij-yazyk.html)', parse_mode='Markdown')

    elif message.text == 'Что означают три звезды на небе?':
        bot.send_message(message.from_user.id, 'Орион (как и Большая Медведица) относится к числу самых знаменитых созвездий. Он виден из обоих полушарий Земли. Три яркие звезды, расположенные в ряд, называются Поясом Ориона, двумя звёздами отмечены плечи мифического охотника. ' +
                         '[ссылке](https://pikabu.ru/story/dostoprimechatelnosti_sozvezdiya_oriona_5490239)', parse_mode='Markdown')

    elif message.text == 'Показать котика? ^.^':
        with open("cat.jpg", "rb") as f:
           bot.send_photo(message.chat.id, photo=f)
    
          
bot.polling(none_stop=True, interval=0)