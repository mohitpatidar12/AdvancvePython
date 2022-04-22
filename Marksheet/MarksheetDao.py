import MarksheetBean
from MarksheetBean import *
mb = MarksheetBean()
import pymysql

class MarksheetDao():
    def nextPK(self):
        r = 0
        connection = pymysql.Connect(host="localhost",user="root",password="root",db="mohit")
        with connection.cursor() as cursor:
            sql = "select max(roll_no) from  marksheet "
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.commit()
        connection.close()
        for e in result:
            r = e[0]
            return r+1


    def Add(self,mb):
        pk = MarksheetDao.nextPK(mb)
        connection = pymysql.Connect(host="localhost",user="root",password="root",db="mohit")
        with connection.cursor() as cursor:
            sql = "insert into marksheet values(%s,%s,%s,%s,%s)"
            data = (pk,mb.getName(),mb.getPhysics(),mb.getChemistry(),mb.getMaths())
            cursor.execute(sql, args=data)
            connection.commit()
        connection.close()

    def Delete(self,mb ):
        connection = pymysql.connect(host="localhost",user="root",password="root",db="mohit")
        with connection.cursor() as cursor:
            sql = "Delete from marksheet where roll_no = %s"
            data= (mb.getRollNo())
            cursor.execute(sql, args=data)
            connection.commit()
        connection.close()


    def update(self,mb):
        connection = pymysql.connect(host="localhost", user="root", password="root", db="mohit")
        with connection.cursor() as cursor:
            sql= "update marksheet set name = %s, physics=%s, chemistry=%s , maths=%s where roll_no =%s"
            data=(mb.getName(),mb.getPhysics(),mb.getChemistry(),mb.getMaths(),mb.getRollNo())
            cursor.execute(sql, args=data)
            connection.commit()
        connection.close()


    def search(self):
        connection = pymysql.connect(host="localhost", user="root", password="root", db="mohit")
        with connection.cursor() as cursor:
            sql= "select * from marksheet"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.commit()
        connection.close()
        for e in result:
            print(e[0],e[1],e[2],e[3],e[4])

    def search_single(self,mb):
        result=""
        connection = pymysql.connect(host="localhost", user="root", password="root", db="mohit")
        with connection.cursor() as cursor:
            sql= "select * from marksheet where roll_no =%s"
            data=(mb.getRollNo(),mb.getName(),mb.getPhysics(),mb.getChemistry(),mb.getMaths())
            cursor.execute(sql,data)
            result = cursor.fetch()
            connection.commit()
        connection.close()


