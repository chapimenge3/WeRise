import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.settings import settings
from app.telegram_app.main import ptb

logger = logging.getLogger('fastapi')

@asynccontextmanager
async def lifespan(_: FastAPI):
    webhook_endpoint = f"{settings.BACKEND_URL}{settings.WEBHOOK_ENDPOINT}"
    await ptb.bot.setWebhook(webhook_endpoint)
    # async with ptb:
    await ptb.initialize()
    await ptb.start()
    yield
    await ptb.stop()
    