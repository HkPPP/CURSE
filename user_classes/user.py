class user:
    def __init__(self, firstName, lastName, IDnumber):
         self.firstName = firstName
         self.lastName = lastName
         self.ID = IDnumber

    def searchCourseByCRN(self, CRN):
        print(CRN + " found")
    
    def searchCourseByName(self, name):
        print(name + " found")







