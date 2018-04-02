import pymongo
from builtins import print
from pymongo import MongoClient
import datetime
import pprint
import time

import telebot
from telebot import types
import os
API_TOKEN = '469509215:AAHCAF2jI5CsEpJFUzG6WhRKLbpJIuVN9vw'
bot = telebot.TeleBot(API_TOKEN)
client = MongoClient('localhost', 27017)
db = client.test_MD_Todo
tag_collection = db.tag

markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
hideBoard = types.ReplyKeyboardRemove()


@bot.message_handler(content_types='photo')
def photo(message):

    fileId=message.photo[-1].file_id
    file_info = bot.get_file(fileId)
    print('file.file_path =', file_info.file_path)
    #os.system()


@bot.message_handler(commands=['Help','help'])
def start(message):
    ans='/dog : Get info about dog \n' \
        '/cat : Get info about cat \n' \
        '/sheep : Get info about sheep \n' \
        '/cow : Get info about cow \n' \
        '/horse : Get info about horse \n' \
        '/elephant : Get info about elephant \n' \
        '/bear : Get info about bear \n' \
        '/zebra : Get info about zebra \n' \
        '/bear : Get info about bear'
    bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['Dog','dog'])
def dog_method(message):
    ans = 'The domestic dog (Canis lupus familiaris or Canis familiaris)[4] is a member of the genus Canis' \
          ' (canines), which forms part of the wolf-like canids,[5] and is the most widely abundant ' \
          'terrestrial carnivore.[6][7][8][9][10] The dog and the extant gray wolf are sister taxa[11][12][13]' \
          ' as modern wolves are not closely related to the wolves that were first domesticated,[12][13] ' \
          'which implies that the direct ancestor of the dog is extinct.[14] The dog was the first species' \
          ' to be domesticated[13][15] and has been selectively bred over millennia for various behaviors,' \
          ' sensory capabilities, and physical attributes.[16]'
    bot.send_message(message.chat.id, ans)

@bot.message_handler(commands=['Cat','cat'])
def cat_method(message):
    ans = ''
    bot.send_message(message.chat.id, ans)

@bot.message_handler(commands=['Horse','horse'])
def horse_method(message):
    ans = ''
    bot.send_message(message.chat.id, ans)

@bot.message_handler(commands=['sheep','sheep'])
def sheep_method(message):
    ans = ''
    bot.send_message(message.chat.id, ans)

@bot.message_handler(commands=['Cow','cow'])
def cow_method(message):
    ans = ''
    bot.send_message(message.chat.id, ans)

@bot.message_handler(commands=['Elephant','elephant'])
def elephant_method(message):
    ans = ''
    bot.send_message(message.chat.id, ans)

@bot.message_handler(commands=['Bear','bear'])
def bear_method(message):
    ans = ''
    bot.send_message(message.chat.id, ans)

@bot.message_handler(commands=['Zebra','zebra'])
def zebra_method(message):
    ans = ''
    bot.send_message(message.chat.id, ans)

@bot.message_handler(commands=['Giraffe','giraffe'])
def giraffe_method(message):
    ans = ''
    bot.send_message(message.chat.id, ans)


@bot.message_handler(content_types='text')
def additional(message):
    ans = 'Command does not recognized. Please enter valid command or use /help command to know about commands.'
    bot.send_message(message.chat.id, ans)


bot.polling()