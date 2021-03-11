import logging
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import requests

URL = "https://api.telegram.org/bot{}/".format(config.token)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def start(update, context):
    update.message.reply_text('Hi!')


def help(update, context):
    update.message.reply_text('User replies to messages')


def reply(update, context):
    
    now = datetime.datetime.now()
    #update.message.reply_text(update.message.text)
    user = update.message.from_user
    print('At '+now.strftime("%d-%m-%Y | %H:%M")+' User {} , User ID: {} , Full Name: {} {} sent this text:'.format(user['username'], user['id'], user['first_name'], user['last_name']))
    print(update.message.text)
    text = input('Enter to replay: ')
    url = URL + "sendMessage?text={}&chat_id={}".format(text, user['id'])
    get_url(url)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(config.token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, reply))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
