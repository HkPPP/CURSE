#User Class was done by Kevin Huang

from sql_class import sql_functions

class user:
    
    def __init__(self, firstName, lastName, IDnumber):
        """set attributes and initialize database connection """
        
        self.firstName = firstName
        self.lastName = lastName
        self.ID = IDnumber

        self.sql = sql_functions()


    def searchAllCourse(self):
        """Print out all courses"""

        return self.sql.select_from("COURSE", "*")

    def searchCourseByCRN(self, CRN):
        """Search courses by CRN by selecting CRN column of COURSE table"""

        return self.sql.select_from_where("COURSE", "*", "CRN", str(CRN))
    
    def searchCourseByName(self, name):
        """Search courses by name by selecting TITLE column of COURSE table"""

        return self.sql.select_from_where("COURSE", "*", "TITLE", str(name))
    
    def searchCoursebyYear(self, year):
        """Search courses by year by selecting YEAR column of COURSE table"""

        return self.sql.select_from_where("COURSE", "*", "YEAR", str(year))

    def searchCoursebySem(self, sem):
        """Search courses by semester by selecting SEMESTER column of COURSE table"""

        return self.sql.select_from_where("COURSE", "*", "SEMESTER", str(sem))

    def searchCoursebyDept(self, dept):
        """Search courses by dept by selecting DEPARTMENT column of COURSE table"""

        return self.sql.select_from_where("COURSE", "*", "DEPARTMENT", str(dept))






