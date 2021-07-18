from user import user

class admin(user):
    def __init__(self, firstName, lastName, IDnumber):
        super().__init__(firstName, lastName, IDnumber)
        
    def addNewCourseInput(self):
        print("Enter the course info to add new course:")
        print("Course name:")
        courseName = input()
        print("CRN code:")
        CRNcode = input()
        print(courseName + " (" + CRNcode + ") has been successfully added.")

    def addNewCourse(self, courseName, CRNcode):
        print("Course " + courseName + " (" + CRNcode + ") added.") 
        
    def removeCourseByCRN(self,CRN):
        print(CRN + " removed")

    def removeCourseByName(self,name):
        print(name + " removed")

    def printAllCourses(self):
        print("Print all courses")

    def addUser(self,firstName, lastName, id):
        print(firstName + " " + lastName + " (" + id +") added.")

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