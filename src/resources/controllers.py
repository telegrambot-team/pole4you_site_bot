from typing import Optional

from aiogram import types
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext

from resources.answer import result, text
from resources.keyboards import get_answer_keyboard, get_answer_keyboard_without_roof
from src.resources.questions import questions


def get_answer(code: str) -> str:
    final_answer = code[1:].replace('-', '0')
    return result.get(final_answer, text)


def determine_next_question_index(code: str) -> Optional[int]:
    for i, digit in enumerate(code):
        if digit == '0':
            return i
    return None


async def survey_routine(question_index: int, message: types.message.Message, state: FSMContext) -> None:
    data = await state.get_data()
    try:
        if question_index is None or question_index >= len(questions):
            await message.edit_text(f"Конец опроса. Ваш код: {data['survey_code'][1:].replace('-', '0')}.\n\n"
                                    f"<b>{get_answer(data['survey_code'])}</b>")
            await state.update_data(survey_code=data['survey_code'])
            return

        elif question_index == 1 and data['survey_code'][0] == '1':
            await message.edit_text(f"{questions[question_index].question_text}",
                                    reply_markup=get_answer_keyboard_without_roof(question_index))
        elif question_index == 1 and data['survey_code'][0] == '5':
            data['survey_code'] = data['survey_code'][:1] + '-' + data['survey_code'][2:]
            await state.update_data(survey_code=data['survey_code'])
            await message.edit_text(f"{questions[question_index + 1].question_text}",
                                    reply_markup=get_answer_keyboard(question_index + 1))

        elif question_index == 4 and data['survey_code'][1] == '6':
            data['survey_code'] = data['survey_code'][:4] + '-' + data['survey_code'][5:]
            await state.update_data(survey_code=data['survey_code'])
            await message.edit_text(f"{questions[question_index + 1].question_text}",
                                    reply_markup=get_answer_keyboard(question_index + 1))
        elif question_index == 4 and data['survey_code'][0] == '5':
            data['survey_code'] = data['survey_code'][:4] + '-' + data['survey_code'][5:]
            await state.update_data(survey_code=data['survey_code'])
            await message.edit_text(f"{questions[question_index + 1].question_text}",
                                    reply_markup=get_answer_keyboard(question_index + 1))

        elif question_index == 7 and data['survey_code'][0] == '5':
            data['survey_code'] = data['survey_code'][:7] + '-' + data['survey_code'][8:]
            await state.update_data(survey_code=data['survey_code'])
            await message.edit_text(f"{questions[question_index + 1].question_text}",
                                    reply_markup=get_answer_keyboard(question_index + 1))
        elif question_index == 7 and data['survey_code'][1] == '6':
            data['survey_code'] = data['survey_code'][:7] + '--'
            await state.update_data(survey_code=data['survey_code'])
            await message.edit_text(f"Конец опроса. Ваш код: {data['survey_code'][1:].replace('-', '0')}.\n\n"
                                    f"<b>{get_answer(data['survey_code'])}</b>")

        elif question_index == 7 and data['survey_code'][0] == '7':
            data['survey_code'] = data['survey_code'][:7] + '--'
            await state.update_data(survey_code=data['survey_code'])
            await message.edit_text(f"Конец опроса. Ваш код: {data['survey_code'][1:].replace('-', '0')}.\n\n"
                                    f"<b>{get_answer(data['survey_code'])}</b>")
            await state.update_data(survey_code=data['survey_code'])
        elif question_index == 7 and data['survey_code'][1] in '12345789':
            data['survey_code'] = data['survey_code'][:7] + '-' + data['survey_code'][8:]
            await state.update_data(survey_code=data['survey_code'])
            await message.edit_text(f"{questions[question_index + 1].question_text}",
                                    reply_markup=get_answer_keyboard(question_index + 1))
        else:
            await message.edit_text(f"{questions[question_index].question_text}", reply_markup=get_answer_keyboard(question_index))
    except TelegramBadRequest:
        if question_index is None or question_index >= len(questions):
            await message.answer(f"Конец опроса. Ваш код: {data['survey_code'][1:].replace('-', '0')}.\n\n"
                                 f"<b>{get_answer(data['survey_code'])}</b>")
            await state.update_data(survey_code=data['survey_code'])
            return
        else:
            await message.answer(f"{questions[question_index].question_text}", reply_markup=get_answer_keyboard(question_index))
