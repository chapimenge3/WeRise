from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext._contexttypes import ContextTypes

from app.models.user import UserSchema
from internal.dao.user import create_user, get_user

from app.telegram_app import constants


# Example handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    chat_id = update.message.chat.id
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

    message = constants.START_COMMAND.format(first_name=user.first_name)
    await context.bot.send_message(chat_id=chat_id, text=message)
    return {"status": "ok"}

async def echo(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

    return {"status": "ok"}


async def help(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    await update.message.reply_text(constants.HELP_COMMAND)