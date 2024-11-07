import base64
import binascii
import json
import logging

from aiogram import Bot, F, Router, types
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from redis.asyncio.client import Redis

from settings import Settings

router = Router()


@router.message(Command(commands=["start"]))
async def start_handler(message: types.Message, state: FSMContext, command: CommandObject):
    await state.set_data({
        "id": message.from_user.id,
        "name": message.from_user.full_name,
        "username": message.from_user.username,
        "survey_code": '000000000',
    })
    await message.answer("Вас приветствует команда поддержки pole4you!\n"
                         "Напишите нам, и мы обязательно решим ваш вопрос!",)
                         # reply_markup=types.ReplyKeyboardMarkup(is_persistent=True,
                         #                                        resize_keyboard=True,
                         #                                        keyboard=[
                         #                                            [types.KeyboardButton(text="Пройти опрос")]]), ),

    logging.info(f"{command.args=}")

    if command.args is not None:
        try:
            decoded = base64.b64decode(command.args)
            from_page = decoded.decode("utf-8")
            logging.info(f"{from_page=}")
            await state.update_data(from_page=from_page)
        except binascii.Error:
            logging.warning("Couldn't decode string")


def parse_redis_dict(value) -> dict[str, int]:
    if value is None:
        return {}
    if isinstance(value, bytes):
        value = value.decode("utf-8")
    return json.loads(value)


@router.message(F.chat.id == Settings().support_chat_id, F.reply_to_message)
async def support_message_handler(message: types.Message, bot: Bot, redis: Redis):
    initial_msg_id = message.reply_to_message.message_id
    redis_data = await redis.get(str(initial_msg_id))
    parsed_data = parse_redis_dict(redis_data)
    await bot.send_message(parsed_data['original_chat_id'], message.text,
                           reply_to_message_id=parsed_data['original_msg_id'])


@router.message(F.text)
async def user_message_handler(message: types.Message, state: FSMContext, bot: Bot, redis: Redis):
    data = await state.get_data()
    support_chat = Settings().support_chat_id
    if 'from_page' in data:
        await bot.send_message(support_chat, f"Страница:\n{data['from_page']}")
        del data['from_page']

    forwarded_msg = await message.forward(support_chat)
    reply_data = {
        'original_chat_id': message.from_user.id,
        'original_msg_id': message.message_id
    }

    await redis.set(
        str(forwarded_msg.message_id),
        json.dumps(reply_data))

    await message.answer("Наша служба поддержки ответит вам в ближайшее время!")
