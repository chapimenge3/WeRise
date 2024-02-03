from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext._contexttypes import ContextTypes

from app.models.user import UserSchema
from internal.dao.user import create_user, get_user

from app.telegram_app import constants


