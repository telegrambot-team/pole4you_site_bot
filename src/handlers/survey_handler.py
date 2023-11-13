from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from resources.controllers import determine_next_question_index, survey_routine


router = Router()


@router.message(F.text == "Пройти опрос")
async def survey_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    a = determine_next_question_index(data['survey_code'])
    await survey_routine(a, message, state)


@router.callback_query(F.data.startswith('answer:'))
async def answer_handler(callback: types.CallbackQuery, state: FSMContext):
    question_index = int(callback.data.split(':')[1])
    answer_code = int(callback.data.split(':')[2])
    # new_survey_code = determine_next_question_index(callback.data.split(':')[1])
    data = await state.get_data()
    new_survey_code = data['survey_code'][:question_index] + str(answer_code) + data['survey_code'][question_index + 1:]
    print(new_survey_code)
    await state.update_data(survey_code=new_survey_code)
    a = determine_next_question_index(new_survey_code)
    await survey_routine(a, callback.message, state)
