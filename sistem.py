import os
import mysql.connector

myconn = mysql.connector.connect(user='root', password='',
                                 host='127.0.0.1',
                                 database='pasien')
cur = myconn.cursor() 
sql = ("INSERT INTO pasien (name, umur )"
"VALUES (%s,%s)")



# dbs = cur.execute("show databases") 

# for x in cur:  
#         print(x) 
print("+------------------------------------------------+")
print("|\tSelamat Datang di Alfador |")
print("|\tbelanja murah dan terjangkau         |")
print("+------------------------------------------------+")
pilihan = str(input("Hallo ,\nApakah anda ingin belanja ? (y/n)"))




while pilihan =="y" :
    nik = (str(input("NIK\t:  ")))
    nama = (str(input("Nama\t: ")))
    umur = (str(input("Umur\t: ")))
    gender = (str(input("gender\t: ")))
    try:
        cur.execute(sql,(nama,umur,))
        myconn.commit()
    except:
        myconn.rollback()
    os.system("cls")
    pilihan = str(input("Hallo , \nApakah anda ingin belanja lagi ? (y/n)"))


print(cur.rowcount, "record inserted!")
myconn.close()

print("+----------------------- Terima Kasih ------------------------+")
