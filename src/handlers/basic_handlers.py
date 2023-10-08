import base64
import binascii
import logging

from aiogram import Bot, F, Router, types
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from settings import Settings
from tables.reply_map_table import ReplyMapTable

router = Router()


@router.message(Command(commands=["start"]))
async def start_handler(message: types.Message, state: FSMContext, command: CommandObject):
    await state.set_data({
        "id": message.from_user.id,
        "name": message.from_user.full_name,
        "username": message.from_user.username,
    })
    await message.answer("Вас приветствует команда поддержки pole4you!\n"
                         "Напишите нам, и мы обязательно решим ваш вопрос!",
                         )

    logging.info(f"{command.args=}")

    if command.args is not None:
        try:
            decoded = base64.b64decode(command.args)
            from_page = decoded.decode("utf-8")
            logging.info(f"{from_page=}")
            await state.update_data(from_page=from_page)
        except binascii.Error:
            logging.warning("Couldn't decode string")


@router.message(F.chat.id == Settings().support_chat_id, F.reply_to_message)
async def support_message_handler(message: types.Message, reply_map: ReplyMapTable, bot: Bot):
    initial_msg_id = message.reply_to_message.message_id
    reply_data = reply_map.get(initial_msg_id)
    await bot.send_message(reply_data.original_chat_id, message.text, reply_to_message_id=reply_data.original_msg_id)


@router.message(F.text)
async def user_message_handler(message: types.Message, state: FSMContext, bot: Bot, reply_map: ReplyMapTable):
    data = await state.get_data()
    support_chat = Settings().support_chat_id
    if 'from_page' in data:
        await bot.send_message(support_chat, f"Страница:\n{data['from_page']}")
        del data['from_page']

    forwarded_msg = await message.forward(support_chat)
    reply_map.save(original_chat_id=message.from_user.id,
                   forwarded_msg_id=forwarded_msg.message_id,
                   original_msg_id=message.message_id)
    await message.answer("Наша служба поддержки ответит вам в ближайшее время!")
