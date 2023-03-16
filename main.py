import telebot
import os
import traceback
from fuzzywuzzy import fuzz
bot = telebot.TeleBot('6244691485:AAFTRfhveZaCaDCjCOOp82FOBt1LviD9ZKs')
mas = []
if os.path.exists('data/boltun.txt'):
    f = open('data/boltun.txt','r', encoding='UTF-8')
    for x in f:
        if len(x.strip()) > 2:
            mas.append(x.strip().lower())
    f.close()
def answer(text):
    try:
        text = text.lower().strip()
        if os.path.exists('data/boltun.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if 'u:' in q:
                   fromfile = (fuzz.token_sort_ratio(q.replace( 'u:', ''),text))
                   if fromfile > a and fromfile != a:
                       a = fromfile
                       nn = n
                n = n + 1
            s = mas[nn +1]
            return s
        else:
            return 'Нет файла'
    except Exception:
        return 'Иная ошибка'+str(traceback.format_exc())
@bot.message_handler(commands=['start'])
def start(m,res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне "Привет" или задай вопрос.')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    f  = open('data/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    s = answer(message.text)
    f.write('u:' + message.text + '\n' + s + '\n')
    f.close()
    bot.send_message(message.chat.id, s)
bot.polling(none_stop=True, interval=0)




























