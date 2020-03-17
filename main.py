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
# mycursor.execute('Show Tables')
# printresult(mycursor)
# mycursor.execute("Drop table gregs_list")
# printresult(mycursor)

# mycursor.execute("CREATE TABLE Zip_code (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, City varchar(40) NOT NULL, State char(2) NOT NULL);")
# mycursor.execute("CREATE TABLE Restaurants (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, zip_code INT, Capacity INT NOT NULL, FOREIGN KEY(zip_code) REFERENCES Zip_code(ID));")
# mycursor.execute("CREATE TABLE Meals (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Price DECIMAL(2,2), Prep_time TIME);")
# mycursor.execute("CREATE TABLE Rest_Menu (ID_Rest INT, ID_Meal INT, FOREIGN KEY(ID_Rest) REFERENCES Restaurants(ID), FOREIGN KEY(ID_Meal) REFERENCES Meals(ID));")
# mycursor.execute("CREATE TABLE Orders (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Rest INT, ID_Meal INT, Amount INT, Date DATETIME, FOREIGN KEY(ID_Rest) REFERENCES Restaurants(ID), FOREIGN KEY(ID_Meal) REFERENCES Meals(ID));")
# mycursor.execute("CREATE TABLE Suppliers (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(30), Phone CHAR(13), E_Mail VARCHAR(40));")
# mycursor.execute("CREATE TABLE Products (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Price DECIMAL(2,2), ID_Sup INT, FOREIGN KEY(ID_Sup) REFERENCES Suppliers(ID));")
# mycursor.execute("CREATE TABLE Ingridients (ID_Meal INT, ID_Prod INT, FOREIGN KEY(ID_Prod) REFERENCES Products(ID), FOREIGN KEY(ID_Meal) REFERENCES Meals(ID));")
# mycursor.execute("CREATE TABLE Reservations (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Rest INT, Date_start DATETIME, Date_end DATETIME, Visitors INT, FOREIGN KEY(ID_Rest) REFERENCES Restaurants(ID));")
# mycursor.execute("CREATE TABLE Event_Menu (ID_Reserv INT, ID_Meal INT, FOREIGN KEY(ID_Reserv) REFERENCES Reservations(ID), FOREIGN KEY(ID_Meal) REFERENCES Meals(ID));")
# mycursor.execute("CREATE TABLE Employees (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ID_Rest INT, First_name VARCHAR(20) NOT NULL, Last_name VARCHAR(20) NOT NULL, Gender char(1) NOT NULL, Birthdate DATE NOT NULL, Phone char(13) NOT NULL, E_Mail varchar(50) NOT NULL, Position varchar(30) NOT NULL, Wage INT, FOREIGN KEY(ID_Rest) REFERENCES Restaurants(ID));")
# mycursor.execute("CREATE TABLE Staff_Event (ID_Reserv INT, ID_Emp INT, FOREIGN KEY(ID_Reserv) REFERENCES Reservations(ID), FOREIGN KEY(ID_Emp) REFERENCES Employees(ID));")


mycursor.execute('Show Tables')
printresult(mycursor)
# mycursor.execute('desc Zip_code')
# printresult(mycursor)


mydb.close()