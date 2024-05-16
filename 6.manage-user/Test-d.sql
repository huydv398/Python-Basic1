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
    "  `hire_date` date NOT NULL,"
    "  `EMAIL` varchar(255) NOT NULL,"
    "  `Status` INT DEFAULT 1,"
    "  PRIMARY KEY (`MSV`)"
    ") ENGINE=InnoDB")

INSERT INTO tb_student (last_name, birth_date, ADDR, PHONE, gender, EMAIL, CCCD, ADDR_BORN, hire_date) 
VALUES ('Duonghuy', '1977-06-14', 'Phuc Yen - Vinh Phuc', '0389724444', 'M', 'Huydv@suncloud.vn', '026098000503', 'Ha noi', '1977-06-14');

("INSERT INTO salaries "
"(emp_no, salary, from_date, to_date) "
"VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

cursorObject.execute("insert into tb_student (NAME, BIRTHDAY, ADDR_BORN, PHONE, EMAIL, CCCD, ADDR) values (%s,%s,%s,%s,%s,%s,%s)", (name,birthday,addr1,phonenum,email,cccd,addr2))
