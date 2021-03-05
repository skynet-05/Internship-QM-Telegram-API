import logging
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import pymongo


mc=pymongo.MongoClient("mongodb://127.0.0.1:27017/")

tgdb=mc["telemetrixdb"]

tgcol=tgdb["rohitsmessages"]


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hi!')


def help(update, context):
    update.message.reply_text('This bot replies with the same message you send :)')


def echo(update, context):
    global tgdb
    global tgcol
    now = datetime.datetime.now()
    update.message.reply_text(update.message.text)
    user = update.message.from_user
    print('At '+now.strftime("%d-%m-%Y | %H:%M")+' User {} , User ID: {} , Full Name: {} {} sent this text:'.format(user['username'], user['id'], user['first_name'], user['last_name']))
    print(update.message.text)
    data={"first name":user["first_name"],"last name":user['last_name'],"userid":user['id'],"username":user['username'],"message":update.message.text,"date and time":now.strftime("%d-%m-%Y | %H:%M")}
    tgcol.insert_one(data)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(config.token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
