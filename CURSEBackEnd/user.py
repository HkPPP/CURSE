from sql_class import sql_functions

class user:
    def __init__(self, firstName, lastName, IDnumber):
         self.firstName = firstName
         self.lastName = lastName
         self.ID = IDnumber

         self.sql = sql_functions()

    def searchAllCourse(self):
        return self.sql.select_from("COURSE", "*")

    def searchCourseByCRN(self, CRN):
        return self.sql.select_from_where("COURSE", "*", "CRN", str(CRN))
    
    def searchCourseByName(self, name):
        return self.sql.select_from_where("COURSE", "*", "TITLE", str(name))
    
    def searchCoursebyYear(self, year):
        return self.sql.select_from_where("COURSE", "*", "YEAR", str(year))

    def searchCoursebySem(self, sem):
        return self.sql.select_from_where("COURSE", "*", "SEMESTER", str(sem))

    def searchCoursebyDept(self, dept):
        return self.sql.select_from_where("COURSE", "*", "DEPARTMENT", str(dept))






