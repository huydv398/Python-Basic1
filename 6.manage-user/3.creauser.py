# importing required library 
import mysql.connector 

# kết nối với máy chủ mysql
conn  = mysql.connector.connect(host = "localhost", user = "huydv", passwd = "Duonghuy@2023", auth_plugin='mysql_native_password', database="dbtest")

# chuẩn bị một đối tượng con trỏ
cursorObject = conn.cursor()

# drop clause 
statement ="UPDATE STUDENT SET NAME = 'Duong Huy' WHERE NAME ='Vani'"
  
cursorObject.execute(statement) 

conn.commit()


# # thực hiện câu lệnh xóa 
# # commit to the database
# cursorObject.execute(sinhvien_tb_delete)
# conn.commit()

# # cuối cùng đóng kết nối cơ sở dữ liệu
conn.close()