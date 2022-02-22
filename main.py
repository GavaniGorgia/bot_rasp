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
b = ((d2 - d1).days // 7) % 2

if b == 0 :
    b = 'нечёт'

if b ==1 :
    b = 'чёт'

bot = telebot.TeleBot('5205958199:AAHgNJKEtMXC5D2v3Ou_OVxckLiHFdkkE4E')

conn = psycopg2.connect(database = "timetable",
                                user="postgres",
                                password="lolo2002",
                                host="localhost",
                                port="5432")
cursor = conn.cursor()

@bot.message_handler(commands=['help'])
def help_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnComm = types.KeyboardButton('Список команд')
    btnMe = types.KeyboardButton('Информация о себе')
    btnDoc = types.KeyboardButton('Краткая документация')
    markup.add(btnComm)
    markup.add(btnMe)
    markup.add(btnDoc)
    bot.send_message(message.chat.id, 'Здравствуйте, выберите пункт, о котором бы хотели узнать получше' , reply_markup=markup) 

@bot.message_handler(commands=['mtuci'])
def mtuci_message(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/' )

@bot.message_handler(commands=['week'])
def mtuci_message(message):
    c=b
    if c == 'нечёт':
        c = 'Верхняя неделя'
    else:
        c = 'Нижняя неделя'
    bot.send_message(message.chat.id, c)

 




@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnPn = types.KeyboardButton('Понедельник')
    btnVt = types.KeyboardButton('Вторник')
    btnSr = types.KeyboardButton('Среда')
    btnCht = types.KeyboardButton('Четверг')
    btnPt = types.KeyboardButton('Пятница')
    btnSb = types.KeyboardButton('Суббота')
    btnNow = types.KeyboardButton('Текущая неделя')
    btnNext = types.KeyboardButton('Следующая неделя')
    btnSev = types.KeyboardButton('Расписание на сегодня')
    btnZav = types.KeyboardButton('Расписание на завтра')
    markup.add(btnPn)
    markup.add(btnVt)  
    markup.add(btnSr)
    markup.add(btnCht)
    markup.add(btnPt)  
    markup.add(btnSb)
    markup.add(btnNow)
    markup.add(btnNext)
    markup.add(btnSev)
    markup.add(btnZav)
    bot.send_message(message.chat.id, 'Здравствуйте, уточните чтобы вы хотели узнать' , reply_markup=markup) 



@bot.message_handler(content_types='text')
def reply_message(message):
    if message.text == 'Список команд':
        bot.send_message(message.chat.id, '/week - покажет какая щас неделя \n /mtuci - ссылка на университет \n /help - помощь ,если будут вопросы  \n /start- вы можете посмотреть расписание на неделю ')        

    if message.text == 'Информация о себе':
         bot.send_message(message.chat.id,'Студент группы Бин2005')

    if message.text == 'Краткая документация':
        bot.send_message(message.chat.id,'https://github.com/GavaniGorgia')

    if message.text == 'Расписание на сегодня':
        current_dt= datetime.datetime.today().weekday()        
        result = ['Пн','Вт','Ср','Чт','Пт','Сб','Вск']
        a = result[current_dt]
        c = b
        if (current_dt == 2 or current_dt == 3 or current_dt == 5) :
            c = 'чёт/нечёт' 
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day=%s and type=%s",[str(a),str(c)])
        records = cursor.fetchall()
        result = a +'\n'+ '---------------'+'\n'
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
                    result = 'Выходной!'
        result+='---------------'
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
        print(records)
        result = a +'\n'+ '---------------'+'\n'
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
                    result = 'Выходной!'
        result+='---------------'
        bot.send_message(message.chat.id, result)    

    if message.text == 'Понедельник':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Пн' and type=%s",[str(b)])
        records = cursor.fetchall()
        result = 'Пн'+'\n'+ '---------------'+'\n'
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
                    result = 'Выходной!'
        result+='---------------'
        bot.send_message(message.chat.id, result)

    if message.text == 'Вторник':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Вт' and type=%s",[str(b)])
        records = cursor.fetchall()
        result = 'Вт'+'\n'+ '---------------'+'\n'
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
                    result = 'Выходной!'
        result+='---------------'
        bot.send_message(message.chat.id, result)
        
    if message.text == 'Среда':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Ср' ")
        records = cursor.fetchall()
        result = 'Ср'+'\n'+ '---------------'+'\n'
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
                    result = 'Выходной!'
        result+='---------------'
        bot.send_message(message.chat.id, result)

    if message.text == 'Четверг':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Чт'  ")
        records = cursor.fetchall()
        result = 'Чт'+'\n'+ '---------------'+'\n'
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
                    result = 'Выходной!'
        result+='---------------'
        bot.send_message(message.chat.id, result)

    if message.text == 'Пятница':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Пт' and type=%s",[str(b)])
        records = cursor.fetchall()
        result = 'Пт'+'\n'+ '---------------'+'\n'
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
                    result = 'Выходной!'
        result+='---------------'
        bot.send_message(message.chat.id, result)

    if message.text == 'Суббота':
        cursor.execute("SELECT subject ,room ,time FROM timetable WHERE day='Сб'")
        records = cursor.fetchall()
        result = 'Сб'+'\n'+ '---------------'+'\n'
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
                    result = 'Выходной!'
        result+='---------------'
        bot.send_message(message.chat.id, result)

    if message.text == 'Текущая неделя':
        
        cursor.execute("SELECT day,subject ,room ,time FROM timetable WHERE type=%s or type='чёт/нечёт'",[str(b)])
        records = cursor.fetchall()
        result = ''
        i = 0
        c= ''
        g = 0
        for arr in records :
            for word in arr:
                if str(word)==arr[0]:
                    if arr[0]!=c:
                        c=arr[0]
                        if g==0:
                            result=result+str(word)+'\n'+'---------------'+'\n'
                        if g!=0:
                            result=result+'---------------'+'\n'+str(word)+'\n'+'---------------'+'\n'
                        g=g+1
                if c==arr[0]:
                    if str(word)==c:
                        result+=''
                    if str(word)!=c:
                        result=result +str(word)+' '
                        i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        result+='---------------'
                
        bot.send_message(message.chat.id, result)

    if message.text == 'Следующая неделя':
        c=b
        if c == 'чёт':
            c = 'нечёт'
        else:
            c = 'нечёт'
        cursor.execute("SELECT day,subject ,room ,time FROM timetable WHERE type=%s or type='чёт/нечёт'",[str(c)])
        records = cursor.fetchall()
        result = ''
        i = 0
        c= ''
        g = 0
        for arr in records :
            for word in arr:
                if str(word)==arr[0]:
                    if arr[0]!=c:
                        c=arr[0]
                        if g==0:
                            result=result+str(word)+'\n'+'---------------'+'\n'
                        if g!=0:
                            result=result+'---------------'+'\n'+str(word)+'\n'+'---------------'+'\n'
                        g=g+1
                if c==arr[0]:
                    if str(word)==c:
                        result+=''
                    if str(word)!=c:
                        result=result +str(word)+' '
                        i=i+1
                if i==3 :
                    result+='\n'
                    i = 0
                else:
                    result+=''
        result+='---------------'

        bot.send_message(message.chat.id, result)


bot.infinity_polling()
