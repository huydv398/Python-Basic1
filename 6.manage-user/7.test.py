import logging
import time
import datetime
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from flask import Flask, render_template, request
from datetime import datetime

config = {
    'user': 'duonghuy',
    'password': 'Duonghuy@2023',
    'host': '127.0.0.1',
    'database': 'db_huydv',
    'raise_on_warnings': True,
    'auth_plugin': 'mysql_native_password'
}
DB_NAME = 'db_huydv'

TABLES = {}
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

try:
    # connect = mysql.connector.connect(user='huydv', password='Duonghuy@2023', host='localhost', database='dbtest', auth_plugin='mysql_native_password')
    # connect = mysql.connector.connect(user='huydv', database='dbtest')
    conn = mysql.connector.connect(**config)

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
    conn.close()    
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)