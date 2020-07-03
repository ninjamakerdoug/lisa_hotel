# -*- coding: utf-8 -*-

from Chatbot import Chatbot
import telepot

telegram = telepot.Bot("1394501396:AAFAZNVtTQjUA0KroJoB-CEvYxWTQmHjKzU")
bot = Chatbot("lisa")


def recebendoMsg(msg):
    autorizados = ['1090587812','1098085687','1189885928']
    frase = bot.escuta(frase=msg['text'])
    chatID = msg['chat']['id']
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    if frase == 'meu id':
        resp = str(chatID)
    else:
        chatID = str(chatID)
        if chatID in autorizados:
            resp = bot.pensa(frase)
        else:
            resp = 'Não autorizado'
    bot.fala(resp)
    telegram.sendMessage(chatID,resp)
telegram.message_loop(recebendoMsg)


while True:
    pass
