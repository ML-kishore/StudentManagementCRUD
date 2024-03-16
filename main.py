from tabulate import tabulate
import mysql.connector

conn = mysql.connector.connect(host= "localhost",user="root",password="yourpassword",database = "studdb")

def insert(name,age,class_name,city):
    res = conn.cursor()
    sql = "insert into studentrecord (stud_name,age,class,city) values (%s,%s,%s,%s)"
    student = (name,age,class_name,city)
    res.execute(sql,student)
    conn.commit()
    print("Data inserted Successfully")
def update(name,age,class_name,city,id):
    res = conn.cursor()
    sql = "update studentrecord  set stud_name=%s,age=%s,class=%s,city=%s where stud_id = %s"
    student = (name, age, class_name, city,id)
    res.execute(sql, student)
    conn.commit()
    print("Data Updated Successfully")

def select():
    res = conn.cursor()
    sql = "SELECT STUD_ID,STUD_NAME ,AGE,CLASS,CITY from studentrecord"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CLASS","CITY"]))


def delete(id):
    res = conn.cursor()
    sql = "delete from studentrecord where stud_id = %s"
    student = (id,)
    res.execute(sql,student)
    conn.commit()
    print("Deleted Data Sucessfully")

while True:
    print("1.insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        name = input("enter your name")
        age = int(input("enter your name"))
        class_name = int(input("enter your name"))
        city = input("enter your name")
        insert(name, age, class_name, city)
    elif choice == 2:
        id= int(input("enter the id to update"))
        name = input("enter your name")
        age = int(input("enter your age"))
        class_name = int(input("enter your class"))
        city = input("enter your city")
        update(name, age, class_name, city, id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = int(input('Enter the ID to delete'))
        delete(id)
    elif choice==5:
        quit()
    else:
        print("invalid option please Try Again")
