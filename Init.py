from azure.data.tables import TableServiceClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()



connection_string = os.getenv("DB_CONNECTION")

table_name = "Transactions"

# Khởi tạo service client và bảng
service = TableServiceClient.from_connection_string(conn_str=connection_string)
table_client = service.create_table_if_not_exists(table_name=table_name)

# Tạo 1 entity với các cột như bạn yêu cầu
# transaction = {
#     "PartitionKey": "finance",      # Có thể chia theo tháng/năm nếu muốn phân vùng
#     "RowKey": "txn001",             # ID duy nhất cho mỗi dòng
#     "CreatedDate": datetime.utcnow(),
#     "Amount": 1_250_000.50,
#     "IsIncome": True,
#     "Reason": "Lương tháng 7"
# }

# # Thêm entity vào bảng
# table_client.create_entity(entity=transaction)

# print("Đã thêm giao dịch thành công.")