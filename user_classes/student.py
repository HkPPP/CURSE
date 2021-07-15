from user import user

class student(user):
    def __init__(self, firstName, lastName, IDnumber):
        super().__init__(firstName, lastName, IDnumber)

    def registerCourseByCRN(self,CRN):
        print(CRN + " registered")

    def registerCourseByName(self, name):
        print(name + " registered")

    def dropCourseByCRN(self,CRN):
        print(CRN + " dropped")

    def dropCourseByName(self, name):
        print(name + " registered")

    def printSchedule(self):
        print("Print schedule")