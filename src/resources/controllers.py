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
    data = await state.get_data()
    if question_index is None or question_index >= len(questions):
        await message.answer(f"Конец опроса, ваш код: {data['survey_code']}")
    elif question_index == 4 and data['survey_code'][1] == '6':
        data['survey_code'] = data['survey_code'][:4] + '-' + data['survey_code'][5:]
        await message.answer(f"{questions[question_index + 1].question_text}", reply_markup=create_answer_keyboard(question_index + 1))

    await message.answer(f"{questions[question_index].question_text}", reply_markup=create_answer_keyboard(question_index))

