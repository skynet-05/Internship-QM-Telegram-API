from telegram.client import Telegram

tg = Telegram(
    api_id='api_id',
    api_hash='api_hash',
    phone='+31611111111',
    database_encryption_key='changeme1234',
)
tg.login()

def new_message_handler(update):
    # we want to process only text messages
    message_content = update['message']['content'].get('text', {})
    message_text = message_content.get('text', '').lower()

    if message_text == 'ping':
        chat_id = update['message']['chat_id']
        print(f'Ping has been received from {chat_id}')
        tg.send_message(
            chat_id=chat_id,
            text='pong',
        )

tg.add_message_handler(new_message_handler)
tg.idle()
