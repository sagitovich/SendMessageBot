from aiogram import types
from config import ADMIN_ID
from function.add_user import add_user
from function.get_users import get_users


async def cmd_start(message: types.Message):
    try:
        user_id = message.from_user.id
        if user_id in ADMIN_ID:
            await message.answer(f'Вы администратор!')
        else:
            users = await get_users()
            if user_id not in users:
                await add_user(user_id)

        await message.delete()
        await message.answer(f'Добро пожаловать!')
    except Exception as e:
        await message.answer('Что-то пошло не так...')
        print(f'Ошибка команды /start: {e}')
