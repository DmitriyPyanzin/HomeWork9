from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import emoji

bot = Bot(token='5602721625:AAG9YTpYwbgNmWgdV4Ll924W60Z9y0bEl74')
updater = Updater(token='5602721625:AAG9YTpYwbgNmWgdV4Ll924W60Z9y0bEl74')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет!\nВы вводите слова с клавиатуры.\n'
                                                       'В некоторых специально допустите ошибки написав\n'
                                                       'сочетание букв "абв", а я выведу текст без них\n')


def finish(update, context):
    smile = emoji.emojize(':red_heart:', variant="emoji_type")
    context.bot.send_message(update.effective_chat.id, f'Возвращайся скорее! {smile}\n'
                                                       'Для возобновления работы нажмите /start')


def find_words(update, context):
    flag = True
    while flag:
        new_text = ''
        text = update.message.text.split()
        for i in text:
            if 'абв' in i.lower():
                continue
            else:
                new_text += i + ' '
        context.bot.send_message(update.effective_chat.id, f'Вот что получилось: {new_text}')
        flag = not flag


start_handler = CommandHandler('start', start)
finish_handler = CommandHandler('finish', finish)
find_words_handler = MessageHandler(Filters.text, find_words)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(finish_handler)
dispatcher.add_handler(find_words_handler)

updater.start_polling()
updater.idle()
