import logging

from aiogram import Bot, Dispatcher

from handlers.basic_handlers import router as basic_router
from settings import Settings


def main():
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
    dispatcher = Dispatcher()
    dispatcher.include_router(basic_router)

    dispatcher.run_polling(bot)


if __name__ == '__main__':
    main()
