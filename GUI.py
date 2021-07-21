from os import add_dll_directory
from guizero import App, Text, TextBox, PushButton, Window

#Main window
app = App(title="CURSE", height =500, width =500, visible=True, layout="grid")
#Student window
student = Window(title="Login", height=500, width=500, master=app)
student.hide()
#Student function window
student1 = Window(title="Student Page", height=500, width=500, master=app)
student1.hide()
#instructor window
instructor = Window(title="Login", height=500, width=500, master=app)
instructor.hide()
#instructor function window
instructor1 = Window(title="Instructor Page", height=500, width=500, master=app)
instructor1.hide()
#admin window
admin = Window(title="Login", height=500, width=500, master=app)
admin.hide()
#admin function window
admin1 = Window(title="Admin Page", height=500, width=500, master=app)
admin1.hide()

#Exit Button
def exit_btn():
    app.visible = False
#Student Button
def stud_btn():
    app.visible = False
    student.show()
#Instructor Button
def inst_btn():
    app.visible = False
    instructor.show()
#Admin Button
def admin_btn():
    app.visible = False
    admin.show()    

#student login button
def stud_login():
    student1.show()
#instructor login button
def ins_login():
    instructor1.show()
#admin login button
def adm_login():
    admin1.show()

#Main page button
def main_btn():
    student.hide()
    instructor.hide()
    admin.hide()
    student1.hide()
    instructor1.hide()
    admin1.hide()
    app.show()

#first window widgets
title = Text(app, text="\n\n\n   Welcome to CURSE Registration System", size=20, font="Times New Roman", grid=[0,0], align="top")
title_2 = Text(app, text="Select an option\n", size=14, font="Times New Roman", grid=[0,1])
student_button = PushButton(app, command=stud_btn,text="Student",grid=[0,2], width=10)
instructor_button = PushButton(app, command=inst_btn,text="Instructor",grid=[0,3], width=10)
admin_button = PushButton(app, command=admin_btn,text="Admin",grid=[0,4], width=10)
txt = Text(app, text=" ",size=14, font="Times New Roman", grid=[0,5])
exit_button = PushButton(app, command=exit_btn, text="Exit", grid=[0,6])

#Student login window widgets
txt = Text(student, text="Username:",size=14, font="Times New Roman")
txtbox = TextBox(student, width=15)
txt3 = Text(student, text="Password:",size=14, font="Times New Roman")
txtbox2 = TextBox(student, width=15)
submit1 = PushButton(student, command=stud_login, text="Enter")
txt = Text(student, text=" ",size=14, font="Times New Roman")
main = PushButton(student, command=main_btn, text="Main Page")


#Instructor login window widgets
txt = Text(instructor, text="Username:",size=14, font="Times New Roman")
txtbox = TextBox(instructor, width=15)
txt3 = Text(instructor, text="Password:",size=14, font="Times New Roman")
txtbox2 = TextBox(instructor, width=15)
submit2 = PushButton(instructor, command=ins_login, text="Enter")
txt = Text(instructor, text=" ",size=14, font="Times New Roman")
main = PushButton(instructor, command=main_btn, text="Main Page")


#Admin login window widgets
txt = Text(admin, text="Username:",size=14, font="Times New Roman")
txtbox = TextBox(admin, width=15)
txt3 = Text(admin, text="Password:",size=14, font="Times New Roman")
txtbox2 = TextBox(admin, width=15)
submit3 = PushButton(admin, command=adm_login, text="Enter")
txt = Text(admin, text=" ",size=14, font="Times New Roman")
main = PushButton(admin, command=main_btn, text="Main Page")

#student functions
def add_courseName():
    pass
def add_courseCRN():
    pass
def rmv_courseName():
    pass
def rmv_courseCRN():
    pass
def print_sched():
    pass
#student function window widgets
txt = Text(student1, text="Student Page", size=20, font="Times New Roman")
txt = Text(student1, text="\nSelect an option", size=15, font="Times New Roman")
add = PushButton(student1, command=add_courseName, text="Add Course by Name", width=18 )
add1 = PushButton(student1, command=add_courseCRN, text="Add Course by CRN", width=18 )
rmv = PushButton(student1, command=rmv_courseName, text="Remove Course by Name", width=18 )
rmv1 = PushButton(student1, command=rmv_courseCRN, text="Remove Course by CRN", width=18 )
print = PushButton(student1, command=print_sched, text="Print Student Schedule", width=18)
txt = Text(student1, text=" ", size=20, font="Times New Roman")
logout = PushButton(student1, command=main_btn, text="Logout")

#instructor functions





app.display()
