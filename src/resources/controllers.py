from typing import Optional

from aiogram import types
from aiogram.fsm.context import FSMContext

from resources.keyboards import create_answer_keyboard
from src.resources.questions import questions


def determine_next_question_index(code: str) -> Optional[int]:
    for i, digit in enumerate(code):
        if digit == '0':
            return i
    return None


async def survey_routine(question_index: int, message: types.message.Message, state: FSMContext) -> None:
    if question_index is None or question_index >= len(questions):
        data = await state.get_data()
        await message.answer(f"Конец опроса, ваш код: {data['survey_code']}")

    await message.answer(f" {questions[question_index].question_text}", reply_markup=create_answer_keyboard(question_index))

