from .help import cmd_help
from .start import cmd_start
from .send_to_all import cmd_mailing
from .answer_to_user import cmd_answer
from .contact_admin import cmd_contact_admin
from function.admin_filter import AdminFilter
from aiogram.filters import Command


def register_commands(dp):
    dp.message.register(cmd_start, Command(commands=['start']))
    dp.message.register(cmd_help, Command(commands=['help']))
    dp.message.register(cmd_contact_admin, lambda message: message.text and message.text.startswith('/to_admin\n')
                                                            or message.caption)

    dp.message.register(cmd_mailing, lambda message: (message.text and message.text.startswith('/to_all\n'))
                                                     or message.caption, AdminFilter())
    dp.message.register(cmd_answer, lambda message: (message.text and message.text.startswith('/to_user\n'))
                                                     or message.caption, AdminFilter())
