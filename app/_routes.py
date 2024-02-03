from fastapi import APIRouter
from telegram import Update

from app.telegram_app.constants import UpdateSchema
from app.telegram_app.main import ptb
from app.settings import settings

PREFIX = "/telegram"
WEBHOOK_ENDPOINT = settings.WEBHOOK_ENDPOINT.replace(PREFIX, "")
router = APIRouter()

@router.post(WEBHOOK_ENDPOINT)
async def process_update_post(request: UpdateSchema):
    req = request.model_dump()
    update = Update.de_json(req, ptb.bot)
    await ptb.process_update(update)
    return {"status": "ok"}

router.get(WEBHOOK_ENDPOINT)
async def process_update_get(request: UpdateSchema):
    req = request.model_dump()
    update = Update.de_json(req, ptb.bot)
    await ptb.process_update(update)
    return {"status": "ok"}
