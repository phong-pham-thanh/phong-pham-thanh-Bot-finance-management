
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import sqlite3
from datetime import datetime

DB_FILE = "expenses.db"



# Load biến môi trường
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text if update.message else ""
    parts = [part.strip() for part in text.split(",") if part.strip()]

    if not parts:
        await update.message.reply_text("Vui lòng nhập chuỗi có dấu ',' để tách.")
        return

    # if len(parts) != 2:
    #     await update.message.reply_text("Nhập 2 part thôi")
    #     return

    # add_expense(parts[0], parts[1])
    # response = "\n".join(parts)
    await update.message.reply_text("Đã thêm: " + parts[0] + " " + parts[1])

def add_expense(reason: str, amount: int):
    """Thêm một khoản chi tiêu vào bảng daily_process"""
    createdDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO daily_process (createdDate, reason, amount)
        VALUES (?, ?, ?)
    """, (createdDate, reason, amount))

    conn.commit()
    conn.close()

    print(f"✅ Đã thêm: {createdDate} | {reason} | {amount}đ")

async def main():
    if not BOT_TOKEN:
        print("❌ Không tìm thấy BOT_TOKEN trong biến môi trường.")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot đang chạy...")
    await app.initialize()      # 👈 bảo đảm ExtBot được khởi tạo
    await app.start()           # bắt đầu bot
    await app.updater.start_polling()  # bắt đầu lấy tin nhắn

    # Đợi cho đến khi nhấn Ctrl+C
    await asyncio.Event().wait()

    await app.stop()
    await app.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
