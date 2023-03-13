from random import randint

from bot import dp, bot
from misc.states import Report


async def get_random_name():
    s = ''
    for i in range(16):
        s = s + str(randint(0, 9))
    return s


@dp.callback_query_handler(lambda d: 'sended' in d.data)
async def sended_handler(data):
    index = data.data.split("_")[1]
    await data.answer("Отлично!")
    message = await data.message.edit_text(
        text="Прикрепите подтверждение")
    await Report.set_file.set()



@dp.message_handler(state=Report.set_file, content_types=['photo'])
async def validate_photo(message, state):
    if 'photo' in dict(message).keys():
        filename = 'db/files/' + await get_random_name() + '.jpg'
        await message.photo[-1].download(filename)
    await state.finish()
    await message.answer("Ожидайте ответа пользователя!")


async def user_approve_report():
    bot.send_message("Пользователь подтвердил получение ДС")
