from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from resources.questions import questions


def get_answer_keyboard(question_index: int) -> InlineKeyboardMarkup:
    buttons = []
    for answer in questions[question_index].answers:
        button = [InlineKeyboardButton(text=answer.answer_text, callback_data=f'answer:{question_index}:{str(answer.answer_code)}')]
        buttons.append(button)
    kbrd = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kbrd


def get_answer_keyboard_without_roof(question_index: int) -> InlineKeyboardMarkup:
    buttons = []
    for answer in questions[question_index].answers:
        button = [InlineKeyboardButton(text=answer.answer_text, callback_data=f'answer:{question_index}:{str(answer.answer_code)}')]
        buttons.append(button)
    buttons.remove(buttons[5])
    kbrd = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kbrd
