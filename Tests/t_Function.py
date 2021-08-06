# from user import user
# from admin import admin
# from instructor import instructor
# from student import student
# from sql_class import sql_functions
# from userLogin import userLogin




def main():
    
    # s = sql_functions()
    # value = "10004, '00030001'"
    # s.insert_into_table_values("ROSTER", value)
    # value = "10005, '00030001'"
    # s.insert_into_table_values("ROSTER", value)
    # value = "10006, '00030001'"
    # s.insert_into_table_values("ROSTER", value)



    # u = instructor("Hank", "Pham","13212")
    # c = u.getRosterFromACourse("'00030001'")

    # for k in c:
    #     print(k)


    p = userLogin()

    



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
