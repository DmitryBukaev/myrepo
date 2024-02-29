import telepot
import time

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Got command: %s' % command)
    print('From : %s' % chat_id)
    if command == '/command1':
        bot.sendMessage(chat_id, 'Oks')
    elif command == '/command2':
        bot.sendMessage(chat_id, 'Ok')

bot = telepot.Bot('6712915454:AAGZxTwmmHHvg97p788jQ5JoqUz2gGNKYj0')
bot.message_loop(handle)
print('I am listening ...')
while 1:
    time.sleep(10)
