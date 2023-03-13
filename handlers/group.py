from aiogram import types

from bot import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers.messages import get_random_name
from misc.states import Approve

channel_id = -1001688280431


def get_post_keyboard(index: int):
    return InlineKeyboardMarkup(resize_keyboard=True).add(
        InlineKeyboardButton("Принять", callback_data=f"accept_{index}"))


def get_sended_keyboard(index: int):
    return InlineKeyboardMarkup(resize_keyboard=True).add(
        InlineKeyboardButton("Перевел", callback_data=f"sended_{index}"))


def get_approve_keyboard(index: int):
    return InlineKeyboardMarkup(resize_keyboard=True).add(
        InlineKeyboardButton("Подтвердить", callback_data=f"approve_{index}"))


async def create_post():
    message = await bot.send_message(channel_id,
                                     text="Тестовый пост",
                                     reply_markup=get_post_keyboard(1))
    print(message)


@dp.callback_query_handler(lambda d: 'accept' in d.data)
async def update_post(data):
    index = data.data.split('_')[1]
    await data.answer("Принято!")
    message = await data.message.edit_text(
        text="~зачеркнутый текст~",
        parse_mode='MarkdownV2')
    bot.send_message(message.from_user.id, "Отправьте перевод вод сюда", reply_markup=get_sended_keyboard(index))


async def user_approve_report_group():
    await bot.send_message(channel_id, "Подтвердить", reply_markup=get_approve_keyboard(1))


@dp.callback_query_handler(lambda d: 'approve_' in d.data)
async def approve_validation(data):
    index = data.data.split('_')[1]
    await data.answer("Согласовано!")
    await Approve.set_file.set()
    await bot.send_message(channel_id, "Необходимо прикрепить фото для согласования")


@dp.message_handler(state=Approve.set_file, content_types=['photo'])
async def validate_photo(message, state):
    if 'photo' in dict(message).keys():
        filename = 'db/files/' + await get_random_name() + '.jpg'
        await message.photo[-1].download(filename)
    await state.finish()
    await message.answer("Крипта переведена на счет!")
