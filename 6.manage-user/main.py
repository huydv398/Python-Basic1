from flask import Flask, render_template, request
from __future__ import print_function
import requests, json
import mysql.connector 
from mysql.connector import errorcode
### Variables
DB_NAME = 'dbtest'
DB_USER = 'huydv'
DB_PASS = 'Duonghuy@2023'


TABLES = {}

TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `MSV` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ")")


# kết nối với máy chủ mysql
# conn  = mysql.connector.connect(host = "localhost", user = database_name, passwd = database_passpw, auth_plugin='mysql_native_password', database = database_name)
conn  = mysql.connector.connect(host = "localhost", user = "huydv", passwd = "Duonghuy@2023", auth_plugin='mysql_native_password', database="dbtest") 
cursorObject = conn.cursor()

def create_database(cursorObject):
    try:
        cursorObject.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursorObject.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursorObject)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

def create_tb_student():
    studentRecord = """CREATE TABLE tb_student (
                    MSV int NOT NULL AUTO_INCREMENT,
                    NAME VARCHAR(50) NOT NULL,
                    BIRTHDAY DATE NOT NULL,
                    ADDR_BORN VARCHAR,
                    PHONE VARCHAR,
                    EMAIL VARCHAR,
                    CCCD VARCHAR,
                    ADDR VARCHAR(100),
                    Status int,
                    PRIMARY KEY (MSV)
                    )"""
    # table created
    cursorObject.execute(studentRecord)
    # disconnecting from server
    conn.close()

# create_tb_student()
# check table exists?
stmt = "SHOW TABLES LIKE 'tb_student'"
cursorObject.execute(stmt)
result = cursorObject.fetchone()
if result:
    print ("OK table")
else:
    create_tb_student()
    print("Create table Success")

def Insert():
    sql = "INSERT INTO tb_student (NAME, BIRTHDAY, ADDR_BORN, PHONE, EMAIL, CCCD, ADDR) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = ("Duong van Huy", "1998-03-18", "Phuc yen, Vinh Phuc", "0389724444", "huydv@suncloud.vn", "123123123", "Vinh phuc")
    cursorObject.execute(sql, val)
    conn.commit()
    
    print(cursorObject.rowcount, "details inserted")
    
    # disconnecting from server
    conn.close()
    
# Insert()

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list-user")
def list_user():
    
    select = """SELECT * FROM tb_student WHERE Status='1'"""
    cursorObject.execute(select)
    result = cursorObject.fetchall()
    # # for e in sinvien_data:
    # #     print(e)
    # conn.close()
    # return result
    return render_template("list-user.html", result=result)

@app.route("/edit-user/<int:MSV>", methods=['GET', 'POST'])
def edit_user(MSV):
    if request.method == 'GET':
        return f'Hello {MSV} !'
    if request.method == 'POST':
        return "edit-post"
    

@app.route("/createuser", methods=['GET', 'POST'])
def createuser():
    if request.method == 'GET':
        return render_template("createuser.html")
        # return render_template("create-user.html", results_cluster=results_cluster)
    if request.method == 'POST':
        #thiết lập chuẩn dữ liệu của DATABASE
        name = request.form['Name']
        birthday = request.form['birthday']
        addr1 = request.form['addr_born']
        phonenum = request.form['phonenum']
        email = request.form['email']
        cccd = request.form['cccd']
        addr2 = request.form['addr']
        cursorObject.execute("insert into tb_student (NAME, BIRTHDAY, ADDR_BORN, PHONE, EMAIL, CCCD, ADDR) values (%s,%s,%s,%s,%s,%s,%s)", (name,birthday,addr1,phonenum,email,cccd,addr2))
        conn.commit()
        return render_template("test.html")
    
@app.route("/createuser", methods=['GET', 'POST'])
def createuser():
    if request.method == 'GET':
        return render_template("createuser.html")
        # return render_template("create-user.html", results_cluster=results_cluster)
    if request.method == 'POST':
        return ("ok")        
@app.route("/deluser", methods=['POST'])    
def deluser():
    if request.method == 'POST':
        name = request.form['MSV']
        cursorObject.execute("UPDATE tb_student SET Status = 0 WHERE MSV = " + name)
        conn.commit()
        # conn.close()
        return render_template("test.html", result=result)    
    
if __name__ == "__main__":
	app.run(host='10.0.11.91', debug=True, port=80)
