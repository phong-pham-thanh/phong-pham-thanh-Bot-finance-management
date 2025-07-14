import os
from telegram.ext import Updater, MessageHandler, Filters
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Lấy token Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")

def handle_message(update, context):
    text = update.message.text
    parts = [part.strip() for part in text.split(',') if part.strip()]

    if not parts:
        update.message.reply_text("Vui lòng nhập chuỗi có dấu ',' để tách.")
        return

    response = '\n'.join(parts)
    update.message.reply_text(response)

def main():
    if not BOT_TOKEN:
        print("❌ Không tìm thấy BOT_TOKEN trong biến môi trường.")
        return

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    print("🤖 Bot đang chạy...")
    updater.idle()

if __name__ == '__main__':
    main()
