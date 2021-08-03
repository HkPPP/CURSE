#Instructor class done by Kevin Huang(50%) and Hank Pham(50%)

try:
    from user import user
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CURSEBackEnd.user import user

class instructor(user):
    def __init__(self, firstName, lastName, IDnumber):
        super().__init__(firstName, lastName, IDnumber)
        
    def getSchedule(self):
        """Get schedule for instructor"""
        courses = self.sql.select_from_where("COURSE", "*", "INSTRUCTOR", self.ID)
        return courses
        

    def getRosterFromACourse(self, CRN):
        """Get Roster from a course"""
        CRN = f"'{CRN}'"
        roster = self.sql.select_from_where_in("STUDENT", "*", "ID", "ROSTER", "StudentID", "CRN", CRN)
        return roster

