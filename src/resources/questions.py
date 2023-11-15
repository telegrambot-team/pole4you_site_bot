from pydantic import BaseModel, ConfigDict


class Answer(BaseModel):
    model_config = ConfigDict(frozen=True)

    question_number: int
    answer_text: str
    answer_code: int


class Question(BaseModel):
    model_config = ConfigDict(frozen=True)
    question_number: int
    question_text: str
    answers: list[Answer]


questions = [
    Question(question_number=1,
             question_text="Где Вы хотите поставить пилон?",
             answers=[
                 Answer(question_number=1, answer_text="Дома", answer_code=1),
                 Answer(question_number=1, answer_text="Студия танцев", answer_code=2),
                 Answer(question_number=1, answer_text="Фитнес центр", answer_code=3),
                 Answer(question_number=1, answer_text="Сцена", answer_code=4),
                 Answer(question_number=1, answer_text="Улица", answer_code=5),
                 Answer(question_number=1, answer_text="Клуб", answer_code=6),
                 Answer(question_number=1, answer_text="Другое", answer_code=7),
             ]),
    Question(question_number=2,
             question_text="Какой потолок в помещении?",
             answers=[
                 Answer(question_number=2, answer_text="Бетон", answer_code=1),
                 Answer(question_number=2, answer_text="Натяжной потолок", answer_code=2),
                 Answer(question_number=2, answer_text="Гипрок (ГВЛ, ФАНЕРА, ДСП и пр.)", answer_code=3),
                 Answer(question_number=2, answer_text="Подвесной (плитка, грильато)", answer_code=4),
                 Answer(question_number=2, answer_text="Деревянный", answer_code=5),
                 Answer(question_number=2, answer_text="Нет потолка", answer_code=6),
                 Answer(question_number=2, answer_text="Другое", answer_code=7),
                 Answer(question_number=2, answer_text="Пропустить", answer_code=8),
             ]),
    Question(question_number=3,
             question_text="Какой высоты необходим пилон? (высота помещения)",
             answers=[
                 Answer(question_number=3, answer_text="до 2,8 м.", answer_code=1),
                 Answer(question_number=3, answer_text="от 2,8 до 3,3 м.", answer_code=2),
                 Answer(question_number=3, answer_text="от 3,3 до 3,8 м.", answer_code=3),
                 Answer(question_number=3, answer_text="от 3,8 до 4 м.", answer_code=4),
                 Answer(question_number=3, answer_text="от 4 до 4,5 м.", answer_code=5),
                 Answer(question_number=3, answer_text="от 4,5 до 5 м.", answer_code=6),
                 Answer(question_number=3, answer_text="более 5 м.", answer_code=7),
             ]),
    Question(question_number=4,
             question_text="Кужна ли функция вращения / блокировки?",
             answers=[
                 Answer(question_number=4, answer_text="Да, нужна", answer_code=1),
                 Answer(question_number=4, answer_text="Нет, пускай пилон будет статичный", answer_code=2),
             ]),
    Question(question_number=5,
             question_text="Можно ли сделать отверстие в потолке?",
             answers=[
                 Answer(question_number=5, answer_text="Да", answer_code=1),
                 Answer(question_number=5, answer_text="Не хотелось бы, но если это необходимо для безопасности, то скорее да",
                        answer_code=2),
                 Answer(question_number=5, answer_text="Нет", answer_code=3),
             ]),
    Question(question_number=6,
             question_text="Можно ли сверлить пол?",
             answers=[
                 Answer(question_number=6, answer_text="Можно врезать опору в пол", answer_code=1),
                 Answer(question_number=6, answer_text="Можно сделать только отверстия в полу", answer_code=2),
                 Answer(question_number=6, answer_text="Не хотелось бы, но если это необходимо для безопасности, то скорее да",
                        answer_code=3),
                 Answer(question_number=6, answer_text="Нет", answer_code=4),
             ]),
    Question(question_number=7,
             question_text="Как часто вы планируете снимать пилон?",
             answers=[
                 Answer(question_number=7, answer_text="Не планирую", answer_code=1),
                 Answer(question_number=7, answer_text="Редко, не более раза в месяц", answer_code=2),
                 Answer(question_number=7, answer_text="Почти каждый день", answer_code=3),
                 Answer(question_number=7, answer_text="Более одного раза в день и снятие должно быть простым, без стремянки",
                        answer_code=4),
                 Answer(question_number=7, answer_text="Пилон будет переезжать в разные помещения", answer_code=5),
             ]),
    Question(question_number=8,
             question_text="Какая высота от натяжного (подвесного) потолка до основного "
                           "(бетонного или др, в который можно закрепить пилон)",
             answers=[
                 Answer(question_number=8, answer_text="до 8 см.", answer_code=1),
                 Answer(question_number=8, answer_text="от 8 до 15 см.", answer_code=2),
                 Answer(question_number=8, answer_text="от 15 до 30 см.", answer_code=3),
                 Answer(question_number=8, answer_text="более 30 см.", answer_code=4),
                 Answer(question_number=8, answer_text="Пропустить", answer_code=5),
             ]),
    Question(question_number=9,
             question_text="Выберите вариант по Вашим потребностям",
             answers=[
                 Answer(question_number=9,
                        answer_text="LITE - обычная полировка трубы, опоры черного цвета, без запаса по нагрузке,"
                                    " более простая комплектация",
                        answer_code=1),
                 Answer(question_number=9,
                        answer_text="PRO - профессиональная полировка трубы, блестящие опоры в цвет трубы, крепления"
                                    " рассчитанные на повышенные, профессиональные нагрузки, все функции и комплектация",
                        answer_code=2),
             ],
             ),
]
