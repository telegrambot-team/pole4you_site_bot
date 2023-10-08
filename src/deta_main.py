from fastapi import FastAPI
from main import setup_dispatcher
from settings import Settings


def get_webhook_path(conf):
    return f"/bot/{conf.bot_token.get_secret_value()}"


def get_webhook_url(conf, webhook_path):
    return conf.deta_space_app_hostname + webhook_path


def setup_app():
    fastapi_app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

    sett = Settings()

    webhook_path = get_webhook_path(sett)
    webhook_url = get_webhook_url(sett, webhook_path)

    dispatcher, bot = setup_dispatcher()

    @fastapi_app.post(webhook_path)
    async def bot_webhook(update: dict):
        res = await dispatcher.feed_webhook_update(bot, update)
        return res

    @fastapi_app.get("/bot/update_webhook")
    async def setup():
        await bot.set_webhook(url=webhook_url, drop_pending_updates=True,
                              secret_token=sett.webhook_secret_token.get_secret_value())
        return "Updated"

    return fastapi_app


app = setup_app()
