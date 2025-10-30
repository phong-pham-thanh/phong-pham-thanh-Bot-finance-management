import sqlite3

# Tên file database (nếu chưa có sẽ được tạo mới)
db_file = "expenses.db"

# Kết nối đến SQLite
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Tạo bảng daily_process
cursor.execute("""
CREATE TABLE IF NOT EXISTS daily_process (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    createdDate DATETIME NOT NULL,
    reason TEXT NOT NULL,
    amount INTEGER NOT NULL
)
""")

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("✅ Bảng 'daily_process' đã được tạo (nếu chưa có).")
