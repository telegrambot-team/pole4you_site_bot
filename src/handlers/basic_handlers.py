from aiogram import Router, types
from aiogram.filters import Command
from controllers.basic_controllers import produce_hello_answer

router = Router()


@router.message(Command(commands=["start"]))
async def start_handler(message: types.Message):
    answer_text = produce_hello_answer(message.from_user.full_name)
    await message.answer(answer_text)
