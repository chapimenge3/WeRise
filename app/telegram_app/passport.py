from secrets import token_urlsafe
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext._contexttypes import ContextTypes

from internal.dao.user import create_user, get_user
from internal.dao.session import create_session, get_session
from app.models.user import UserSchema
from app.telegram_app import constants
from app.settings import settings


async def verify_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo the user message."""
    chat_id = update.message.chat.id
    chat_type = update.message.chat.type
    if chat_type != "private":
        await update.message.reply_text(constants.USE_ONLY_PRIVATE_CHAT)
        return {"status": "error"}

    user_id = update.message.from_user.id
    user = get_user(str(user_id))

    if not user:
        user_data = update.message.from_user.to_dict()
        user_data["telegram_id"] = user_data.pop("id")
        user_details = UserSchema(**user_data)
        create_user(user_details)
        message = constants.WELLCOME_MESSAGE.format(first_name=user_details.first_name)
        await context.bot.send_message(chat_id=chat_id, text=message)
        return {"status": "ok"}

    message = constants.VERIFY_IDENTIFY
    token = token_urlsafe(32)
    keyboard = [
        [
            InlineKeyboardButton(
                "Verify💳",
                url=settings.BACKEND_URL + settings.VERIFY_ENDPOINT.format(token=token),
            ),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=chat_id, text=message, reply_markup=reply_markup
    )

    # save token to session
    create_session(user_id, token, None)
    return {"status": "ok"}


async def get_passport_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Downloads and prints the received passport data."""
    # Retrieve passport data
    passport_data = update.message.passport_data
    token = passport_data.decrypted_credentials.nonce
    session = get_session(token=token)
    if not session:
        print("session not found")
    
    user = update.message.from_user

    for data in passport_data.decrypted_data:
        if data.type == "phone_number":
            print("Phone: ", data.phone_number)

        elif data.type == "email":
            print("Email: ", data.email)

        if data.type in (
            "personal_details",
            "passport",
            "driver_license",
            "identity_card",
            "internal_passport",
            "address",
        ):
            print(data.type, data.data)

        if data.type in (
            "utility_bill",
            "bank_statement",
            "rental_agreement",
            "passport_registration",
            "temporary_registration",
        ):
            print(data.type, len(data.files), "files")
            for file in data.files:
                actual_file = await file.get_file()
                print(actual_file)
                await actual_file.download_to_drive()
        if (
            data.type
            in ("passport", "driver_license", "identity_card", "internal_passport")
            and data.front_side
        ):
            front_file = await data.front_side.get_file()
            print(data.type, front_file)
            await front_file.download_to_drive()
        if data.type in ("driver_license" and "identity_card") and data.reverse_side:
            reverse_file = await data.reverse_side.get_file()
            print(data.type, reverse_file)
            await reverse_file.download_to_drive()
        if (
            data.type
            in ("passport", "driver_license", "identity_card", "internal_passport")
            and data.selfie
        ):
            selfie_file = await data.selfie.get_file()
            print(data.type, selfie_file)
            await selfie_file.download_to_drive()
        if data.translation and data.type in (
            "passport",
            "driver_license",
            "identity_card",
            "internal_passport",
            "utility_bill",
            "bank_statement",
            "rental_agreement",
            "passport_registration",
            "temporary_registration",
        ):
            print(data.type, len(data.translation), "translation")
            for file in data.translation:
                actual_file = await file.get_file()
                print(actual_file)
                await actual_file.download_to_drive()

    await context.bot.send_message(user.id, constants.DOCUMENT_RECIEVED.format(first_name=user.first_name)) 