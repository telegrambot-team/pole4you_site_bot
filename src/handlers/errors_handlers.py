import sys
import traceback
import typing

import aiogram

if typing.TYPE_CHECKING:
    from aiogram.types.error_event import ErrorEvent

import logging

from aiogram import Router

router = Router()


@router.errors()
async def error_handler(exception: 'ErrorEvent', bot: aiogram.Bot):
    print("Handled exception:", exception)
    logging.exception(exception.update)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_msg = ' - '.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    while exc_msg:
        block = exc_msg[:500]
        await bot.send_message(99988303, block)
        exc_msg = exc_msg[500:]
    return True
