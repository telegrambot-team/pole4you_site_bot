import logging

from aiogram import Bot, Dispatcher

from deta_state_srorage import DetaStateStorage
from handlers.basic_handlers import router as basic_router
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

    dispatcher.message.middleware.register(LoggingMiddleware())
    dispatcher.callback_query.middleware.register(LoggingMiddleware())

    dispatcher.include_router(basic_router)

    return dispatcher, bot


def main():
    dispatcher, bot = setup_dispatcher()
    dispatcher.run_polling(bot)


if __name__ == '__main__':
    main()
