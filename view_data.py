from azure.data.tables import TableServiceClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Kết nối
connection_string = os.getenv("DB_CONNECTION")

if not connection_string:
    raise ValueError("Biến môi trường DB_CONNECTION chưa được thiết lập.")

table_name = "Transactions"

# Lấy bảng
service = TableServiceClient.from_connection_string(conn_str=connection_string)
table_client = service.get_table_client(table_name=table_name)

# Lấy danh sách entity (bản ghi)
entities = table_client.list_entities()

# In ra từng dòng
for entity in entities:
    print("-" * 40)
    print(f"RowKey: {entity['RowKey']}")
    print(f"CreatedDate: {entity.get('CreatedDate')}")
    print(f"Amount: {entity.get('Amount')}")
    print(f"IsIncome: {entity.get('IsIncome')}")
    print(f"Reason: {entity.get('Reason')}")
