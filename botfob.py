from telegram.ext import Updater, CommandHandler
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
import asyncio

BOT_TOKEN = '7770419737:AAGDQcoZPz8k0FqZdUQ5hPdk0W1GP78I1Ic'  
API_ID = '25741913'  
API_HASH = '51d52fa2d86be95219e48dd61bf59645' 
PHONE = '+996507555894'  
YOUR_CHAT_ID = '930678932'  

CHANNELS = ['@findwork', '@codifynews']  

client = TelegramClient('session_name', API_ID, API_HASH)

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

def start(update, context):
    update.message.reply_text('Бот запущен! Отслеживаю вакансии.')

dp.add_handler(CommandHandler('start', start))

async def check_channels():
    await client.start(phone=PHONE)
    while True:
        for channel_name in CHANNELS:
            channel = await client.get_entity(channel_name)
            async for message in client.iter_messages(channel, limit=1): 
                if message.text:  
                    if any(keyword in message.text.lower() for keyword in ['Android', 'Kotlin', 'android']):
                        updater.bot.send_message(chat_id=YOUR_CHAT_ID, text=f"Новая вакансия в {channel_name}:\n{message.text}")
        await asyncio.sleep(300)  

if __name__ == '__main__':
    updater.start_polling()
    loop = asyncio.get_event_loop()
    loop.create_task(check_channels())
    loop.run_forever()
