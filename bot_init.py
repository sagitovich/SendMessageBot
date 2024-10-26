from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from handlers import register_commands
from aiogram.types import BotCommand, BotCommandScopeDefault

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
register_commands(dp)


async def start_bot():
    try:
        await bot.set_my_commands(
            commands=[
                BotCommand(command='/start', description='Запуск'),
                BotCommand(command='/help', description='Помощь')
            ],
            scope=BotCommandScopeDefault()
        )
        print('Бот запущен')
        await dp.start_polling(bot)
    except Exception as e:
        print(f'Ошибка запуска бота: {e}')
