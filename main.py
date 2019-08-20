import time

import telepot

from telegram import bot

BOT_TOKEN = "850993777:AAGgJpamkp3O2Mea05GZakHR59fpJqJRgyo"


def handle(msg):
    """
    Receive message and pass the command to call the corresponding function.
    :param msg: Message received by the bot
    """
    content_type, chat_type, chat_id = telepot.glance(msg)

    # you can add more content type, like if someone send a picture
    if msg.get('text'):
        bot.sendMessage(chat_id, msg.get('text'))

    if msg.get('entities'):
        for ent in msg.get('entities'):
            if ent.get('type') == 'url':
                bot.sendMessage(chat_id, ent)


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def features(command):
    """ Regroup all commands"""
    if '#' in command:
        return find(command, '#')


if __name__ == '__main__':
    bot = telepot.Bot(BOT_TOKEN)
    bot.message_loop(handle)

    print('Listening ...')
    while True:
        time.sleep(1)