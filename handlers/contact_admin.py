import asyncio
from aiogram import types
from config import ADMIN_ID
from aiogram.enums import ParseMode
from function.add_user import add_user
from function.get_users import get_users


async def cmd_contact_admin(message: types.Message):
    try:
        user_id = message.from_user.id
        if user_id not in ADMIN_ID:
            users = await get_users()
            if user_id not in users:
                await add_user(user_id)

        lines = message.caption.split('\n') if message.caption else message.text.split('\n')
        msg_to_admin = "\n".join(lines[1:]).strip()
        msg_to_admin += f'\nID пользователя: <code>{user_id}</code>'
        photo = message.photo[-1].file_id if message.photo else None

        for ID in ADMIN_ID:
            if photo:
                await message.bot.send_photo(chat_id=ID, photo=photo, caption=msg_to_admin, parse_mode=ParseMode.HTML)
                await asyncio.sleep(0.5)
            else:
                await message.bot.send_message(chat_id=ID, text=msg_to_admin, parse_mode=ParseMode.HTML)
                await asyncio.sleep(0.5)

        await message.answer(f'Ваше сообщение отправлено администратору!\n'
                             f'Ожидайте ответ...')

    except Exception as e:
        await message.answer('Что-то пошло не так...')
        print(f'Ошибка команды /to_admin: {e}')
