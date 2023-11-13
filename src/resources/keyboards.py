from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from resources.questions import questions


def create_answer_keyboard(question_index: int) -> InlineKeyboardMarkup:
    buttons = []
    for answer in questions[question_index].answers:
        button = [InlineKeyboardButton(text=answer.answer_text, callback_data=f'answer:{question_index}:{str(answer.answer_code)}')]
        buttons.append(button)
    kbrd = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kbrd


question_number = 1  # Номер вопроса
keyboard = create_answer_keyboard(question_number)
