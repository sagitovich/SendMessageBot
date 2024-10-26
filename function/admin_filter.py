from __future__ import annotations

from config import ADMIN_ID
from aiogram.types import Message
from aiogram.filters import BaseFilter


class AdminFilter(BaseFilter):
    def __init__(self, is_admin: bool = True):
        self.is_admin = is_admin

    async def __call__(self,  message: Message) -> bool:
        user_id = message.from_user.id
        return user_id in ADMIN_ID
