from contextlib import suppress

import aiogram.exceptions
from aiogram import Bot, Router, types
from aiogram.filters import Command, Filter
from settings import Settings

router = Router()


class IsAdmin(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id == Settings().admin_id


router.message.filter(IsAdmin())


@router.message(Command(commands=["chat_id"]))
async def chat_id_handler(message: types.Message, bot: Bot):
    with suppress(aiogram.exceptions.TelegramBadRequest):
        await message.delete()

    await bot.send_message(message.from_user.id, f"Chat id: {message.chat.id}")
