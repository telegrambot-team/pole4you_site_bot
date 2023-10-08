from pydantic import BaseModel, ConfigDict


class Answer(BaseModel):
    model_config = ConfigDict(frozen=True)

    answer_text: str
    next_question: int


class Question(BaseModel):
    model_config = ConfigDict(frozen=True)

    question_text: str
    answers: list[Answer]


questions = [
    Question(question_text="Где Вы хотите поставить пилон?",
             answers=[
                 Answer(answer_text="Дома", next_question=2),
                 Answer(answer_text="Студия танцев", next_question=2),
                 Answer(answer_text="Фитнес центр", next_question=2),
                 Answer(answer_text="Сцена", next_question=2),
                 Answer(answer_text="Улица", next_question=2),
                 Answer(answer_text="Клуб", next_question=2),
                 Answer(answer_text="Другое *", next_question=2),
             ]),
    Question(question_text="Какой потолок в помещении?",
             answers=[
                 Answer(answer_text="Бетон", next_question=2),
                 Answer(answer_text="Натяжной потолок", next_question=2),
                 Answer(answer_text="Гипрок (ГВЛ, ФАНЕРА, ДСП и пр.)", next_question=2),
                 Answer(answer_text="Подвесной (плитка, грильато)", next_question=2),
                 Answer(answer_text="Деревянный", next_question=2),
                 Answer(answer_text="Нет потолка", next_question=3),
                 Answer(answer_text="Другое", next_question=2),
                 Answer(answer_text="Пропустить	", next_question=3),
             ]),
    Question(question_text="Какой высоты необходим пилон? (высота помещения)",
             answers=[
                 Answer(answer_text="до 2,8 м.", next_question=4),
                 Answer(answer_text="от 2,8 до 3,3 м.", next_question=4),
                 Answer(answer_text="от 3,3 до 3,8 м.", next_question=4),
                 Answer(answer_text="от 3,8 до 4 м.", next_question=4),
                 Answer(answer_text="от 4 до 4,5 м.", next_question=4),
                 Answer(answer_text="от 4,5 до 5 м.", next_question=4),
                 Answer(answer_text="более 5 м.", next_question=4),
             ]),
    Question(question_text="Кужна ли функция вращения / блокировки?",
             answers=[
                 Answer(answer_text="Да, нужна", next_question=5),
                 Answer(answer_text="Нет, пускай пилон будет статичный", next_question=5),
             ]),
    Question(question_text="Можно ли сделать отверстие в потолке?",
             answers=[
                 Answer(answer_text="Да", next_question=6),
                 Answer(answer_text="Не хотелось бы, но если это необходимо для безопасности, то скорее да",
                        next_question=6),
                 Answer(answer_text="Нет", next_question=6),
             ]),
    Question(question_text="Можно ли сверлить пол?",
             answer=[
                 Answer(answer_text="Да", next_question=7),
                 Answer(answer_text="Не хотелось бы, но если это необходимо для безопасности, то скорее да",
                        next_question=7),
                 Answer(answer_text="Нет", next_question=7),
             ]),
    Question(question_text="Как часто вы планируете снимать пилон?",
             answer=[
                 Answer(answer_text="Не планирую", next_question=8),
                 Answer(answer_text="Редко, не более раза в месяц", next_question=8),
                 Answer(answer_text="Почти каждый день", next_question=8),
                 Answer(answer_text="Более одного раза в день и снятие должно быть простым, без стремянки",
                        next_question=8),
                 Answer(answer_text="Пилон будет переезжать в разные помещения", next_question=8),
             ]),
    Question(
        question_text="Какая высота от натяжного (подвесного) потолка до основного (бетонного или др, в который можно закрепить пилон)",
        answer=[
            Answer(answer_text="до 8 см.", next_question=9),
            Answer(answer_text="от 8 до 15 см.", next_question=9),
            Answer(answer_text="от 15 до 30 см.", next_question=9),
            Answer(answer_text="более 30 см.", next_question=9),
            Answer(answer_text="Пропустить", next_question=9),
        ]),
    Question(
        question_text="Выберите вариант по Вашим потребностям",
        answer=[
            Answer(
                answer_text="LITE - обычная полировка трубы, опоры черного цвета, без запаса по нагрузке, более простая комплектация",
                next_question=10),
            Answer(
                answer_text="PRO - профессиональная полировка трубы, блестящие опоры в цвет трубы, крепления рассчитанные на повышенные, профессиональные нагрузки, все функции и комплектация",
                next_question=10),
        ]
    )
]
