import logging
import time
import datetime
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from flask import Flask, render_template, request
from datetime import datetime

config = {
    'user': 'huydv',
    'password': 'Duonghuy@2023',
    'host': '127.0.0.1',
    'database': 'dbtest',
    'raise_on_warnings': True,
    'auth_plugin': 'mysql_native_password'
}
DB_NAME = 'dbtest'
# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


# Log to console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Also log to a file
file_handler = logging.FileHandler("cpy-errors.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler) 

def connect_to_mysql(config, attempts=3, delay=2):
    attempt = 1
    # Implement a reconnection routine
    while attempt < attempts + 1:
        try:
            return mysql.connector.connect(**config)
        except (mysql.connector.Error, IOError) as err:
            if (attempts is attempt):
                # Attempts to reconnect failed; returning None
                logger.info("Failed to connect, exiting without a connection: %s", err)
                return None
            logger.info(
                "Connection failed: %s. Retrying (%d/%d)...",
                err,
                attempt,
                attempts-1,
            )
            # progressive reconnect delay
            time.sleep(delay ** attempt)
            attempt += 1
    return None

# try cho phép bạn kiểm tra lỗi của một block of code.
try:
    # connect = mysql.connector.connect(user='huydv', password='Duonghuy@2023', host='localhost', database='dbtest', auth_plugin='mysql_native_password')
    # connect = mysql.connector.connect(user='huydv', database='dbtest')
    connect = mysql.connector.connect(**config)

# except cho phép bạn xử lý lỗi.
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
# else cho phép bạn thực thi code khi không có lỗi.
else:
    connect.close()    
    
TABLES = {}
# TABLES['employees'] = (
#     "CREATE TABLE `employees` ("
#     "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
#     "  `birth_date` date NOT NULL,"
#     "  `first_name` varchar(14) NOT NULL,"
#     "  `last_name` varchar(16) NOT NULL,"
#     "  `gender` enum('M','F') NOT NULL,"
#     "  `hire_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`)"
#     ") ENGINE=InnoDB")

# TABLES['departments'] = (
#     "CREATE TABLE `departments` ("
#     "  `dept_no` char(4) NOT NULL,"
#     "  `dept_name` varchar(40) NOT NULL,"
#     "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
#     ") ENGINE=InnoDB")

TABLES['tb_student'] = (
    "CREATE TABLE `tb_student` ("
    "  `MSV` int NOT NULL AUTO_INCREMENT,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `birth_date` date NOT NULL,"
    "  `ADDR_BORN` varchar(255) NOT NULL,"
    "  `ADDR` varchar(255) NOT NULL,"
    "  `PHONE` varchar(10) NOT NULL,"
    "  `CCCD` varchar(12) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` TIMESTAMP NOT NULL,"
    "  `EMAIL` varchar(255) NOT NULL,"
    "  `Status` INT DEFAULT 1,"
    "  PRIMARY KEY (`MSV`)"
    ") ENGINE=InnoDB")

#Mở một kết nối đến máy chủ MySQL và lưu trữ đối tượng kết nối trong biến con.
conn = mysql.connector.connect(**config)

# tạo một con trỏ mới: cursor, theo mặc định là đối tượng MySQLCursor,
# sử dụng phương thức cursor() của connector.
cursor = conn.cursor()

# create database
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        conn.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# conn.close()
# cursor.close()
# # ====== Test=========
# tomorrow = datetime.now().date() + timedelta(days=1)

# # print(tomorrow)
# add_employee = ("INSERT INTO employees "
#                 "(first_name, last_name, hire_date, gender, birth_date) "
#                 "VALUES (%s, %s, %s, %s, %s)")

# data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
# # Insert new employee
# cursor.execute(add_employee, data_employee)


# # emp_no = cursor.lastrowid
# # add_salary = ("INSERT INTO salaries "
# #                 "(emp_no, salary, from_date, to_date) "
# #                 "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
# # # Insert salary information
# # data_salary = {
# #     'emp_no': emp_no,
# #     'salary': 50000,
# #     'from_date': tomorrow,
# #     'to_date': date(9999, 1, 1),
# # }
# # cursor.execute(add_salary, data_salary)

# # Make sure data is committed to the database
# conn.commit()

# # cursor.close()
# conn.close()

# query = ("SELECT first_name, last_name, hire_date FROM employees ")



# cursor.execute(query)

# for (first_name, last_name, hire_date) in cursor:
#     print("{}, {} was hired on {:%d %b %Y}".format(
#         last_name, first_name, hire_date))

# cursor.close()
# conn.close()



# # =======END TEST==================


print("OK em iu")

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user")
def list_user():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    select = """SELECT * FROM tb_student WHERE Status='1'"""
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("list-user.html", result=result)

@app.route("/user/<param>", methods=['GET', 'POST'])
def edituser(param):
    if request.method == 'GET':
        # return param
        func = "Sửa thông tin Sinh viên"
        conn = mysql.connector.connect(**config)
        action = "{{ url_for('edituser') }}"
        cursor = conn.cursor()
        select = ("SELECT * FROM tb_student WHERE Status='1' AND MSV = " + param)
        cursor.execute(select)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # return result
        return render_template("createuser.html", result=result, func=func, param=param, action=action)
    if ((request.method == 'POST') and (param != 0)):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        # edit_sinhvien = ("""UPDATE tb_student 
        #                 SET (last_name = %(name)s, birth_date =  %(birthday)s , ADDR =  %(addr1)s, PHONE = %(phonenum)s, gender = %(gender)s, EMAIL = %(email)s, CCCD = %(cccd)s, ADDR_BORN = %(addr2)s, hire_date = %(today)s)
        #                 WHERE MSV = '%(id)s'""")
        # name = request.form['Name']
        edit_sinhvien = ("UPDATE tb_student SET last_name = %(name)s , birth_date =  %(birthday)s , ADDR =  %(addr2)s, PHONE = %(phonenum)s, gender = %(gender)s, EMAIL = %(email)s, CCCD = %(cccd)s, ADDR_BORN = %(addr1)s, hire_date = %(today)s WHERE MSV = %(id)s")
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        data_sinhvien = {
            'name': request.form['Name'],
            'birthday': request.form['birthday'],
            'addr1': request.form['addr'],
            'phonenum': request.form['phonenum'],
            'gender': request.form['gender'],
            'email': request.form['email'],
            'cccd': request.form['cccd'],
            'addr2':request.form['addr_born'],
            'today': timestamp,
            'id': request.form['MSV']
        }
        cursor.execute(edit_sinhvien, data_sinhvien)
        conn.commit()
        cursor.close()
        conn.close()
        return render_template("test.html")
        # return data_sinhvien

@app.route("/createuser", methods=['GET', 'POST'])
def createuser():
    if request.method == 'GET':
        func = "Tạo sinh viên mới"
        action = "/createuser"
        param = ''
        result = [['']]
        # return fun
        return render_template("createuser.html", func=func, result=result, param = '', action=action)
        # return render_template("create-user.html", results_cluster=results_cluster)
    if request.method == 'POST':
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        # #thiết lập chuẩn dữ liệu của DATABASE
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print("Timestamp:", current_timestamp)
        # name = request.form['Name']
        # birthday = request.form['birthday']
        # addr1 = request.form['addr_born']
        
        # phonenum = request.form['phonenum']
        # email = request.form['email']
        # cccd = request.form['cccd']
        # addr2 = request.form['addr']
        # gender = request.form['gender']
        
        add_sinhvien = ("INSERT INTO tb_student "
                        "(last_name, birth_date, ADDR, PHONE, gender, EMAIL, CCCD, ADDR_BORN, hire_date) "
                        "VALUES (%(name)s, %(birthday)s, %(addr1)s, %(phonenum)s, %(gender)s, %(email)s, %(cccd)s, %(addr2)s, %(today)s)")
        # name = request.form['Name']
        
        data_sinhvien = {
            'name': request.form['Name'],
            'birthday': request.form['birthday'],
            'addr1': request.form['addr'],
            'phonenum': request.form['phonenum'],
            'gender': request.form['gender'],
            'email': request.form['email'],
            'cccd': request.form['cccd'],
            'addr2':request.form['addr_born'],
            'today': timestamp
        }
        # test = ("John", "Highway 21")
        # Insert new employee
        # cursor.execute("INSERT INTO tb_student (last_name, birth_date, ADDR, PHONE, gender, EMAIL, CCCD, ADDR_BORN, hire_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, birthday, addr2, phonenum, gender, email, cccd, addr1, today))
        cursor.execute(add_sinhvien, data_sinhvien)
        conn.commit()
        cursor.close()
        conn.close()
        return render_template("test.html")
        # return data_sinhvien

@app.route("/deluser", methods=['POST'])    
def deluser():
    if request.method == 'POST':
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        name = request.form['MSV']
        cursor.execute("UPDATE tb_student SET Status = 0 WHERE MSV = " + name)
        conn.commit()
        cursor.close()
        conn.close()
        return render_template("test.html")  
        # return name

@app.route("/test")
def test():
    test = "huydv"
    return render_template("test.html", test = test)

if __name__ == "__main__":
	app.run(host='10.0.11.91', debug=True, port=80)