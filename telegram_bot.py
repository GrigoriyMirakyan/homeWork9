from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler


bot = Bot(token='5492812666:AAFttoWzPNS3eO-0p60bpcKsYidJzcc5j1I')
updater = Updater(token='5492812666:AAFttoWzPNS3eO-0p60bpcKsYidJzcc5j1I')
dispatcher = updater.dispatcher

STATE0 = 1
STATE1 = 2
STATE2 = 3
STATE3 = 4


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Я бот-калькулятор.\nНапиши какие числа посчитать, рациональные или комплексные?\nДля выхода введи /cancel')

    return STATE0


def message0(update, context):

    if 'раци' in update.message.text.lower():
        context.bot.send_message(
            update.effective_chat.id, '\nНапиши пример используя +-*/\nНапример 5 + 5\nДля выхода введи /cancel')
        return STATE1
    elif 'комп' in update.message.text.lower():
        context.bot.send_message(
            update.effective_chat.id, 'Напиши пример используя +-*/\nНапример 2-3j + 27+7j\nДля выхода введи /cancel')
        return STATE2
    else:
        context.bot.send_message(
            update.effective_chat.id, 'Я тебя не очень хорошо понял.')
        return STATE0


def message1(update, context):
    context.bot.send_message(
        update.effective_chat.id, '\nНапиши пример используя +-*/\nНапример 5 + 5\nДля выхода введи /cancel')
    msg = update.message.text
    items = msg.split()
    x = float(items[0])
    y = float(items[2])
    action = items[1]
    if action == '+':
        update.message.reply_text(f'{x} + {y} = {x+y}')
        return STATE0
    elif action == '-':
        update.message.reply_text(f'{x} - {y} = {x-y}')
        return STATE1
    elif action == '*':
        update.message.reply_text(f'{x} * {y} = {x*y}')
        return STATE1
    elif action == '/':
        update.message.reply_text(f'{x} / {y} = {x/y}')
        return STATE1
    else:
        update.message.reply_text(f'Что-то пошло не так!!')
    return STATE0


def message2(update, context):
    context.bot.send_message(
        update.effective_chat.id, 'Напиши пример используя +-*/\nНапример 2-3j + 27+7j\nДля выхода введи /cancel')
    msg = update.message.text
    items = msg.split()
    x = complex(items[0])
    y = complex(items[2])
    action = items[1]
    if action == '+':
        update.message.reply_text(f'{x} + {y} = {x+y}')
        return STATE2
    elif action == '-':
        update.message.reply_text(f'{x} - {y} = {x-y}')
        return STATE2
    elif action == '*':
        update.message.reply_text(f'{x} * {y} = {x*y}')
        return STATE2
    elif action == '/':
        update.message.reply_text(f'{x} / {y} = {x/y}')
        return STATE2
    else:
        update.message.reply_text(f'Что-то пошло не так!!')
    return STATE0


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Рад был пообщаться! Всего доброго!')

    return ConversationHandler.END


start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
message0_handler = MessageHandler(Filters.text, message0)
message1_handler = MessageHandler(Filters.text, message1)
message2_handler = MessageHandler(Filters.text, message2)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={STATE0: [message0_handler],
                                           STATE1: [message1_handler],
                                           STATE2: [message2_handler]},
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(conv_handler)


# В конце |||
print('Server start')
updater.start_polling()
updater.idle()  # ctrl + C
