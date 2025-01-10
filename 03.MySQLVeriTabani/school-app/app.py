from dbmenager import DbManager
from Student import Student
import datetime

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Örenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == "1":
                self.displayStudendts()
            elif islem == "2":
                self.addStudents()
            elif islem == "3":
                self.editStudent()
            elif islem == "4":
                self.deleteStudent()
            elif islem == "E" or islem == "Ç":
                break
            else:
                print("Yanlış bir giriş yaptınız!")

    def displayClasses(self):
        classes = self.db.getClasses()

        for i in classes:
            print(f"{i.id}: {i.name}")

    def displayStudendts(self):
        self.displayClasses()
        clasid = int(input('hangi sınıf: '))

        students = self.db.getStudentsByClassId(clasid)

        print("------------------Öğrenci Listesi------------------")
        for student in students:
            print(f"{student.id}.{student.name} {student.surname}")
        
        return clasid

    def addStudents(self):
        self.displayClasses()

        classid = int(input('hangi sınıf: '))
        number = input("Numara: ")
        name = input("Ad: ")
        surname = input("Soyad: ")
        year = int(input("Yıl: "))
        month = int(input("Ay: "))
        day = int(input("Gün: "))
        birthdate = datetime.date(year,month,day)
        gender = input("Cinsiyet (E/K): ")

        student = Student(None, number, name, surname, birthdate, gender, classid)
        self.db.addStudent(student)

    def editStudent(self):
        clasid = self.displayStudendts()
        studentid = int(input("Öğrneci id: "))

        student = self.db.getStudentById(studentid)

        student[0].name = input("name: ") or student[0].name
        student[0].surname = input("surname: ") or student[0].surname
        student[0].gender = input("gender (E/K): ") or student[0].gender
        student[0].classid = input("classid: ") or student[0].classid

        year = input("yıl: ") or student[0].birthdate.year
        month = input("ay: ") or student[0].birthdate.month
        day = input("gün: ") or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)
        self.db.editStudent(student[0])
    
    def deleteStudent(self):
        classid = self.displayStudendts()
        studentid = int(input("Öğrneci id: "))

        self.db.deleteStudent(studentid)





app = App()
app.initApp()