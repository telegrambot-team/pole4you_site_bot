import logging.config
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from handlers.admin_handlers import router as admin_router
from handlers.basic_handlers import router as basic_router
from handlers.errors_handlers import router as error_router
from handlers.survey_handler import router as survey_router
from logging_setup import get_logging_config
from middleware.logging_middleware import LoggingMiddleware
from middleware.upd_dumper_middleware import UpdatesDumperMiddleware
from settings import Settings


def setup_dispatcher():
    logs_directory = Path("logs")
    logs_directory.mkdir(parents=True, exist_ok=True)
    logging_config = get_logging_config(__name__)
    logging.config.dictConfig(logging_config)

    logging.info("Application started")

    sett = Settings()

    bot = Bot(token=sett.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    storage = RedisStorage.from_url(sett.redis_url.unicode_string())
    dispatcher = Dispatcher(storage=storage, redis=storage.redis, settings=sett)

    dispatcher.update.outer_middleware(UpdatesDumperMiddleware())

    dispatcher.message.middleware.register(LoggingMiddleware())
    dispatcher.callback_query.middleware.register(LoggingMiddleware())

    dispatcher.include_router(admin_router)
    dispatcher.include_router(survey_router)
    dispatcher.include_router(basic_router)
    dispatcher.include_router(error_router)

    return dispatcher, bot


def main():
    dispatcher, bot = setup_dispatcher()
    dispatcher.run_polling(bot)


if __name__ == '__main__':
    main()
