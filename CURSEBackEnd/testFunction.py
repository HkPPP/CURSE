from admin import admin
from instructor import instructor
from student import student
from sql_class import sql_functions




def main():
    sql = sql_functions()

    
    query_result = sql.select_from_where('student', 'ID, NAME, SURNAME', 'ID', '10001')
    print(query_result[0][2])
    print(len(query_result))


if __name__ == "__main__":
    main()





# def main():
#     print("Testing admin class")
#     adm = admin("admin", "admin", "999")
#     adm.addNewCourseInput()
#     adm.addNewCourse("Math", "1223")
#     adm.searchCourseByCRN("1212")
#     adm.searchCourseByName("Math")
#     adm.removeCourseByCRN("34523")
#     adm.removeCourseByName("Physics")
#     adm.printAllCourses()
#     adm.addUser("Hank", "Pham", "W0121")
#     adm.removeUserByID("W021321")
#     adm.addStudentToCourse("W3213", "Math")
#     adm.addStudentToRoster("W21312", "Team Blue")
#     adm.removeStudentFromRoster("W12123", "Team Red")
#     adm.printAllUser()

#     print("\nTesting instructor class")
#     inst = instructor("Bruce", "Decker", "W2131245132")
#     inst.searchCourseByCRN("1212")
#     inst.searchCourseByName("Math")
#     inst.printSchedule()
#     inst.printRoster()
    
#     print("\nTesting student class")
#     stu = student("Hank","Pham","W021323")
#     stu.searchCourseByCRN("1212")
#     stu.searchCourseByName("Math")
#     stu.registerCourseByCRN("213123")
#     stu.registerCourseByName("Psychology")
#     stu.dropCourseByCRN("21412")
#     stu.dropCourseByName("Music")
#     stu.printSchedule()
