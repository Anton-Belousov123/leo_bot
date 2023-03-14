import requests
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot import bot, dp
from db import actions
from handlers import private
from misc import messages, secrets

provider_group_id = -1001688280431
provider_channel_id = -1001815435429


@dp.callback_query_handler(lambda d: 'accept' in d.data)
async def update_post(data):
    user_to_send = dict(data)['from']['id']
    index = data.data.split('_')[1]
    await data.answer(messages.ACCEPTED)
    await data.message.edit_text(
        text=f"{actions.get_obj_by_id(int(index))}")
    await private.send_receipt_here(user_to_send, index)


