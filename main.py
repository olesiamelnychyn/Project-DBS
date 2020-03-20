import mysql.connector

mydb = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7328399",
    passwd="JiuG5rmmFh",
    database='sql7328399',
    port="3306",
)
mycursor = mydb.cursor()
print("run the mydb")

def printresult(result):
  for x in mycursor:
    print(x)

def getresult(result):
  res=[]
  for x in mycursor:
    res.append(x)
  return res

def search_all(args):
  result=["Nothing"]

  if(args['group_by']!=''):
    if(args['group_by']=='reservation'):
      search="select r.reserv_id, sum(e.wage) from employee e join emp_reserv r on r.emp_id=e.id group by r.reserv_id"
    elif(args['group_by']=='restaurant'):
      search="select rest_id, sum(wage) from employee group by rest_id"
    else: 
      search="select "+args['group_by']+", sum(wage) from employee group by "+args['group_by']
  
  else:
    search="Select e.id, e.first_name, e.last_name, e.wage, e.rest_id, e.position, e.gender from employee e "
    i=0

    if(args['reserv']!=''):
      search+="join emp_reserv r on e.id=r.emp_id where r.reserv_id="+args['reserv']
      i+=1
    if(i==0):
      search+=" where e.wage between "+args['wage1']+" and "+args['wage2']
    else:
      search+=" and e.wage between "+args['wage1']+" and "+args['wage2']

    if(args['name_sername']!=''):
      search+=" and (e.first_name like \'"+args['name_sername']+"%\' or e.last_name like \'"+args['name_sername']+"%\') "

    if(args['rest']!=''):
      search+=" and e.rest_id="+args['rest']

    if(args['gender']!=''):
      search+=" and e.gender=\'"+args['gender']+"\'"
      
    if(args['position']!=''):
      search+=" and e.position=\'"+args['position']+"\'"
    search+=" order by e."+args['order_by']+";"

 
  print(search)
  mycursor.execute(search)
  result=getresult(mycursor)
  print(result)
  return result

# def insert(table, keys, values):
#   sqlinsert="insert into "+table+" ("
#   for i in range(0, len(keys)):
#     sqlinsert+=keys[i]
#     if(i!=len(keys)-1):
#       sqlinsert+=", "
#     else:
#       sqlinsert+=") "
#   sqlinsert+="("
#   for i in range(0,len(values)):
#     sqlinsert+="\'"+values[i]+"\'"
#     if(i!=len(keys)-1):
#       sqlinsert+=", "
#     else:
#       sqlinsert+=");"

#   print(sqlinsert)
def delete_employee(table, id_value):
  sql_del1="Delete from emp_reserv where emp_id="+id_value+";"
  sqlDelete="Delete from employee where id="+id_value+";"
  mycursor.execute(sql_del1)
  mycursor.execute(sqlDelete)
  # mycursor.execute()
  print(sqlDelete)
  

  

# mycursor.execute("CREATE TABLE gregs_list (last_name VARCHAR(20) NOT NULL, first_name varchar(20) NOT NULL, gender char(1) NOT NULL, email varchar(100) NOT NULL, phone char(10) NOT NULL, birthday date NOT NULL, profession varchar(20) NOT NULL, location varchar(20) NOT NULL, interests varchar(100) NOT NULL, status varchar(10) NOT NULL)")
# sqlinsert="Insert Into gregs_list Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# values=[
#   ('Quill', 'Peter', 'M', 'quillPeter@list.com', '0508765234','1989-06-13','Teacher', 'New-York, NY', 'books, art, animals', 'married'),
#   ('Grant', 'Emma', 'F', 'grantEmma@list.com', '0509876781', '1995-07-27', 'Actor','Texas, TX', 'animals, music, sport', 'free'),
#   ('Williams', 'John', 'M', 'williamsJohn@list.com', '0504567123','1993-09-17', 'Programmer', 'Chicago, CH','sport, programming, coffee', 'free'),
#   ('Hamilton','Caroline', 'F', 'hamiltonCaroline@list.com', '0502387123', '1992-08-05', 'Doctor', 'Los-Angeles, LA', 'books, cooking, horses', 'married')
# ]
# mycursor.executemany(sqlinsert,values)

# mycursor.execute("DELETE FROM reservation")

# mycursor.execute("CREATE TABLE zip (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, city varchar(40) NOT NULL, state char(2) NOT NULL);")
# mycursor.execute("CREATE TABLE restaurant (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, zip INT, capacity INT NOT NULL, FOREIGN KEY(zip) REFERENCES zip(id));")
# mycursor.execute("CREATE TABLE meal (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, price DECIMAL(2,2), prep_time TIME);")
# mycursor.execute("CREATE TABLE meal_rest (rest_id INT, meal_id INT, FOREIGN KEY(rest_id) REFERENCES restaurant(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
# mycursor.execute("CREATE TABLE cheque (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, rest_id INT, meal_id INT, amount INT, date DATETIME, FOREIGN KEY(rest_id) REFERENCES restaurant(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
# mycursor.execute("CREATE TABLE supplier (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, title VARCHAR(30), phone CHAR(13), e_mail VARCHAR(40));")
# mycursor.execute("CREATE TABLE product (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, price DECIMAL(2,2), supp_id INT, FOREIGN KEY(supp_id) REFERENCES supplier(id));")
# mycursor.execute("CREATE TABLE meal_product (meal_id INT, prod_id INT, FOREIGN KEY(prod_id) REFERENCES product(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
# mycursor.execute("CREATE TABLE reservation (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, rest_id INT, date_start DATETIME, date_end DATETIME, visitors INT, FOREIGN KEY(rest_id) REFERENCES restaurant(id));")
# mycursor.execute("CREATE TABLE meal_reserv (reserv_id INT, meal_id INT, FOREIGN KEY(reserv_id) REFERENCES reservation(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
# mycursor.execute("CREATE TABLE employee (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, rest_id INT, first_name VARCHAR(20) NOT NULL, last_name VARCHAR(20) NOT NULL, gender char(1) NOT NULL, birthdate DATE NOT NULL, phone char(13) NOT NULL, e_mail varchar(50) NOT NULL, position varchar(30) NOT NULL, wage INT, FOREIGN KEY(rest_id) REFERENCES restaurant(id));")
# mycursor.execute("CREATE TABLE emp_reserv (reserv_id INT, emp_id INT, FOREIGN KEY(reserv_id) REFERENCES reservation(id), FOREIGN KEY(emp_id) REFERENCES employee(id));")

# sqlinsert="INSERT INTO zip (id, city, state) VALUES(%s, %s, %s)"
# values=[
#   (1,'Los Angeles', 'CA'),
#   (2,'Miami', 'FL'),
#   (3,'New York', 'NY'),
#   (4,'Washington', 'DC'),
#   (5,'Boston', 'MA'),
#   (6,'Chicago', 'IL')
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from zip')
# printresult(mycursor)
# mydb.commit()

# sqlinsert="INSERT INTO restaurant (id, zip, capacity) VALUES(%s, %s, %s)"
# values=[
#   (1, 2, 50),
#   (2, 1, 76),
#   (3, 3, 20),
#   (4, 1, 90),
#   (5, 1, 35),
#   (6, 3, 40),
#   (7, 3, 20),
#   (8, 2, 70),
#   (9, 1, 20)
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from restaurant')
# printresult(mycursor)
# mydb.commit()

# sqlinsert="INSERT INTO employee (rest_id, first_name, last_name, gender, birthdate, phone, e_mail, position, wage) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# values=[
#   (1, 'Peter', 'Quill', 'M', '1989-06-13', '+420508765234', 'quillPeter@list.com','manager', '1100'),
#   (1, 'Julia', 'Williams', 'W', '1990-07-10', '+420508778123', 'williamsJulia@list.com','waiter', '876'),
#   (1, 'Anna', 'Sormantes', 'W', '1981-12-13', '+420501235234', 'sormAnna@list.com','chef', '1050'),
#   (1, 'Antony', 'Lirk', 'M', '1979-09-23', '+420668765234', 'lirkAntony@list.com','cooker', '925'),
#   (2, 'Loren', 'Adrian', 'W', '1992-02-08', '+428798765234', 'adrianLoren@list.com','manager', '1200'),
#   (2, 'John', 'Dreque', 'M', '1991-06-24', '+420508980234', 'drequeJohn@list.com','waiter', '930'),
#   (2, 'Sebstian', 'Firts', 'M', '1986-06-21', '+420545665234', 'firtsSeb@list.com','chef', '1175'),
#   (4, 'Klara', 'Minor', 'W', '1987-11-09', '+420508744434', 'minorKlara@list.com','manager', '1010'),
#   (4, 'Chris', 'Ferns', 'M', '1993-03-30', '+420508789034', 'fernsChris@list.com','chef', '980'),
#   (4, 'Scarlett', 'Evans', 'W', '1990-08-24', '+420324765234', 'evansScar@list.com','waiter', '840'),
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from employee')
# printresult(mycursor)
# mydb.commit()

# sqlinsert="INSERT INTO reservation (id, rest_id, date_start, date_end, visitors) VALUES(%s, %s, %s, %s, %s)"
# values=[
#   (1,1, '2020-03-08 17:00:00', '2020-03-08 21:00:00', 20),
#   (2,1, '2020-03-09 17:00:00', '2020-03-09 21:00:00', 30),
#   (3,1, '2020-02-17 17:00:00', '2020-02-17 22:30:00', 20),
#   (4,2, '2020-03-08 17:00:00', '2020-03-08 23:00:00', 70),
#   (5,2, '2020-03-10 14:00:00', '2020-03-10 18:00:00', 60),
#   (6,2, '2020-03-11 17:00:00', '2020-03-11 20:00:00', 65),
#   (7,4, '2020-03-08 12:00:00', '2020-03-08 16:00:00', 20),
#   (8,4, '2020-03-19 16:00:00', '2020-03-19 19:00:00', 50),
#   (9,4, '2020-02-28 13:00:00', '2020-02-28 18:00:00', 20),
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from reservation')
# printresult(mycursor)
# mydb.commit()

# sqlinsert="INSERT INTO emp_reserv VALUES(%s, %s)"
# values=[
#   (1,1),
#   (1,2),
#   (1,3),
#   (1,4),
#   (2,5),
#   (2,6),
#   (2,7),
#   (3,8),
#   (4,9),
#   (5,10)
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from emp_reserv')
# printresult(mycursor)
# mydb.commit()

# mycursor.execute('Show Tables')
# printresult(mycursor)
# mycursor.execute('desc Zip_code')




