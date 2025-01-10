import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class


class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self, id):
        sql = "SELECT * FROM student WHERE id=%s"
        param = (id,)
        self.cursor.execute(sql, param)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as e:
            print("Error: ",e)

    def getClasses(self):
        sql = "SELECT * FROM class"
        self.cursor.execute(sql)
        try:
            objs = self.cursor.fetchall()
            return Class.CreateClass(obj=objs)
        except mysql.connector.Error as e:
            print("Error:",e)

    def getStudentsByClassId(self, cid):
        sql = "SELECT * FROM student WHERE classid=%s"
        param = (cid,)
        self.cursor.execute(sql,param)
        try:
            objs = self.cursor.fetchall()
            return Student.CreateStudent(obj=objs)
        except mysql.connector.Error as e:
            print("Error:",e)
            
    
    def addStudent(self, student : Student):
        sql = "INSERT INTO Student(StudentNumber, Name_, Surname, Birthdate, Gender, ClassId) VALUES(%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as e:
            print("Hata:",e)

    def editStudent(self, student : Student):
        sql = "UPDATE student SET StudentNumber=%s, Name_=%s, Surname=%s, Birthdate=%s, Gender=%s, ClassId=%s WHERE id=%s"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as e:
            print("Hata:",e)
    
    def deleteStudent(self, studentid):
        sql = "DELETE FROM student WHERE id = %s"
        value = (studentid,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt silindi.")
        except mysql.connector.Error as e:
            print("Hata:",e)
    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print("db silindi.")

db = DbManager()

student = db.getStudentById(7) 

student[0].name = "Ali"


db.editStudent(student[0]) 

# students = db.getStudentsByClassId(1)
# for s in students:
#     print(s.name)

