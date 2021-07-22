#Admin Class was done by Hank Pham

from user import user
from sql_class import sql_functions

class admin(user):
    def __init__(self, firstName, lastName, IDnumber):
        super().__init__(firstName, lastName, IDnumber)
        
        
    def addNewCourseByInput(self):
        print("Enter the course info to add new course:")
        print("Course name:")
        courseName = input()
        print("CRN code:")
        CRNcode = input()
        print(courseName + " (" + CRNcode + ") has been successfully added.")

    def addNewCourse(self, courseName,  department = "TBA", instructor = "TBA", time = 0, semester = "TBA", year = 0, credits = 0):
        self.lastID = 30001 + int(self.sql.get_last_rowID())
        self.CRN = "000" + str(self.lastID)
        self.value = f"{self.CRN}, {courseName}, {department}, {instructor}, {time}, {semester}, {year}, {credits}"
        self.sql.insert_into_table_values("COURSE", self.value)


    def removeCourseByCRN(self,CRN):
        self.sql.delete_from_table_where("COURSE", "CRN", CRN) 

    def removeCourseByName(self,name):
        self.sql.delete_from_table_where("COURSE", "CRN", name) 

    def printAllCourses(self):
        courses = self.sql.select_from("COURSE", "*")
        for course in courses:
            print(course)
        
    def addUser(self, firstName, lastName, graduation, major = "TBA"):
        self.lastID = 10001 + int(self.sql.get_last_rowID()) 
        self.studentID = str(self.lastID)
        self.email = ""
        self.value = f"{self.studentID}, {firstName}, {lastName}, {graduation}, {major}, {self.email}"
        self.sql.insert_into_table_values("STUDENT", self.value)
        

    def removeUserByID(self, id):
        print(id + " removed")

    def addStudentToCourse(self, id, CRNcode):  
        print("Student " + id + " added to course " + CRNcode)

    def removeStudentFromCourse(self, id, CRNcode):
        print("Student " + id + " removed from course " + CRNcode)

    def addStudentToRoster(self, id, roster):
        print("Student " + id + " added to roster " + roster)

    def removeStudentFromRoster(self, id, roster):
        print("Student " + id + " removed from roster " + roster)

    def printAllUser(self):
        print("Print all users")