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
    if(args['order_by']=="wage"):
      search+=" order by sum(wage)"
    elif(args['order_by']=="wage desc"):
      search+=" order by sum(wage) desc"
  
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

def search_supp(args):
  result=["Nothing"]
  if(args==''):
    search= "Select * from supplier"
  else:
    search= "Select * from supplier where title like \'"+args+"%\';"
  print(search)
  mycursor.execute(search)
  result=getresult(mycursor)
  print(result)
  return result

def add_supp(title, phone, email):
  insert="Insert into supplier (title, phone, e_mail) values(\""+title+"\",\""+phone+"\",\""+email+"\");"
  print(insert)
  mycursor.execute(insert)
  mydb.commit()

def delete_employee(table, id_value):
  sql_del1="Delete from emp_reserv where emp_id="+id_value+";"
  sqlDelete="Delete from employee where id="+id_value+";"
  mycursor.execute(sql_del1)
  mycursor.execute(sqlDelete)
  mydb.commit()
  print(sqlDelete)
  
def search_meals(args):
  search="Select * from meal"
  if(args):
    if(args['group_by']!=''):
      if(args['group_by']=='reservation'):
        search="Select r.id, r.visitors, round(avg(m.price),2), round(sum(m.price)*r.visitors,2), DATE_FORMAT(r.date_start, \"%H:%i\"), DATE_FORMAT(r.date_end, \"%H:%i\") from meal m join meal_reserv mr on mr.meal_id=m.id join reservation r on mr.reserv_id=r.id group by mr.reserv_id  order by mr.id"
      else:
        search="Select r.id, r.capacity, round(avg(m.price),2), round(sum(m.price)*r.capacity,2), zc.state from meal m join meal_rest mr on mr.meal_id=m.id join restaurant r on mr.rest_id=r.id join zip zc on r.zip=zc.code group by mr.rest_id order by mr.id"
    else:
      search="Select m.id, m.title, m.price, m.prep_time from meal m "
      if(args["product_in"]!=""):
        search+=" join meal_product p on p.meal_id=m.id where p.prod_id="+args["product_in"]+" and "
      else:
        search+="where "
      search+="m.price between "+args['price_from']+" and "+args['price_to']+" and m.prep_time between time(\""+args['prep_from']+"\") and time(\""+args['prep_to']+"\")"
      if(args['title']!=''):
        search+=" and m.title like \'"+args['title']+"%\'"
      if(args['order_by']!=''):
        search+=" order by "+args['order_by']
      else:
        search+=" order by m.id"
    
  print(search)
  mycursor.execute(search)
  result=getresult(mycursor)
  print(result)
  return result

def delete_meals(id):
  mycursor.execute("Delete from cheque where meal_id="+str(id))
  mycursor.execute("Delete from meal_product where meal_id="+str(id))
  mycursor.execute("Delete from meal_reserv where meal_id="+str(id))
  mycursor.execute("Delete from meal_rest where meal_id="+str(id))
  mycursor.execute("Delete from meal where id="+str(id))
  mydb.commit()

def search_products(args):
  search="select * from product"
  if(args):
    if(args['group_by']!=''):
      if(args['group_by']=='meal'):
        search="select m.id, m.title, round(avg(p.price),2), round(sum(p.price), 2), m.price from meal m join meal_product mp on mp.meal_id=m.id join product p on p.id=mp.prod_id group by mp.meal_id order by mp.id"
      else:
        search="select s.id, s.title, round(avg(p.price),2), round(sum(p.price),2) from supplier s join product p on p.Supp_id=s.id group by s.id order by s.id"
    else:
      search="select p.id, p.title, p.price, p.supp_id from product p "
      if(args["supplier"]!=""):
        search+=" join supplier s on p.supp_id=s.id where s.id="+args["supplier"] + " and "
      else:
        search+="where "
      search+="p.price between "+args['price_from']+" and "+args['price_to']
      if(args['title']!=''):
        search+=" and p.title like \'"+args['title']+"%\'"
      if(args['order_by']==" desc"):
        search+=" order by p.id desc"
      elif(args['order_by']!=''):
        search+=" order by "+args['order_by']
      else:
        search+=" order by p.id"
    
  print(search)
  mycursor.execute(search)
  result=getresult(mycursor)
  print(result)
  return result

def delete_product(id):
  mycursor.execute("delete from meal_product where prod_id="+str(id))
  mycursor.execute("delete from product where id="+str(id))
  mydb.commit()


# mycursor.execute("drop table emp_reserv; drop table meal_rest; drop table meal_product; drop table meal_reserv;")
# mycursor.execute("drop table meal_product;")
# mycursor.execute("drop table meal_reserv")
# mycursor.execute("drop table meal_rest")
# mydb.commit()
# mycursor.execute("drop table product;" )
# mycursor.execute("drop table cheque;" )
# mycursor.execute("drop table meal;") 
# mycursor.execute("drop table product; drop table supplier; drop table cheque; drop table meal;")
# mycursor.execute("drop table reservation; drop table employee; drop table restaurant; drop table zip;")
# mydb.commit()
# mycursor.execute("Show tables")
# print(getresult(mycursor))

# mycursor.execute("CREATE TABLE zip (code varchar(10) NOT NULL PRIMARY KEY, state char(2) NOT NULL);")
# mycursor.execute("CREATE TABLE restaurant (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, zip varchar(10), capacity INT NOT NULL, FOREIGN KEY(zip) REFERENCES zip(code));")
# mycursor.execute("CREATE TABLE meal (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, title varchar(40), price DECIMAL(6,2), prep_time TIME);")
# mycursor.execute("CREATE TABLE meal_rest (id int not null auto_increment primary key, rest_id INT, meal_id INT, FOREIGN KEY(rest_id) REFERENCES restaurant(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
# mycursor.execute("CREATE TABLE cheque (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, rest_id INT, meal_id INT, amount INT, date DATETIME, FOREIGN KEY(rest_id) REFERENCES restaurant(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
# mycursor.execute("CREATE TABLE supplier (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, title VARCHAR(30), phone CHAR(13), e_mail varchar(320));")
# mycursor.execute("CREATE TABLE product (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, title varchar(40), price DECIMAL(6,2), supp_id INT, FOREIGN KEY(supp_id) REFERENCES supplier(id));")
# mycursor.execute("CREATE TABLE meal_product (id int not null auto_increment primary key, meal_id INT, prod_id INT, FOREIGN KEY(prod_id) REFERENCES product(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
# mycursor.execute("CREATE TABLE reservation (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, rest_id INT, date_start DATETIME, date_end DATETIME, visitors INT, FOREIGN KEY(rest_id) REFERENCES restaurant(id));")
# mycursor.execute("CREATE TABLE meal_reserv (id int not null auto_increment primary key, reserv_id INT, meal_id INT, FOREIGN KEY(reserv_id) REFERENCES reservation(id), FOREIGN KEY(meal_id) REFERENCES meal(id));")
# mycursor.execute("CREATE TABLE employee (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, rest_id INT, first_name VARCHAR(20) NOT NULL, last_name VARCHAR(20) NOT NULL, gender char(1) NOT NULL, birthdate DATE NOT NULL, phone char(13) NOT NULL, e_mail varchar(320) NOT NULL, position varchar(30) NOT NULL, wage INT, FOREIGN KEY(rest_id) REFERENCES restaurant(id));")
# mycursor.execute("CREATE TABLE emp_reserv (id int not null auto_increment primary key, reserv_id INT, emp_id INT, FOREIGN KEY(reserv_id) REFERENCES reservation(id), FOREIGN KEY(emp_id) REFERENCES employee(id));")
# mydb.commit()

# sqlinsert="INSERT INTO zip (code, state) VALUES(%s, %s)"
# values=[
#   ('90014', 'CA'),
#   ('33142', 'FL'),
#   ('11416', 'NY'),
#   ('20010', 'DC'),
#   ('02118', 'MA'),
#   ('60608', 'IL')
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from zip')
# printresult(mycursor)
# mydb.commit()

# sqlinsert="INSERT INTO restaurant (id, zip, capacity) VALUES(%s, %s, %s)"
# values=[
#   (1, '33142', 50),
#   (2, '90014', 76),
#   (3, '11416', 20),
#   (4, '90014', 90),
#   (5, '90014', 35),
#   (6, '11416', 40),
#   (7, '11416', 20),
#   (8, '33142', 70),
#   (9, '90014', 20)
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

# sqlinsert="INSERT INTO emp_reserv (reserv_id, emp_id) VALUES(%s, %s)"
# values=[
#   (1,1),
#   (1,2),
#   (1,3),
#   (1,4),
#   (2,5),
#   (2,6),
#   (2,1),
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

# sqlinsert="INSERT INTO supplier (title, phone, e_mail) VALUES(%s, %s, %s)"
# values=[
#   ("Grandpa\'s garden", "+1415908678", "grandpa@supp.com"),
#   ("World of vegetables", "+1415908678", "vegetable@supp.com"),
#   ("Fruits", "+141565478", "fruit@supp.com"),
#   ("Be vegan", "+1415890234", "vegan@supp.com"),
#   ("Meet meat", "+1415123786", "meat@supp.com"),
#   ("Sweet life", "+1415765845", "sweets@supp.com"),
#   ("Seaworld", "+1415234567", "sea@supp.com"),
#   ("Milk way", "+1415987654", "milky@supp.com"),
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from supplier')
# printresult(mycursor)
# mydb.commit()
# mycursor.execute("Delete from meal_product")
# mycursor.execute("Delete from meal")
# mycursor.execute("Delete from product")
# mydb.commit()

# sqlinsert="INSERT INTO meal (id, title, price, prep_time) VALUES(%s, %s, %s, %s)"
# values=[
#   (1,"Greek salad", 4.5, "10"),
#   (2, "Salad \"Caesar\"", 4.25, "13"),
#   (3,"Milkshake", 2.5, "5"),
#   (4,"Pancakes with marple syrup", 3.3, "15"),
#   (5,"Pork stake", 6.0, "30"),
#   (6,"Pizza \"Hawaii\"", 3.5, "20"),
#   (7,"Backed losos", 5.8, "25"),
#   (8,"Coffee", 2.1, "7")
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from meal')
# printresult(mycursor)
# mycursor.execute('Select max(price) from meal')
# printresult(mycursor)
# mydb.commit()

# sqlinsert="INSERT INTO product (id, title, price, supp_id) VALUES(%s, %s, %s, %s)"
# values=[
#   (1,"Milk", 2.0, 8),
#   (2, "Flour", 1.5 ,1),
#   (3, "Salat", 2.5, 2),
#   (4, "Chicken", 3.3, 5),
#   (5, "Pork", 5.0, 5),
#   (6, "Cheese", 3.5, 8),
#   (7, "Losos", 5.8, 7),
#   (8, "Coffee", 3.4, 1),
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from product')

# printresult(mycursor)
# # mycursor.execute('Select max(price) from product')
# # res=getresult(mycursor)
# mydb.commit()

# sqlinsert="INSERT INTO meal_product (prod_id, meal_id) VALUES(%s, %s)"
# values=[
#   (1,3),
#   (1,4),
#   (1,8),
#   (2,4),
#   (2,6),
#   (3,2),
#   (3,1),
#   (4,2),
#   (5,5),
#   (6,6),
#   (7,7),
#   (8,8)
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from meal_product')
# printresult(mycursor)
# mydb.commit()

# sqlinsert="INSERT INTO meal_rest (rest_id, meal_id) VALUES(%s, %s)"
# values=[
#   (1,3),
#   (1,4),
#   (1,8),
#   (2,4),
#   (2,6),
#   (3,2),
#   (3,1),
#   (4,2),
#   (4,7),
#   (4,3),
#   (4,1),
#   (5,5),
#   (5,6),
#   (5,1),
#   (5,3),
#   (6,6),
#   (6,6),
#   (6,6),
#   (6,3),
#   (7,7),
#   (7,4),
#   (7,5),
#   (7,6),
#   (8,8),
#   (8,7),
#   (8,4),
#   (8,3)
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from meal_rest')
# printresult(mycursor)
# mydb.commit()

# sqlinsert="INSERT INTO meal_reserv (reserv_id, meal_id) VALUES(%s, %s)"
# values=[
#   (1,3),
#   (1,4),
#   (1,8),
#   (2,4),
#   (2,6),
#   (3,2),
#   (3,1),
#   (4,2),
#   (4,7),
#   (4,3),
#   (4,1),
#   (5,5),
#   (5,6),
#   (5,1),
#   (5,3),
#   (6,6),
#   (6,6),
#   (6,6),
#   (6,2),
#   (7,7),
#   (7,4),
#   (7,5),
#   (7,6),
#   (8,8),
#   (8,7),
#   (8,4),
#   (8,3)
# ]
# mycursor.executemany(sqlinsert,values)
# mycursor.execute('Select * from meal_reserv')
# printresult(mycursor)
# mydb.commit()

