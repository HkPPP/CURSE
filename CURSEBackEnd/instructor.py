#Instructor class done by Kevin Huang(50%) and Hank Pham(50%)

from user import user

class instructor(user):
    def __init__(self, firstName, lastName, IDnumber):
        super().__init__(firstName, lastName, IDnumber)
        
    def getSchedule(self):
        """Get schedule for instructor"""
        print("Print schedule")

    def getRosterFromACourse(self, CRN):
        """Get Roster from a course"""
        self.roster = self.sql.select_from_where_in("STUDENT", "*", "ID", "ROSTER", "StudentID", "CRN", CRN)
        return self.roster
        