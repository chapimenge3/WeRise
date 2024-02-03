from telegram.ext import Application, CommandHandler, MessageHandler, filters
from pathlib import Path
from app.settings import settings
from .handlers import start, echo, help
from .passport import verify_user, get_passport_data


private_key = Path(f"{settings.BASE_DIR}/private.key")
# Initialize python telegram bot
ptb = (
    Application.builder()
    .updater(None)
    .token(settings.TELEGRAM_TOKEN)
    .private_key(private_key.read_bytes())
    .build()
)

ptb.add_handler(CommandHandler("start", start))
ptb.add_handler(CommandHandler("help", help))
ptb.add_handler(CommandHandler("verify", verify_user))
ptb.add_handler(MessageHandler(filters.PASSPORT_DATA, get_passport_data))
ptb.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
