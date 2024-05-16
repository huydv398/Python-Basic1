# importing required library 
import mysql.connector 

# kết nối với máy chủ mysql
conn  = mysql.connector.connect(host = "localhost", user = "root", passwd = "Duonghuy@2023!@#", auth_plugin='mysql_native_password', database="dbtest")  
# conn  = mysql.connector.connect(host = "localhost", user = "huydv", passwd = "Duonghuy@2023", auth_plugin='mysql_native_password', database="dbtest")  

# chuẩn bị một đối tượng con trỏ
cursorObject = conn.cursor()

# insert statement for tblemployee
# this statement will enable us to insert multiple rows at once.
employeetbl_insert = """INSERT INTO STUDENT (
                        NAME,
                        ADDR,
                        PHONE,
                        CODE,
                        AGE) 
                        VALUES  (%s, %s, %s, %s, %s)"""

# we save all the row data to be inserted in a data variable
data = [("Vani", "HA NOI", "0987987987", "IT01","30"),
        ("huydv", "VINH PHUC", "0123123123", "IT01","20"),
        ("conglv", "PHU THO", "0123654654", "IT01","65"),
        ("quangKT", "NAM DINH", "0999888777", "IT01","19"),
        ("linhnt", "SAI GON", "0111222333", "IT01","45")]

cursorObject.executemany(employeetbl_insert, data)
cursorObject.commit()


# # thực hiện câu lệnh xóa 
# # commit to the database
# cursorObject.execute(sinhvien_tb_delete)
# conn.commit()

# # cuối cùng đóng kết nối cơ sở dữ liệu
conn.close()