import telegram
from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import time
from telegram import InlineQueryResultArticle, ChatAction, InputTextMessageContent
import requests
from bs4 import BeautifulSoup
import random
import datetime
import emoji

bot = telegram.Bot(token=)
updater = Updater(token='')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text= "")
        
                    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def weather(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    url = 'http://www.accuweather.com/en/sg/singapore/300597/daily-weather-forecast/300597'
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    weather = soup.find('span', {'class':'cond'}).text
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d")
    print(time)
    print(weather)
    update.message.reply_text(time + "\n"  + weather)
    
weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)

url = 'https://www.dailyinspirationalquotes.in/'
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
quote = soup.select('.td-module-thumb a')
i = random.randint(1, 10)
q = quote[i].get('title')
    
def problem(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text="")
    time.sleep(5)
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    update.message.reply_text("")
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    update.message.reply_text(q)
problem_handler = CommandHandler('problem', problem)
dispatcher.add_handler(problem_handler)
updater.start_polling()

def reply(bot, update):
    di = ['Is it worse to fail at something or never attempt it in the first place?', 'Does nature shape our personalities more than nurture?', 'What is true happiness?',
          'What makes a good friend?', 'Who defines good and evil?', 'What is the difference between living and being alive?', 'Who decides what morality is?', 'What is true love?', 'What role does honour play in today’s society?']
    d = random.randint(0,8)
    bot.sendMessage(chat_id=update.message.chat_id, text=di[d])
reply_handler = MessageHandler(Filters.text, reply)
dispatcher.add_handler(reply_handler)

def trip(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text= '')
                       
trip_handler = CommandHandler('trip', trip)
dispatcher.add_handler(trip_handler)


#added last
def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

    

    
