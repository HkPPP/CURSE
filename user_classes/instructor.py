from user import user

class instructor(user):
    def __init__(self, firstName, lastName, IDnumber):
        super().__init__(firstName, lastName, IDnumber)

    def printSchedule(self):
        print("Print schedule")

    def printRoster(self):
        print("Print all rosters and students in each roster")