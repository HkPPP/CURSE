# Written by Hank

from user import user
from sql_class import sql_functions

class userLogin():
    def __init__(self) -> None:
        self.sql = sql_functions()
        self.__cred = {
            'utype': 'Invalid',
            'lname': 'Invalid',
            'fname': 'Invalid',
            'ID': 'Invalid'
        }

    def getCredentials(self)->dict:
        """Return credentials as a Dict"""
        return self.__cred


    def logIn(self, utype, ID, email):
        """Fill out credentials and return True if ID and last name are found in DB. Otherwise, return False"""

        query_result = self.sql.select_from_where(utype, 'ID, SURNAME, NAME, EMAIL', 'ID', ID)

        if len(query_result == 0):
            return False
        else:
            if  email == query_result[0][3]:
                self.__cred['utype'] = str(utype)
                self.__cred['ID'] = query_result[0][0]
                self.__cred['lname'] = query_result[0][1]
                self.__cred['fname'] = query_result[0][2]
                return True
            else:
                return False

    def logOut(self, u):
        """Delete object if object is a User type"""

        if isinstance(u, user):
            del u

    def selectUserType_Input(self):
        """Manually fill in user type with terminal prompts"""

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

    def credentials_Input(self):
        """Manually fill in last name and ID with terminal prompts"""

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


    def checkUser_Input(self) -> bool:
        """REQUIRED PREFILLED ID AND UTYPE (Call 'selectUserType_Input' and 'credentials_Input' first). Return True if last name and ID found. Otherwise, return False"""

        if self.__cred['utype'] == 'Invalid':
            return False
        else:
            query_result = self.sql.select_from_where(self.__cred['utype'], 'ID, SURNAME, NAME', 'ID', self.__cred['ID'])
            if len(query_result == 0):
                return False
            else:
                if self.__cred['utype'] == query_result[0][0] and self.__cred['lname'] == query_result[0][1]:
                    self.__cred['fname'] = query_result[0][3]
                    return True
                else:
                    return False

