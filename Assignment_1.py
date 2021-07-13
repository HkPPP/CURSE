class user:
    first = 0
    last = 0
    ID = 0

    def setFirst(self, f):
        self.first = f
    def setLast(self, l):
        self.last = l
    def setID(self, id):
        self.ID = id

    def getFirst(self):
        return self.first
    def getLast(self):
        return self.last
    def getID(self):
        return self.ID
    
    def user(self, f, l, id):
        self.first = f
        self.last = l
        self.ID = id


class Student(user):
    
    def searchCourse():
        pass
    def addCourse():
        pass
    def rmvCourse():
        pass
    def printSched():
        pass

class Instructor(user):
    def printSched():
        pass
    def printRstr():
        pass
    def searchCourse():
        pass


class Admin(user):
    def addCourseToSys():
        pass
    def rmvCourse():
        pass
    def addUser():
        pass
    def rmvUser():
        pass
    def forceOut():
        pass
    def forceIn():
        pass
    def searchSch():
        pass
    def searchRstr():
        pass
    def printSched():
        pass
    def printRstr():
        pass

while True:

    print("\nUser Types")
    print("1. Student")
    print("2. Instructor")
    print("3. Admin")
    print("0. Exit")
    choice = int(input("Select an option:"))

    if choice == 1:
        print("Enter First name, Last name, and ID. ")
        first = input("First name:")
        last = input("Last name:")
        ID = input("ID:")
        print("Student:\nName:", first, " ", last)
        print("ID:W", ID)
        print("-------------------------------")
    elif choice == 2:
        print("Enter First name, Last name, and ID. ")
        first = input("First name:")
        last = input("Last name:")
        ID = input("ID:")
        print("Instructor:\nName:", first, " ", last)
        print("ID:W", ID)
        print("-------------------------------")
    elif choice == 3:
        print("Enter First name, Last name, and ID. ")
        first = input("First name:")
        last = input("Last name:")
        ID = input("ID:")
        print("Admin:\nName:", first, " ", last)
        print("ID:W", ID)
        print("-------------------------------")
    elif choice == 0:
        break
    else:
        print("Invalid input. Please try again.")