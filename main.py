import telebot
import psycopg2
import datetime
from telebot import types
from datetime import date  
from datetime import timedelta

now = datetime.datetime.now()
sep = datetime.datetime(now.year if now.month >= 9 else now.year - 1, 9, 1)

d1 = sep - timedelta(days=sep.weekday())
d2 = now - timedelta(days=now.weekday())
print(d1)
b = ((d2 - d1).days // 7) % 2

if b == 0 :
    b = 'нечёт'

if b ==1 :
    b = 'чёт'

bot = telebot.TeleBot('2119464296:AAHHvLPvNioNKU58ucHa6cA1zeaHhsRUi18')

conn = psycopg2.connect(database = "timetable",
                                user="postgres",
                                password="lolo2002",
                                host="localhost",
                                port="5432")
cursor = conn.cursor()

@bot.message_handler(commands=['hello'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnChet = types.KeyboardButton('Чётная неделя')
    btnNeChet = types.KeyboardButton('Нечётная неделя')
    btnSev = types.KeyboardButton('Расписание на сегодня')
    btnZav = types.KeyboardButton('Расписание на завтра')
    markup.add(btnChet)
    markup.add(btnNeChet)
    markup.add(btnSev)
    markup.add(btnZav)
    bot.send_message(message.chat.id, 'Выберите какая щас неделя' , reply_markup=markup) 



@bot.message_handler(content_types='text')
def reply_message(message):
    if message.text == 'Расписание на сегодня':
        current_dt= datetime.datetime.today().weekday()        
        result = ['Пн','Вт','Ср','Чт','Пт','Сб','Вск']
        a = result[current_dt]
        c = b
        if (current_dt == 2 or current_dt == 3 or current_dt == 5) :
            c = 'чёт/нечёт' 
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day=%s and type=%s",[str(a),str(c)])
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        if result == '':
            result = 'сегодня можно спать!'
        bot.send_message(message.chat.id, result)                                                              
        
    if message.text == 'Расписание на завтра':
        current_dt= datetime.datetime.today().weekday()        
        result = ['Пн','Вт','Ср','Чт','Пт','Сб','Вск']
        a = result[current_dt-6]
        c = b
        if (current_dt == 1 or current_dt == 2 or current_dt == 4) :
            c = 'чёт/нечёт' 
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day=%s and type=%s",[str(a),str(c)])
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        if result == '':
            result = 'сегодня можно спать!'
        bot.send_message(message.chat.id, result)    

    if message.text == 'Чётная неделя':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnPn = types.KeyboardButton('Понедельник чёт')
        btnVt = types.KeyboardButton('Вторник чёт')
        btnSr = types.KeyboardButton('Среда чёт')
        btnCht = types.KeyboardButton('Четверг чёт')
        btnPt = types.KeyboardButton('Пятница чёт')
        btnSb = types.KeyboardButton('Суббота чёт')
        btnVsk = types.KeyboardButton('Воскресенье чёт')
        markup.add(btnPn)
        markup.add(btnVt)  
        markup.add(btnSr)
        markup.add(btnCht)
        markup.add(btnPt)  
        markup.add(btnSb)
        markup.add(btnVsk)         
        bot.send_message(message.chat.id, 'Выберите дату по которой вы хотите узнать какие будут пары' , reply_markup=markup)
    if message.text == 'Понедельник чёт':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Пн' and type='чёт'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Вторник чёт':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Вт' and type='чёт'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)
        
    if message.text == 'Среда чёт':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Ср' ")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Четверг чёт':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Чт'  ")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Пятница чёт':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Пт' and type='чёт'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Суббота чёт':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Сб'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Воскресенье чёт':
        bot.send_message(message.chat.id, 'Можно спать весь день!')


    if message.text == 'Нечётная неделя':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnPn2 = types.KeyboardButton('Понедельник нечёт')
        btnVt2 = types.KeyboardButton('Вторник нечёт')
        btnSr2 = types.KeyboardButton('Среда нечёт')
        btnCht2 = types.KeyboardButton('Четверг нечёт')
        btnPt2 = types.KeyboardButton('Пятница нечёт')
        btnSb2 = types.KeyboardButton('Суббота нечёт')
        btnVsk2 = types.KeyboardButton('Воскресенье нечёт')
        markup.add(btnPn2)
        markup.add(btnVt2)  
        markup.add(btnSr2)
        markup.add(btnCht2)
        markup.add(btnPt2)  
        markup.add(btnSb2)
        markup.add(btnVsk2)         
        bot.send_message(message.chat.id, 'Выберите дату по которой вы хотите узнать какие будут пары' , reply_markup=markup)

    if message.text == 'Понедельник нечёт':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Пн' and type='нечёт'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Вторник нечёт':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Вт' and type='нечёт'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)
        
    if message.text == 'Среда нечёт':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Ср'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Четверг нечёт':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Чт'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Пятница нечёт':
        bot.send_message(message.chat.id, 'Можно спать весь день!')

    if message.text == 'Суббота нечёт':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Сб'")
        records = cursor.fetchall()
        result = ''
        i = 0
        for arr in records :
            for word in arr:
                result=result +str(word)+' '
                i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        bot.send_message(message.chat.id, result)

    if message.text == 'Воскресенье нечёт':
        bot.send_message(message.chat.id, 'Можно спать весь день!')



bot.infinity_polling()