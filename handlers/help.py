from aiogram import types
from config import ADMIN_ID
from aiogram.enums import ParseMode
from function.add_user import add_user
from function.get_users import get_users
from lang.texts import HELP_FOR_USER, HELP_FOR_ADMIN


async def cmd_help(message: types.Message):
    try:
        user_id = message.from_user.id
        if user_id not in ADMIN_ID:
            users = await get_users()
            if user_id not in users:
                await add_user(user_id)

            await message.answer(HELP_FOR_USER, parse_mode=ParseMode.HTML)
        else:
            await message.answer(HELP_FOR_ADMIN, parse_mode=ParseMode.HTML)
    except Exception as e:
        await message.answer('Что-то пошло не так...')
        print(f'Ошибка команды /help: {e}')
