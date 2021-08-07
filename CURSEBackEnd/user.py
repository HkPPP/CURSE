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
        """Search courses by CRN by selecting CRN column of COURSE table"""

        return self.sql.select_from_where("COURSE", "*", "CRN", self.single_quote_around_str(CRN))
    
    def searchCourseByName(self, name):
        """Search courses by name by selecting TITLE column of COURSE table"""

        return self.sql.select_from_where("COURSE", "*", "TITLE", self.single_quote_around_str(name))
    
    def searchCoursebyYear(self, year):
        """Search courses by year by selecting YEAR column of COURSE table"""

        return self.sql.select_from_where("COURSE", "*", "YEAR", self.single_quote_around_str(year))

    def searchCoursebySem(self, sem):
        """Search courses by semester by selecting SEMESTER column of COURSE table"""

        return self.sql.select_from_where("COURSE", "*", "SEMESTER", self.single_quote_around_str(sem))

    def searchCoursebyDept(self, dept):
        """Search courses by dept by selecting DEPARTMENT column of COURSE table"""

        return self.sql.select_from_where("COURSE", "*", "DEPARTMENT", self.single_quote_around_str(dept))

    @staticmethod
    def single_quote_around_str(string):
        return f"'{string}'"




