import asyncio
from aiogram import types
from function.get_users import get_users


async def cmd_mailing(message: types.Message):
    try:
        msg_to_all = message.caption[len('/to_all\n'):].strip() if message.caption \
                                                                    else message.text[len('/to_all\n'):].strip()
        photo = message.photo[-1].file_id if message.photo else None
        users = await get_users()

        for user in users:
            if photo:
                await message.bot.send_photo(chat_id=user, photo=photo, caption=msg_to_all)
            else:
                await message.bot.send_message(chat_id=user, text=msg_to_all)
            await asyncio.sleep(0.5)

        await message.answer('Рассылка сообщений завершена!')
    except Exception as e:
        await message.answer('Что-то пошло не так...')
        print(f'Ошибка команды /to_all: {e}')
