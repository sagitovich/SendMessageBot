from aiogram import types


async def cmd_answer(message: types.Message):
    try:
        lines = message.caption.split('\n') if message.caption else message.text.split('\n')
        user = int(lines[1].strip())
        msg_to_all = "\n".join(lines[2:]).strip()
        photo = message.photo[-1].file_id if message.photo else None

        if photo:
            await message.bot.send_photo(chat_id=user, photo=photo, caption=msg_to_all)
        else:
            await message.bot.send_message(chat_id=user, text=msg_to_all)

        await message.answer(f'Ответ отправлен пользователю {user}!')
    except Exception as e:
        await message.answer('Что-то пошло не так...')
        print(f'Ошибка команды /to_all: {e}')
