import requests
from aiogram.types import ReplyKeyboardRemove, Message
from bot import bot, dp
from db import actions
from handlers.private import get_random_name
from misc import messages, secrets
from misc.states import Approve

admin_group_id = -1001908884821
admin_channel_id = -1001751669371


@dp.callback_query_handler(lambda d: 'approve_' in d.data)
async def approve_validation(data):
    print(data.data.split('_')[1]) # TODO: edit this 
    await data.answer(messages.APPROVED)
    await data.message.edit_text(
        text=f"{(actions.get_obj_by_id(int(data.data.split('_')[1])))}")



@dp.message_handler(state=Approve.set_file, content_types=['photo'])
async def validate_photo(message, state):
    print(message)
    filename = 'db/files/' + await get_random_name() + '.jpg'
    await message.photo[-1].download(filename)
    await state.finish()
    actions.set_admin_photo(filename, message.chat.id)
    await bot.send_message(message.chat.id, messages.MONEYS_SENT)

@dp.message_handler()
async def new_thread(message: Message):
    if dict(message)['from']['id'] == 777000:
        reply_to_message_id = message.message_id
        transaction_api_id = message.text.split('Номер: ')[1].split('\n')[0]
        actions.update_thread_id(transaction_api_id, reply_to_message_id)
        url = f"https://api.telegram.org/bot{secrets.secret_info.TELEGRAM_API_TOKEN}/sendMessage"
        params = {
            "chat_id": {message.chat.id},
            "text": messages.SEND_CONFIRMATION_SENT_PHOTO,
            "reply_to_message_id": message.message_id
        }
        requests.post(url, params=params)

@dp.message_handler(content_types=['photo'])
async def photo_handler(message):
    print(message.message_thread_id)

    filename = 'db/files/' + await get_random_name() + '.jpg'
    await message.photo[-1].download(filename)
    actions.update_admin_photo(message.message_thread_id, filename)

