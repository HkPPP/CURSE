#Admin Class was done by Hank Pham
from typing import List

try:
    from user import user
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CURSEBackEnd.user import user

class admin(user):
    def __init__(self, firstName, lastName, IDnumber):
        super().__init__(firstName, lastName, IDnumber)
        
    def getAllStudent(self)->List:
        return self.sql.select_from("STUDENT", "*")
    
    def getAllInstructor(self)->List:
        return self.sql.select_from("INSTRUCTOR", "*")

    def addNewCourse(self, courseName,  department = "TBA", instructor = "TBA", time = 0, day = "TBA", semester = "TBA", year = 0, credits = 0)->None:
        """Add new course to database"""

        lastID = 30001 + int(self.sql.get_last_rowID("COURSE"))
        CRN = "000" + str(lastID)
        value = f"'{CRN}', '{courseName}', '{department}', '{instructor}', {time}, '{semester}', '{day}', {year}, {credits}"
        self.sql.insert_into_table_values("COURSE", value)

    def removeCourseByCRN(self,CRN)->None:
        """Remove course by CRN in COURSE table"""
        CRN = f"'{CRN}'"
        self.sql.delete_from_table_where("COURSE", "CRN", CRN) 

    def removeCourseByName(self,name)->None:
        """Remove course by name in COURSE table"""
        name = f"'{name}'"
        self.sql.delete_from_table_where("COURSE", "TITLE", name) 

    def addNewStudent(self, firstName, lastName, graduation, major = "TBA")->None:
        """Add new student to STUDENT table"""

        student_count = int(self.sql.get_last_rowID("STUDENT"))
        studentID = f"{10001 + student_count}"
        email = self.createNewEmail(firstName, lastName, "STUDENT")
        value = f"{studentID}, '{firstName}', '{lastName}', {graduation}, '{major}', '{email}'"
        self.sql.insert_into_table_values("STUDENT", value)
        
    def addNewInstructor(self, first, last, hire_year, title="TBA", dept="TBA")->None:
        """Add new instructor to INSTRUCTOR table"""

        ins_count = int(self.sql.get_last_rowID("INSTRUCTOR"))
        insID = f"{20001 + ins_count}"
        email = self.createNewEmail(first, last, "INSTRUCTOR")
        value = f"{insID}, '{first}', '{last}', '{title}', {hire_year}, '{dept}', '{email}'"
        self.sql.insert_into_table_values("INSTRUCTOR", value)

    def removeStudentByID(self, id)->None:
        """"Remove a student from STUDENT, ROSTER tables by matching ID """

        self.sql.delete_from_table_where("STUDENT", "ID", id) 
        self.sql.delete_from_table_where("ROSTER", "StudentID", id)
    
    def removeProfessorByID(self, id)->None:
        """Remove a professor from INSTRUCTOR and COURSE tables"""

        self.sql.delete_from_table_where("INSTRUCTOR", "ID", id)
        new_info = f"INSTRUCTOR = 20000"
        condt = f"INSTRUCTOR = {id}"
        self.sql.update_set_where("COURSE", new_info, condt)


    def createNewEmail(self, firstName, lastName, table) -> str:
        """Create a new email in the format 'lastf0'"""

        last_and_first_init = f"{lastName.lower()}{firstName[0:1].lower()}"
        condt = f"'{last_and_first_init}%'"
        email_index = len(self.sql.get_partial_matches(table, "EMAIL","EMAIL",condt))
        email =f"{last_and_first_init}{email_index}"
        return email

 


    # TODO below
    

    
    def addStudentToCourse(self, id, CRNcode): 
        """Add Student ID along with Course ID to ROSTER table"""

        print("Student " + id + " added to course " + CRNcode)

    def removeStudentFromCourse(self, id, CRNcode):
        """Remove the Student ID and CRN code from the Roster table"""

        print("Student " + id + " removed from course " + CRNcode)



def main():
    # ad = admin("Barack","Obama","30001")
    # ad.addNewStudent("Issac","Newton",1668,"BSAS")
    pass

if __name__=="__main__":
    main()