from aiogram.utils.executor import start_webhook
import handlers
import config
import tg_api


async def on_startup(dp):
    await tg_api.bot.set_webhook(config.WEBHOOK_URL)


async def on_shutdown(dp):
    await tg_api.bot.delete_webhook()


if __name__ == '__main__':
    start_webhook(
        dispatcher=tg_api.dp,
        webhook_path=config.WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT
    )
