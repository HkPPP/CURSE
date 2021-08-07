# from admin import admin
# from instructor import instructor
# from student import student
# from sql_class import sql_functions
# from userLogin import userLogin

def main():
    login = userLogin()

    if login.logIn("student", "10004", "notcool") is False:
        print(False)

    print("User Logged in")

    cred = login.getCredentials()

    if cred['utype'] == 'admin':
        user = admin(cred['fname'], cred['lname'], cred['ID'])
    elif cred['utype'] == 'instructor':
        user = instructor(cred['fname'], cred['lname'], cred['ID'])
    elif cred['utype'] == 'student':
        user = student(cred['fname'], cred['lname'], cred['ID'])
    else:
        print("A problem has occur. Cannot create user...")

        main()      # Restart the program
    
    user.dropCourseByCRN("'00030001'")
    print("Dropped 00030001")
    user.registerCourseByCRN("'00030002'")
    print("Registered 00030002")

    print("Search all course:")
    print(user.searchAllCourse())
    print("\n")

    print("\nSearch based on parameters")
    print(user.searchCourseByCRN("'00030002'"))
    print("\n")
    print(user.searchCoursebyDept("'BSCO'"))
    print("\n")
    print(user.searchCourseByName("'Signals & Systems'"))
    print("\n")
    print(user.searchCoursebySem("'Su'"))
    print("\n")
    print(user.searchCoursebyYear("2021"))


    login.logOut(user)
    print("Logged out")


    
if __name__ == "__main__":
    main()