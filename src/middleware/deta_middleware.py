
from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from deta import Deta

from tables.reply_map_table import ReplyMapTable


class DetaMiddleware(BaseMiddleware):
    def __init__(self, deta_project_key: str):
        self.deta = Deta(deta_project_key)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        data['reply_map'] = ReplyMapTable(self.deta.Base('reply_map'))
        return await handler(event, data)
