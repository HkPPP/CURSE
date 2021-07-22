#Student Class was done by Kevin Huang(50%) and Hank Pham(50%)

from user import user

class student(user):
    def __init__(self, firstName, lastName, IDnumber):
        """initialize parent class"""
        super().__init__(firstName, lastName, IDnumber)
        
    def registerCourseByCRN(self, CRN):
        """adds student ID and CRN to the ROSTER table """

        if len(self.searchCourseByCRN(CRN)) !=0:
            self.value = f"{self.ID}, {CRN}"
            self.sql.insert_into_table_values("ROSTER", self.value)
            return True
        else:
            return False
        
    def dropCourseByCRN(self, CRN):
        """Deletes student ID and CRN from ROSTER table"""

        self.value = f"{CRN} AND StudentID = {self.ID}"
        self.sql.delete_from_table_where("ROSTER", "CRN", self.value)

    def getSchedule(self):
        """Prints out the courses from the COURSE table that have the same CRN as the one from ROSTER table and looks at thr CRN of the student ID entered"""
        
        self.courses = self.sql.select_from_where_in("COURSE", "*", "CRN", "ROSTER", "CRN", "StudentID", self.ID)
        return self.courses
        