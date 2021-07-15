from user_classes.admin import admin
from user_classes.instructor import instructor
from user_classes.student import student
from userLogin import userLogin

def main():
    logIn = userLogin()
    logIn.selectUserType()
    logIn.credentialsInput()

    cred = logIn.getCredentials()

    if cred['utype'] == 'admin':
        user = admin(cred['fname'], cred['lname'], cred['ID'])
    elif cred['utype'] == 'instructor':
        user = instructor(cred['fname'], cred['lname'], cred['ID'])
    elif cred['utype'] == 'student':
        user = student(cred['fname'], cred['lname'], cred['ID'])
    else:
        print("A problem has occur. Cannot create user...")

        main()      # Restart the program


if __name__ == "__main__":
    main()