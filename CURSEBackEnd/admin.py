#Admin Class was done by Hank Pham

try:
    from user import user
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CURSEBackEnd.user import user

class admin(user):
    def __init__(self, firstName, lastName, IDnumber):
        super().__init__(firstName, lastName, IDnumber)
        

    def addNewCourse(self, courseName,  department = "TBA", instructor = "TBA", time = 0, day = "TBA", semester = "TBA", year = 0, credits = 0):
        """Add new course to database"""

        self.lastID = 30001 + int(self.sql.get_last_rowID("COURSE"))
        self.CRN = "000" + str(self.lastID)
        self.value = f"'{self.CRN}', '{courseName}', '{department}', '{instructor}', {time}, '{semester}', '{day}', {year}, {credits}"
        self.sql.insert_into_table_values("COURSE", self.value)

    def removeCourseByCRN(self,CRN):
        """Remove course by CRN in COURSE table"""
        CRN = f"'{CRN}'"
        self.sql.delete_from_table_where("COURSE", "CRN", CRN) 

    def removeCourseByName(self,name):
        """Remove course by name in COURSE table"""
        name = f"'{name}'"
        self.sql.delete_from_table_where("COURSE", "TITLE", name) 

    def addNewStudent(self, firstName, lastName, graduation, major = "TBA"):
        """Add new student to STUDENT table"""

        self.lastID = 10001 + int(self.sql.get_last_rowID()) 
        self.studentID = str(self.lastID)
        self.email = ""
        self.value = f"{self.studentID}, '{firstName}', '{lastName}', {graduation}, '{major}', '{self.email}'"
        self.sql.insert_into_table_values("STUDENT", self.value)
        

    # TODO below

    def removeStudentByID(self, id):
        """"Remove a student from STUDENT, ROSTER tables by matching ID """

        print(id + " removed")

    def removeProfessorByID(self, id):
        """Remove a professor from PROFESSOR and COURSE table"""

        print(id + " removed")

    def addStudentToCourse(self, id, CRNcode): 
        """Add Student ID along with Course ID to ROSTER table"""

        print("Student " + id + " added to course " + CRNcode)

    def removeStudentFromCourse(self, id, CRNcode):
        """Remove the Student ID and CRN code from the Roster table"""

        print("Student " + id + " removed from course " + CRNcode)

    def getAllUser(self):
        """Return a list of all user"""
        
        print("Print all users")

    # Incomplete function
    def addNewCourseByInput(self):
        """Prompt user inputs to add new course"""

        print("Enter the course info to add new course:")
        print("Course name:")
        courseName = input()
        print("CRN code:")
        CRNcode = input()
        print(courseName + " (" + CRNcode + ") has been successfully added.")
