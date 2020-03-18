import mysql.connector

mydb = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7328399",
    passwd="JiuG5rmmFh",
    database='sql7328399',
    port="3306"
)
mycursor = mydb.cursor()

def printresult(result):
  for x in mycursor:
    print(x)


# mycursor.execute("CREATE TABLE gregs_list (last_name VARCHAR(20) NOT NULL, first_name varchar(20) NOT NULL, gender char(1) NOT NULL, email varchar(100) NOT NULL, phone char(10) NOT NULL, birthday date NOT NULL, profession varchar(20) NOT NULL, location varchar(20) NOT NULL, interests varchar(100) NOT NULL, status varchar(10) NOT NULL)")
# sqlinsert="Insert Into gregs_list Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# values=[
#   ('Quill', 'Peter', 'M', 'quillPeter@list.com', '0508765234','1989-06-13','Teacher', 'New-York, NY', 'books, art, animals', 'married'),
#   ('Grant', 'Emma', 'F', 'grantEmma@list.com', '0509876781', '1995-07-27', 'Actor','Texas, TX', 'animals, music, sport', 'free'),
#   ('Williams', 'John', 'M', 'williamsJohn@list.com', '0504567123','1993-09-17', 'Programmer', 'Chicago, CH','sport, programming, coffee', 'free'),
#   ('Hamilton','Caroline', 'F', 'hamiltonCaroline@list.com', '0502387123', '1992-08-05', 'Doctor', 'Los-Angeles, LA', 'books, cooking, horses', 'married')
# ]
# mycursor.executemany(sqlinsert,values)


# mycursor.execute("CREATE TABLE zip (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, city varchar(40) NOT NULL, state char(2) NOT NULL);")
# mycursor.execute("CREATE TABLE restaurant (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, zip INT, capacity INT NOT NULL, FOREIGN KEY(zip) REFERENCES zip(id));")
# mycursor.execute("CREATE TABLE meal (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, price DECIMAL(2,2), prep_time TIME);")
# mycursor.execute("CREATE TABLE meal_rest (rest_id INT, meal_id INT, FOREIGN KEY(rest_id) REFERENCES restaurant(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
<<<<<<< HEAD
mycursor.execute("CREATE TABLE checkue (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, rest_id INT, meal_id INT, amount INT, date DATETIME, FOREIGN KEY(rest_id) REFERENCES restaurant(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
# mycursor.execute("CREATE TABLE supplier (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, title varchar(30), phone CHAR(13), e_mail varchar(40));")
=======
# mycursor.execute("CREATE TABLE cheque (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, rest_id INT, meal_id INT, amount INT, date DATETIME, FOREIGN KEY(rest_id) REFERENCES restaurant(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
# mycursor.execute("CREATE TABLE supplier (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, title VARCHAR(30), phone CHAR(13), e_mail VARCHAR(40));")
>>>>>>> d6c35f4c04804251303223f5a5206cffc647271f
# mycursor.execute("CREATE TABLE product (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, price DECIMAL(2,2), supp_id INT, FOREIGN KEY(supp_id) REFERENCES supplier(id));")
# mycursor.execute("CREATE TABLE meal_product (meal_id INT, prod_id INT, FOREIGN KEY(prod_id) REFERENCES product(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
# mycursor.execute("CREATE TABLE reservation (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, rest_id INT, date_start DATETIME, date_end DATETIME, visitors INT, FOREIGN KEY(rest_id) REFERENCES restaurant(id));")
# mycursor.execute("CREATE TABLE meel_reserv (reserv_id INT, meal_id INT, FOREIGN KEY(reserv_id) REFERENCES reservation(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
<<<<<<< HEAD
# mycursor.execute("CREATE TABLE employee (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, rest_id INT, first_name varchar(20) NOT NULL, last_name varchar(20) NOT NULL, gender char(1) NOT NULL, birthdate DATE NOT NULL, phone char(13) NOT NULL, e_mail varchar(50) NOT NULL, position varchar(30) NOT NULL, wage INT, FOREIGN KEY(rest_id) REFERENCES restaurant(id));")
=======
# mycursor.execute("CREATE TABLE employee (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, rest_id INT, first_name VARCHAR(20) NOT NULL, last_name VARCHAR(20) NOT NULL, gender char(1) NOT NULL, birthdate DATE NOT NULL, phone char(13) NOT NULL, e_mail varchar(50) NOT NULL, position varchar(30) NOT NULL, wage INT, FOREIGN KEY(rest_id) REFERENCES restaurant(id));")
>>>>>>> d6c35f4c04804251303223f5a5206cffc647271f
# mycursor.execute("CREATE TABLE emp_reserv (reserv_id INT, emp_id INT, FOREIGN KEY(reserv_id) REFERENCES reservation(id), FOREIGN KEY(emp_id) REFERENCES employee(id));")


mycursor.execute('Show Tables')
printresult(mycursor)
# mycursor.execute('desc Zip_code')

mydb.close()
