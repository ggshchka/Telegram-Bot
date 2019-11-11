# -*- coding: utf-8 -*-
import telebot
import converter
import time

url = ''
mp3_file = ''
bot = telebot.TeleBot('996144487:AAEaCujc637KC6HgOOd4uMgnvMtzRJoBZQ4')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, it is a YouTube Converter. Send URL of YouTube video to convert it to mp3')

@bot.message_handler(content_types=['text'])
def get_url(message):
	try:
		url = message.text
		mp3_file = converter.convert(url)
		bot.send_message(message.chat.id, 'Wait a sec...\n{} is loading...'.format(mp3_file[6 : -4]))
		audio = open(mp3_file, 'rb')
		bot.send_audio(message.chat.id, audio)
		converter.delete(mp3_file)
	except:
		bot.send_message(message.chat.id, 'Check your URL and try again')

bot.polling()