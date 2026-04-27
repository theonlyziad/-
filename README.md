# LongCat Telegram Bot

A Telegram AI bot powered by LongCat OpenAI-compatible API.

## Features

- Text chat
- Thinking mode
- Lite mode
- Omni multimodal mode
- Image understanding
- Voice/audio understanding
- Video understanding
- PDF/DOCX/TXT/code file analysis
- Voice replies with `/speak`
- Railway/Docker ready

## Environment variables

Copy `.env.example` to `.env` and fill:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
LONGCAT_API_KEY=your_longcat_api_key
LONGCAT_BASE_URL=https://api.longcat.chat/openai
DEFAULT_TEXT_MODEL=LongCat-Flash-Chat
DEFAULT_THINKING_MODEL=LongCat-Flash-Thinking-2601
DEFAULT_LITE_MODEL=LongCat-Flash-Lite
DEFAULT_OMNI_MODEL=LongCat-Flash-Omni-2603
```

## Run locally

```bash
pip install -r requirements.txt
python main.py
```

## Railway

Set the environment variables in Railway Variables, then deploy. The included `Procfile` starts the bot.
