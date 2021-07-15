import sqlite3

# login = login() # ask for name and ID
#                 # save user type, firstname, lastname, IDnumber

# info = login.get_info() # return as an dictionary
# if info["user_type"] == "admin":
#     user = admin(info["firstname"], ...)

# elif info["user_type"] == "student":
#     user = student(info...)
# else:
#     user = instructor(info....)

class userLogin():
    def __init__(self) -> None:

        self.cred = {
            'utype': 'Invalid',
            'lname': 'Invalid',
            'fname': 'Invalid',
            'ID': 'Invalid'
        }
        print(self.cred)

    def getCredentials(self)->dict:
        return self.cred

    def selectUserType(self):
        utype_found = False
        choice = ""
        msg = """Please enter:
        1 if you are an ADMIN
        2 if you are an INSTRUCTOR
        3 if you are a STUDENT
        quit to exit program"""
        print(msg)
        while(utype_found is False):
            choice = input("Enter here: ")
            confirmed = input("Please confirm your answer\n 1 for YES, 2 for NO\n=> ")
            if confirmed == "1":
                utype_found = True
            else:
                continue
        
        choice = choice.lower()
        if choice == "1":
            self.cred['utype'] = 'admin'
        elif choice == "2":
            self.cred['utype'] = 'instructor'
        elif choice == "3":
            self.cred['utype'] = 'student'
        elif choice == "quit":
            quit()
        else:
            print("Invalid inputs...")
            print("\n\n******************************************")
            self.selectUserType()

    def credentialsInput(self):
        user_found = False
        while(user_found is False):
            self.cred['lname'] = input("Please enter your LAST name: ")
            self.cred['ID'] = input("Please enter your ID: ")            
            if self.cred['lname'] == "quit" or self.cred['ID'] == "quit":
                quit()

            confirmed = input("Please confirm your answer\n 1 for YES, 2 for NO\n=> ")
            if confirmed == "1":
                user_found = True
            else:
                continue


    def checkUser(self) -> bool:
        # Connect to database. Return False if fails
        try:    
            database = sqlite3.connect("schooldatabase.db") 
        except Exception:
            print("Cannot find database")
            return False

        try:
            cursor = database.cursor() 
        finally:
            database.close()
        
