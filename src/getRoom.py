import pyodbc
from datetime import date
ngay_hien_tai = date.today()

# server = 'NGUYENTIENDAT'
# database = 'ProJect_StartUP'
# table='Phong

def getRoom(server,database,table):
    l=[]
    # username = 'your_username'
    # password = 'your_password'

    # Tạo kết nối
    #connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database) #+ ';UID=' + username + ';PWD=' + password)
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute(f"SELECT MAPHONG, NGAY FROM {table} WHERE NGAY = '{ngay_hien_tai}'")

    for row in cursor:
        l.append(row)

    cleaned_data = [(item[0], item[1].strftime('%Y-%m-%d')) for item in l]
    return cleaned_data


if '__name__'=='__main__':
    getRoom()
