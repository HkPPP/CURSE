#Instr

from user import user

class instructor(user):
    def __init__(self, firstName, lastName, IDnumber):
        super().__init__(firstName, lastName, IDnumber)
        
    def getSchedule(self):
        print("Print schedule")

    def getRosterFromACourse(self, CRN):
        self.roster = self.sql.select_from_where_in("STUDENT", "*", "ID", "ROSTER", "StudentID", "CRN", CRN)
        return self.roster
        