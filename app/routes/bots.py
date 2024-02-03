from typing import Union

from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from telegram import Update
from pydantic import BaseModel

from app.telegram_app.constants import UpdateSchema
from app.telegram_app.main import ptb
from internal.dao.session import get_session, delete_session
from app.settings import settings

PREFIX = "/telegram"
WEBHOOK_ENDPOINT = settings.WEBHOOK_ENDPOINT.replace(PREFIX, "")
router = APIRouter()


class PassportDataSchema(BaseModel):
    token: Union[str, int]


@router.post(WEBHOOK_ENDPOINT)
async def process_update_post(request: UpdateSchema):
    req = request.model_dump()
    update = Update.de_json(req, ptb.bot)
    await ptb.process_update(update)
    return {"status": "ok"}


@router.get(WEBHOOK_ENDPOINT)
async def process_update_get(request: UpdateSchema):
    req = request.model_dump()
    update = Update.de_json(req, ptb.bot)
    await ptb.process_update(update)
    return {"status": "ok"}


@router.get("/verify/{token}")
async def verify(token: str):
    session = get_session(token=token)
    if not session:
        with open(f"{settings.BASE_DIR}/app/verification/unauthorized.html") as f:
            html = f.read()
        return HTMLResponse(html, status_code=401)
    with open(f"{settings.BASE_DIR}/app/verification/index.html") as f:
        html = f.read()

    return HTMLResponse(html)


@router.post("/passport-data")
async def get_passport_params(body: PassportDataSchema):
    data = {}

    # load public key
    # with open(f"{settings.BASE_DIR}/public.key", "r") as f:
    #     public_key = f.read()
    # data["public_key"] = public_key
    data["bot_id"] = ptb.bot.id
    # data["bot_id"] = 543260180
    data[
        "callback_url"
    ] = f"{settings.BACKEND_URL}{settings.VERIFY_CALLBACK_ENDPOINT}".format(
        token=body.token
    )
    # data[
    #     "callback_url"
    # ] = "https://core.telegram.org/passport/example?passport_ssid=175ee0225fcc4dce880ba841ea07f993_98508773_7a3b4c4fa717189b1c"
    data["scope"] = {
        "data": [
            {"type": "id_document", "selfie": True},
            "address_document",
            "email",
        ],
        "v": "1",
    }
    data["nonce"] = body.token
    data["nonce"] = "175ee0225fcc4dce880ba841ea07f993_98508773_c135032610860da1a6"
    import json
    print(json.dumps(data))

    return JSONResponse(data)


@router.get("/verify/callback/{token}")
async def verify_callback(token: str, tg_passport: str = None):
    session = get_session(token=token)
    if not session:
        with open(f"{settings.BASE_DIR}/app/verification/unauthorized.html") as f:
            html = f.read()
        return HTMLResponse(html, status_code=401)

    if tg_passport.lower() == "success":
        with open(f"{settings.BASE_DIR}/app/verification/success.html") as f:
            html = f.read()

        return HTMLResponse(html)

    with open(f"{settings.BASE_DIR}/app/verification/failure.html") as f:
        html = f.read()

    return HTMLResponse(html)
