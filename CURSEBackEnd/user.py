#User Class was done by Kevin Huang
try:
    from sql_class import sql_functions
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CURSEBackEnd.sql_class import sql_functions

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
        """Search courses by CRN by looking at CRN column of COURSES table"""
        return self.sql.select_from_where("COURSE", "*", "CRN", str(CRN))
    
    def searchCourseByName(self, name):
        """Search courses by name by looking at TITLE column of COURSES table"""
        return self.sql.select_from_where("COURSE", "*", "TITLE", str(name))
    
    def searchCoursebyYear(self, year):
        """Search courses by year by looking at YEAR column of COURSES table"""
        return self.sql.select_from_where("COURSE", "*", "YEAR", str(year))

    def searchCoursebySem(self, sem):
        """Search courses by semester by looking at SEMESTER column of COURSES table"""
        return self.sql.select_from_where("COURSE", "*", "SEMESTER", str(sem))

    def searchCoursebyDept(self, dept):
        return self.sql.select_from_where("COURSE", "*", "DEPARTMENT", str(dept))






