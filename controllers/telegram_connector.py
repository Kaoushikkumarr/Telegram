""" Telegram_Controller """

import asyncio
from asyncio import sleep

from constants import api_id, api_hash_key


class TelegramAPIController:

    def get_telegram_api(self):
        """ GET method for Collaboration API. """
        from telethon import TelegramClient, events, sync
        asyncio.set_event_loop(asyncio.new_event_loop())
        client = TelegramClient('session_name', api_id, api_hash_key)
        client.start()
        sleep()

        print(client.get_me().stringify())

        client.send_message('me', 'Kaoushik')
        client.send_file('me', '/home/kaoushik/Downloads/IMG_20210815_114641.jpg')

        client.download_profile_photo('me')
        messages = client.get_messages('me')
        messages[0].download_media()

        @client.on(events.NewMessage(pattern='(?i)hi|hello'))
        async def handler(event):
            result = await event.respond('Hey!')
            return {
                'response': result
            }
