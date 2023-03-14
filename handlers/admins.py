import requests
from aiogram.types import ReplyKeyboardRemove
from bot import bot, dp
from db import actions
from handlers.private import get_random_name
from misc import messages, secrets
from misc.states import Approve

admin_group_id = -1001908884821
admin_channel_id = -1001751669371


@dp.callback_query_handler(lambda d: 'approve_' in d.data)
async def approve_validation(data):
    await data.answer(messages.APPROVED)
    await data.message.edit_text(
        text=f"{messages.NEW_POST(actions.get_obj_by_id(int(data.data.split('_')[1])))}",
        parse_mode='MarkdownV2')
    await bot.send_message(dict(data)['from']['id'], messages.SEND_CONFIRMATION_SENT_PHOTO)
    await Approve.set_file.set()


@dp.message_handler(state=Approve.set_file, content_types=['photo'])
async def validate_photo(message, state):
    print(message)
    filename = 'db/files/' + await get_random_name() + '.jpg'
    await message.photo[-1].download(filename)
    await state.finish()
    actions.set_admin_photo(filename, message.chat.id)
    await bot.send_message(message.chat.id, messages.MONEYS_SENT)

@dp.message_handler()
async def new_thread(message):
    if dict(message)['from']['id'] == 777000:
        url = f"https://api.telegram.org/bot{secrets.secret_info.TELEGRAM_API_TOKEN}/sendMessage"
        params = {
            "chat_id": {message.chat.id},
            "text": messages.WELCOME_TO_CONVERSATIONS,
            "reply_to_message_id": message.message_id
        }
        requests.post(url, params=params)
