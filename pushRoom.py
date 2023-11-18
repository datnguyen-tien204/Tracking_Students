import pyodbc
def pushRoom(server, database, table, room_name, date_to_push):
    # Tạo kết nối
    try:
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {table} (maphong, ngay) VALUES (?, ?)", (room_name, date_to_push))

        # Nếu ngày chưa tồn tại, thêm mới dữ liệu
        #cursor.execute(f"INSERT INTO {table} (maphong, ngay) VALUES (?, ?)", room_name, date_to_push)
        connection.commit()
        connection.close()
        return True

    except:
        return False

if '__name__' == '__main__':
    pushRoom()
