import logging

from aiogram import Bot, Dispatcher
from deta_state_srorage import DetaStateStorage
from handlers.admin_handlers import router as admin_router
from handlers.basic_handlers import router as basic_router
from handlers.errors_handlers import router as error_router
from handlers.survey_handler import router as survey_router
from middleware.deta_middleware import DetaMiddleware
from middleware.logging_middleware import LoggingMiddleware
from middleware.upd_dumper_middleware import UpdatesDumperMiddleware
from settings import Settings


def setup_dispatcher():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s: "
               "%(filename)s: "
               "%(levelname)s: "
               "%(funcName)s(): "
               "%(lineno)d:\t"
               "%(message)s",
    )

    logging.info("Application started")

    sett = Settings()

    bot = Bot(token=sett.bot_token.get_secret_value())

    storage = DetaStateStorage(sett.deta_project_key.get_secret_value())
    dispatcher = Dispatcher(storage=storage)

    dispatcher.update.outer_middleware(UpdatesDumperMiddleware(sett.deta_project_key.get_secret_value()))

    deta_mid = DetaMiddleware(sett.deta_project_key.get_secret_value())
    dispatcher.message.middleware.register(deta_mid)
    dispatcher.callback_query.middleware.register(deta_mid)

    dispatcher.message.middleware.register(LoggingMiddleware())
    dispatcher.callback_query.middleware.register(LoggingMiddleware())

    dispatcher.include_router(admin_router)
    dispatcher.include_router(basic_router)
    dispatcher.include_router(survey_router)
    dispatcher.include_router(error_router)

    return dispatcher, bot


def main():
    dispatcher, bot = setup_dispatcher()
    dispatcher.run_polling(bot)


if __name__ == '__main__':
    main()
