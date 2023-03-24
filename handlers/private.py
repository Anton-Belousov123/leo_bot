from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot import dp, bot
from db import actions
from misc import messages
from misc.states import Report
from misc.utils import get_random_name


def get_sent_keyboard(index: int):
    return InlineKeyboardMarkup(resize_keyboard=True).add(
        InlineKeyboardButton(messages.SENT, callback_data=f"sent_{index}"))


async def send_receipt_here(user_id, index):
    print(user_id, index)
    await bot.send_message(user_id, actions.get_obj_by_id_to_private(index), reply_markup=get_sent_keyboard(index))


@dp.callback_query_handler(lambda d: 'sent' in d.data)
async def sent_handler(data):
    index = data.data.split("_")[1]
    await data.answer(messages.GOOD)
    await data.message.edit_text(
        text=messages.SEND_CONFIRMATION_PHOTO)
    actions.set_private_user_id(data.message.chat.id, int(index))
    await Report.set_file.set()


@dp.message_handler(state=Report.set_file, content_types=['photo'])
async def validate_photo(message, state):
    filename = 'db/files/' + await get_random_name() + '.jpg'
    await message.photo[-1].download(filename)
    await state.finish()
    actions.set_private_photo(filename, message.chat.id)
    await message.answer(messages.WAIT_USER_CALLBACK)


async def user_approve_report():
    bot.send_message(messages.USER_APPROVED_DC)

