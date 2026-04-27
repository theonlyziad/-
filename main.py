from app.config import load_settings
from app.telegram_bot import LongCatTelegramBot


def main() -> None:
    settings = load_settings()
    bot = LongCatTelegramBot(settings)
    app = bot.build()
    print("ZED LongCat Telegram Bot is running...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
