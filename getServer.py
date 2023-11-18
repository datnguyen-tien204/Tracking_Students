import pyodbc
def getServer():
    servers = []
    servers.append("")
    conn = pyodbc.connect("DRIVER={SQL Server};SERVER=(local);DATABASE=master;Trusted_Connection=yes")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sys.servers")
    results = cursor.fetchall()
    conn.close()
    for server in results:
        servers.append(server[0])
    return servers

def getDatabase(name_server):

    # Tạo chuỗi kết nối
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={name_server};Trusted_Connection=yes;'
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    database_names = [""]
    cursor.execute("SELECT name FROM sys.databases")
    database_names.extend([row.name for row in cursor.fetchall()])
    conn.close()
    return database_names

def getTable(server,database):
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    table_names = []
    table_names.append("")

    # Sử dụng truy vấn SQL để lấy danh sách tên bảng
    table_query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"

    cursor.execute(table_query)

    for row in cursor.fetchall():
        table_names.append(row.TABLE_NAME)
    conn.close()

    return table_names