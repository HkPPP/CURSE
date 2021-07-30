from tkinter import *
from tkinter import ttk
import sqlite3


#gui class
class MainApp:

    #initialize
    def __init__(self):
        
        #Main App Window
        self.main = Tk()
        self.main.title("CURSE")
        self.main.configure(bg="#D3D3D3")

        #main Window dimensions
        ####################################################
        app_width = 425
        app_height = 300
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)
        self.main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        ####################################################

        #Main Window Text Widgets
        ####################################################
        self.title = Label(self.main, text="CURSE Registration System", bg="#D3D3D3", fg="black", font="calibri 24 bold", width=app_width, anchor=CENTER)
        self.title.pack()

        self.option_txt = Label(self.main, text="Select a user type", bg="#D3D3D3", fg="black", font="calibri 18 bold", width=app_width, anchor=CENTER)
        self.option_txt.pack(pady=10)
        ####################################################

        #Main Window Button frame widget
        ####################################################
        self.user_frame = LabelFrame(self.main, text="User Type", font="calibri 12 ", bg="#D3D3D3")
        self.user_frame.pack(pady=10)

        self.s_button = Button(self.user_frame, text="  Student  ", font="calibri 12 ", command=self.student_login_page)
        self.s_button.grid(row=0, column=0, padx=10, pady=10)

        self.i_button = Button(self.user_frame, text="  Instructor  ", font="calibri 12 ",command=self.instructor_login_page)
        self.i_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.a_button = Button(self.user_frame, text="  Admin  ", font="calibri 12 ", command=self.admin_login__page)
        self.a_button.grid(row=0, column=2, padx=10, pady=10)

        self.exit_btn = Button(self.main, text = 'Exit', font="calibri 12 ", width=7, command = self.main.destroy)
        self.exit_btn.pack(pady=10, side='bottom')
        ####################################################
        
        self.main.mainloop()

    #student login page
    def student_login_page(self):
        #Main window stays closed until exit button is pressed
        self.main.withdraw()

        #close student window and reopen main menu/Exit Button Function
        def main_menu():
            self.main.deiconify()
            stud_login.withdraw()

        #Login button function
        def s_login_btn():

            #Student Functions Window
            stud_login.withdraw()
            student = Tk()
            student.title("Student")
            student.configure(bg="#D3D3D3")
            app_width = 300
            app_height = 200
            screen_width = student.winfo_screenwidth()
            screen_height = student.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            student.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            s_frame = Frame(student, bg="#D3D3D3" )
            s_frame.pack(pady=30)

            #course button function
            def course_button():
                student.withdraw()
                global course

                #exit button functiion
                def go_back():
                    course.withdraw()
                    student.deiconify()
                
                #course search window
                course = Tk()
                course.title("Courses")
                course.configure(bg="#D3D3D3")
                app_width = 1000
                app_height = 300
                screen_width = course.winfo_screenwidth()
                screen_height = course.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                course.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                #display all courses onto table
                def search_all():
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE")
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()                 

                #SEARCH FUNCTIONS
                ###############################################
                #search courses by crn function
                def search_CRN():
                    #search entry box value
                    crn = crn_entry.get()
                    #destory search window
                    searchCRN.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE CRN = ?", (crn,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by name function
                def search_Name():
                    #search entry box value
                    name = name_entry.get()
                    #destory search window
                    searchName.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE TITLE LIKE ?", (name,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()

                #search courses by department function
                def search_Dept():
                    #search entry box value
                    dept = dept_entry.get()
                    #destory search window
                    searchDept.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE DEPARTMENT LIKE ?", (dept,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()

                #search courses by instructor function
                def search_In():
                    #search entry box value
                    inst = in_entry.get()
                    #destory search window
                    searchIn.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE INSTRUCTOR LIKE ?", (inst,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by year function
                def search_Year():
                    #search entry box value
                    year = yr_entry.get()
                    #destory search window
                    searchYear.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE YEAR LIKE ?", (year,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by time function
                def search_Time():
                    #search entry box value
                    time = time_entry.get()
                    #destory search window
                    searchTime.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE TIME LIKE ?", (time,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
            
                #search courses by semester function
                def search_Sem():
                    #search entry box value
                    sem = sem_entry.get()
                    #destory search window
                    searchSem.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE SEMESTER LIKE ?", (sem,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by day function
                def search_Day():
                    #search entry box value
                    day = day_entry.get()
                    #destory search window
                    searchDay.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE DAYS LIKE ?", (day,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                #################################################################

                #SEARCH FUNCTION WINDOWS
                #################################################################
                #search courses by CRN window
                def searchByCRN():
                    global crn_entry, searchCRN
                    searchCRN = Toplevel(course)
                    searchCRN.title("Search by CRN")
                    searchCRN.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchCRN.winfo_screenwidth()
                    screen_height = searchCRN.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchCRN.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchCRN_frame = LabelFrame(searchCRN, text="CRN", font="calibri 12 ", bg="#D3D3D3")
                    searchCRN_frame.pack(padx=10, pady=10)

                    crn_entry = Entry(searchCRN_frame, font="calibri")
                    crn_entry.pack(padx=10, pady=10)

                    search_button = Button(searchCRN, text="Search Course", font="calibri 12 ", bg="#D3D3D3", command=search_CRN)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by name window
                def searchByName():
                    global name_entry, searchName
                    searchName = Toplevel(course)
                    searchName.title("Search by Name")
                    searchName.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchName.winfo_screenwidth()
                    screen_height = searchName.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchName.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchName_frame = LabelFrame(searchName, text="Name", font="calibri 12 ", bg="#D3D3D3")
                    searchName_frame.pack(padx=10, pady=10)

                    name_entry = Entry(searchName_frame, font="calibri")
                    name_entry.pack(padx=10, pady=10)

                    search_button = Button(searchName, text="Search Name", font="calibri 12 ", bg="#D3D3D3", command=search_Name)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by department window
                def searchByDept():
                    global dept_entry, searchDept
                    searchDept = Toplevel(course)
                    searchDept.title("Search by Department")
                    searchDept.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchDept.winfo_screenwidth()
                    screen_height = searchDept.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchDept.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchDept_frame = LabelFrame(searchDept, text="Department", font="calibri 12 ", bg="#D3D3D3")
                    searchDept_frame.pack(padx=10, pady=10)

                    dept_entry = Entry(searchDept_frame, font="calibri")
                    dept_entry.pack(padx=10, pady=10)

                    search_button = Button(searchDept, text="Search Department", font="calibri 12 ", bg="#D3D3D3", command=search_Dept)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by instructor window
                def searchByIn():
                    global in_entry, searchIn
                    searchIn = Toplevel(course)
                    searchIn.title("Search by Instructor")
                    searchIn.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchIn.winfo_screenwidth()
                    screen_height = searchIn.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchIn.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchIn_frame = LabelFrame(searchIn, text="Instructor", font="calibri 12 ", bg="#D3D3D3")
                    searchIn_frame.pack(padx=10, pady=10)

                    in_entry = Entry(searchIn_frame, font="calibri")
                    in_entry.pack(padx=10, pady=10)

                    search_button = Button(searchIn, text="Search Instructor", font="calibri 12 ", bg="#D3D3D3", command=search_In)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by year window
                def searchByYear():
                    global yr_entry, searchYear
                    searchYear = Toplevel(course)
                    searchYear.title("Search by Year")
                    searchYear.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchYear.winfo_screenwidth()
                    screen_height = searchYear.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchYear.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchYear_frame = LabelFrame(searchYear, text="Year", font="calibri 12 ", bg="#D3D3D3")
                    searchYear_frame.pack(padx=10, pady=10)

                    yr_entry = Entry(searchYear_frame, font="calibri")
                    yr_entry.pack(padx=10, pady=10)

                    search_button = Button(searchYear, text="Search Year", font="calibri 12 ", bg="#D3D3D3", command=search_Year)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by time window
                def searchByTime():
                    global time_entry, searchTime
                    searchTime = Toplevel(course)
                    searchTime.title("Search by Year")
                    searchTime.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchTime.winfo_screenwidth()
                    screen_height = searchTime.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchTime.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchTime_frame = LabelFrame(searchTime, text="Time", font="calibri 12 ", bg="#D3D3D3")
                    searchTime_frame.pack(padx=10, pady=10)

                    time_entry = Entry(searchTime_frame, font="calibri")
                    time_entry.pack(padx=10, pady=10)

                    search_button = Button(searchTime, text="Search Time", font="calibri 12 ", bg="#D3D3D3", command=search_Time)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by semester window    
                def searchBySem():        
                    global sem_entry, searchSem
                    searchSem = Toplevel(course)
                    searchSem.title("Search by Semester")
                    searchSem.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchSem.winfo_screenwidth()
                    screen_height = searchSem.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchSem.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchSem_frame = LabelFrame(searchSem, text="Semester", font="calibri 12 ", bg="#D3D3D3")
                    searchSem_frame.pack(padx=10, pady=10)

                    sem_entry = Entry(searchSem_frame, font="calibri")
                    sem_entry.pack(padx=10, pady=10)

                    search_button = Button(searchSem, text="Search Semester", font="calibri 12 ", bg="#D3D3D3", command=search_Sem)
                    search_button.pack(padx=20, pady=20)

                #search courses by day window
                def searchByDay():
                    global day_entry, searchDay
                    searchDay = Toplevel(course)
                    searchDay.title("Search by Day")
                    searchDay.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchDay.winfo_screenwidth()
                    screen_height = searchDay.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchDay.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchDay_frame = LabelFrame(searchDay, text="Day", font="calibri 12 ", bg="#D3D3D3")
                    searchDay_frame.pack(padx=10, pady=10)

                    day_entry = Entry(searchDay_frame, font="calibri")
                    day_entry.pack(padx=10, pady=10)

                    search_button = Button(searchDay, text="Search Day", font="calibri 12 ", bg="#D3D3D3", command=search_Day)
                    search_button.pack(padx=20, pady=20)
                #################################################################
                
                #search functions menu
                c_menu = Menu(course)
                course.config(menu=c_menu)
                search_menu = Menu(c_menu, tearoff=0)
                c_menu.add_cascade(label="Search", menu=search_menu)
                search_menu.add_command(label="Search by CRN", command=searchByCRN)
                search_menu.add_command(label="Search by Name", command=searchByName)
                search_menu.add_command(label="Search by Department", command=searchByDept)
                search_menu.add_command(label="Search by Instructor", command=searchByIn)
                search_menu.add_command(label="Search by Year", command=searchByYear)
                search_menu.add_command(label="Search by Time", command=searchByTime)
                search_menu.add_command(label="Search by Semester", command=searchBySem)
                search_menu.add_command(label="Search by Day", command=searchByDay)
                search_menu.add_separator()
                search_menu.add_command(label="Reset List", command=search_all)

                #Courses Table style
                style = ttk.Style()
                style.theme_use('default')
                style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
                style.map('Treeview', background=[('selected', "blue")])

                #Table layout
                list_frame = Frame(course)
                list_frame.pack(padx=10,pady=10, fill=X )
                list_scroll = Scrollbar(list_frame)
                list_scroll.pack(side=RIGHT, fill=Y)

                #Courses Table
                course_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
                course_list.pack( fill=X)
                list_scroll.config(command=course_list.yview)

                #Courses Table Content
                course_list['columns'] = ("CRN", "Title", "Department", "Instructor", "Time", "Days", "Semester", "Year", "Credits")
                course_list.column("#0", width=0, stretch=NO)
                course_list.column("CRN", anchor=W, width=25)
                course_list.column("Title", anchor=CENTER, width=125)
                course_list.column("Department", anchor=CENTER, width=20)
                course_list.column("Instructor", anchor=CENTER, width=75)
                course_list.column("Time", anchor=CENTER, width=20)
                course_list.column("Days", anchor=CENTER, width=20)
                course_list.column("Semester", anchor=CENTER, width=40)
                course_list.column("Year", anchor=CENTER, width=30)
                course_list.column("Credits", anchor=CENTER, width=30)

                #Courses Table labels
                course_list.heading("#0", text="", anchor=W)
                course_list.heading("CRN", text="CRN", anchor=W)
                course_list.heading("Title", text="Title", anchor=CENTER)
                course_list.heading("Department", text="Department",anchor=CENTER)
                course_list.heading("Instructor", text="Instructor", anchor=CENTER)
                course_list.heading("Time", text="Time",anchor=CENTER)
                course_list.heading("Days", text="Days", anchor=CENTER)
                course_list.heading("Semester", text="Semester", anchor=CENTER)
                course_list.heading("Year", text="Year", anchor=CENTER)
                course_list.heading("Credits", text="Credits", anchor=CENTER)

                #Exit Button
                gb_btn = Button(course, text = 'Go Back', font="calibri 12 ", width=7, command = go_back)
                gb_btn.pack(pady=10, side='bottom')
                
                #call print list function 
                search_all()

            #schedule button function
            def schedule_button():
                student.withdraw()
                global schedule

                #go back button function
                def go_back():
                    schedule.withdraw()
                    student.deiconify()
                
                #schedule window dimensions
                schedule = Tk()
                schedule.title("Schedule")
                schedule.configure(bg="#D3D3D3")
                app_width = 750
                app_height = 500
                screen_width = schedule.winfo_screenwidth()
                screen_height = schedule.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                schedule.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                #Exit Button
                gb_btn = Button(schedule, text = 'Go Back', font="calibri 12 ", width=7, command = go_back)
                gb_btn.pack(pady=10, side='bottom')

            #logout button function
            def logout_button():
                #destroy student window and go back to login window
                student.destroy()
                self.main.deiconify()
                
            #Student Function Window Widgets
            course_btn = Button(s_frame, text="Courses", font="calibri 12", command=course_button)
            course_btn.grid(row=0, column=0, padx=10, pady=10)
            schedule_btn = Button(s_frame, text="Schedule", font="calibri 12", command=schedule_button)
            schedule_btn.grid(row=0, column=1, padx=10, pady=10)

            #Logout Button
            exit_btn = Button(student, text = 'Logout', font="calibri 12 ", width=7, command = logout_button)
            exit_btn.pack(pady=10,side='bottom')
                    
        #Student login Window Dimensions
        stud_login = Tk()
        stud_login.title("Student")
        stud_login.configure(bg="#D3D3D3")
        app_width = 450
        app_height = 250
        screen_width = stud_login.winfo_screenwidth()
        screen_height = stud_login.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)
        stud_login.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        #Login frame w/widgets
        login_frame = LabelFrame(stud_login, text="Login", font="calibri 12 ", bg="#D3D3D3")
        login_frame.pack(pady=10)

        #email
        e_label = Label(login_frame, text="Email", font="calibri 12 ", bg="#D3D3D3")
        e_label.grid(row=0, column=0, padx=10, pady=10)
        e_entry = Entry(login_frame)
        e_entry.grid(row=0, column=1, padx=10, pady=10)

        #id
        id_label = Label(login_frame, text="ID", font="calibri 12",  bg="#D3D3D3")
        id_label.grid(row=1, column=0, padx=10, pady=10)
        id_entry = Entry(login_frame)
        id_entry.grid(row=1, column=1, padx=10, pady=10)

        #Login button 
        login_btn = Button(stud_login, text="Login", font="calibri 12 ", width=7, command=s_login_btn)
        login_btn.pack(side='top')
        
        #Login status/either successful or invalid
        login_status = Entry(stud_login)
        login_status.pack(side='top',pady=5)

        #Exit Button
        exit_btn = Button(stud_login, text = 'Exit', font="calibri 12 ", width=7, command = main_menu)
        exit_btn.pack(pady=10, side='bottom')

    #instructor login page
    def instructor_login_page(self):
        #Main window stays closed until exit button is pressed
        self.main.withdraw()

        #close instructor window and reopen main menu/Exit Button Function
        def main_menu():
            self.main.deiconify()
            inst_login.withdraw()

        #Login button function
        def i_login_btn():
            #close login window
            inst_login.withdraw()

            #Instructor Functions Window
            instructor = Tk()
            instructor.title("Instructor")
            instructor.configure(bg="#D3D3D3")
            app_width = 300
            app_height = 200
            screen_width = instructor.winfo_screenwidth()
            screen_height = instructor.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            instructor.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            i_frame = Frame(instructor, bg="#D3D3D3" )
            i_frame.pack(pady=30)

            #Course Button Function
            def course_button():
                #Close instructor function window
                instructor.withdraw()

                #exit button functiion
                def go_back():
                    course.withdraw()
                    instructor.deiconify()
                
                #course search window
                course = Tk()
                course.title("Courses")
                course.configure(bg="#D3D3D3")
                app_width = 1000
                app_height = 300
                screen_width = course.winfo_screenwidth()
                screen_height = course.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                course.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                #display all courses onto table
                def search_all():
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE")
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()                 

                #SEARCH FUNCTIONS
                #################################################################
                #search courses by crn function
                def search_CRN():
                    #search entry box value
                    crn = crn_entry.get()
                    #destory search window
                    searchCRN.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE CRN = ?", (crn,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by name function
                def search_Name():
                    #search entry box value
                    name = name_entry.get()
                    #destory search window
                    searchName.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE TITLE LIKE ?", (name,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()

                #search courses by department function
                def search_Dept():
                    #search entry box value
                    dept = dept_entry.get()
                    #destory search window
                    searchDept.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE DEPARTMENT LIKE ?", (dept,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()

                #search courses by instructor function
                def search_In():
                    #search entry box value
                    inst = in_entry.get()
                    #destory search window
                    searchIn.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE INSTRUCTOR LIKE ?", (inst,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by year function
                def search_Year():
                    #search entry box value
                    year = yr_entry.get()
                    #destory search window
                    searchYear.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE YEAR LIKE ?", (year,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by time function
                def search_Time():
                    #search entry box value
                    time = time_entry.get()
                    #destory search window
                    searchTime.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE TIME LIKE ?", (time,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
            
                #search courses by semester function
                def search_Sem():
                    #search entry box value
                    sem = sem_entry.get()
                    #destory search window
                    searchSem.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE SEMESTER LIKE ?", (sem,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by day function
                def search_Day():
                    #search entry box value
                    day = day_entry.get()
                    #destory search window
                    searchDay.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE DAYS LIKE ?", (day,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                #################################################################
                
                #SEARCH FUNCTION WINDOWS
                #################################################################
                #search courses by CRN window
                def searchByCRN():
                    global crn_entry, searchCRN
                    searchCRN = Toplevel(course)
                    searchCRN.title("Search by CRN")
                    searchCRN.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchCRN.winfo_screenwidth()
                    screen_height = searchCRN.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchCRN.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchCRN_frame = LabelFrame(searchCRN, text="CRN", font="calibri 12 ", bg="#D3D3D3")
                    searchCRN_frame.pack(padx=10, pady=10)

                    crn_entry = Entry(searchCRN_frame, font="calibri")
                    crn_entry.pack(padx=10, pady=10)

                    search_button = Button(searchCRN, text="Search Course", font="calibri 12 ", bg="#D3D3D3", command=search_CRN)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by name window
                def searchByName():
                    global name_entry, searchName
                    searchName = Toplevel(course)
                    searchName.title("Search by Name")
                    searchName.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchName.winfo_screenwidth()
                    screen_height = searchName.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchName.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchName_frame = LabelFrame(searchName, text="Name", font="calibri 12 ", bg="#D3D3D3")
                    searchName_frame.pack(padx=10, pady=10)

                    name_entry = Entry(searchName_frame, font="calibri")
                    name_entry.pack(padx=10, pady=10)

                    search_button = Button(searchName, text="Search Name", font="calibri 12 ", bg="#D3D3D3", command=search_Name)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by department window
                def searchByDept():
                    global dept_entry, searchDept
                    searchDept = Toplevel(course)
                    searchDept.title("Search by Department")
                    searchDept.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchDept.winfo_screenwidth()
                    screen_height = searchDept.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchDept.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchDept_frame = LabelFrame(searchDept, text="Department", font="calibri 12 ", bg="#D3D3D3")
                    searchDept_frame.pack(padx=10, pady=10)

                    dept_entry = Entry(searchDept_frame, font="calibri")
                    dept_entry.pack(padx=10, pady=10)

                    search_button = Button(searchDept, text="Search Department", font="calibri 12 ", bg="#D3D3D3", command=search_Dept)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by instructor window
                def searchByIn():
                    global in_entry, searchIn
                    searchIn = Toplevel(course)
                    searchIn.title("Search by Instructor")
                    searchIn.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchIn.winfo_screenwidth()
                    screen_height = searchIn.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchIn.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchIn_frame = LabelFrame(searchIn, text="Instructor", font="calibri 12 ", bg="#D3D3D3")
                    searchIn_frame.pack(padx=10, pady=10)

                    in_entry = Entry(searchIn_frame, font="calibri")
                    in_entry.pack(padx=10, pady=10)

                    search_button = Button(searchIn, text="Search Instructor", font="calibri 12 ", bg="#D3D3D3", command=search_In)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by year window
                def searchByYear():
                    global yr_entry, searchYear
                    searchYear = Toplevel(course)
                    searchYear.title("Search by Year")
                    searchYear.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchYear.winfo_screenwidth()
                    screen_height = searchYear.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchYear.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchYear_frame = LabelFrame(searchYear, text="Year", font="calibri 12 ", bg="#D3D3D3")
                    searchYear_frame.pack(padx=10, pady=10)

                    yr_entry = Entry(searchYear_frame, font="calibri")
                    yr_entry.pack(padx=10, pady=10)

                    search_button = Button(searchYear, text="Search Year", font="calibri 12 ", bg="#D3D3D3", command=search_Year)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by time window
                def searchByTime():
                    global time_entry, searchTime
                    searchTime = Toplevel(course)
                    searchTime.title("Search by Year")
                    searchTime.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchTime.winfo_screenwidth()
                    screen_height = searchTime.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchTime.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchTime_frame = LabelFrame(searchTime, text="Time", font="calibri 12 ", bg="#D3D3D3")
                    searchTime_frame.pack(padx=10, pady=10)

                    time_entry = Entry(searchTime_frame, font="calibri")
                    time_entry.pack(padx=10, pady=10)

                    search_button = Button(searchTime, text="Search Time", font="calibri 12 ", bg="#D3D3D3", command=search_Time)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by semester window    
                def searchBySem():        
                    global sem_entry, searchSem
                    searchSem = Toplevel(course)
                    searchSem.title("Search by Semester")
                    searchSem.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchSem.winfo_screenwidth()
                    screen_height = searchSem.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchSem.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchSem_frame = LabelFrame(searchSem, text="Semester", font="calibri 12 ", bg="#D3D3D3")
                    searchSem_frame.pack(padx=10, pady=10)

                    sem_entry = Entry(searchSem_frame, font="calibri")
                    sem_entry.pack(padx=10, pady=10)

                    search_button = Button(searchSem, text="Search Semester", font="calibri 12 ", bg="#D3D3D3", command=search_Sem)
                    search_button.pack(padx=20, pady=20)

                #search courses by day window
                def searchByDay():
                    global day_entry, searchDay
                    searchDay = Toplevel(course)
                    searchDay.title("Search by Day")
                    searchDay.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchDay.winfo_screenwidth()
                    screen_height = searchDay.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchDay.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchDay_frame = LabelFrame(searchDay, text="Day", font="calibri 12 ", bg="#D3D3D3")
                    searchDay_frame.pack(padx=10, pady=10)

                    day_entry = Entry(searchDay_frame, font="calibri")
                    day_entry.pack(padx=10, pady=10)

                    search_button = Button(searchDay, text="Search Day", font="calibri 12 ", bg="#D3D3D3", command=search_Day)
                    search_button.pack(padx=20, pady=20)
                #################################################################
                
                #search functions menu
                c_menu = Menu(course)
                course.config(menu=c_menu)
                search_menu = Menu(c_menu, tearoff=0)
                c_menu.add_cascade(label="Search", menu=search_menu)
                search_menu.add_command(label="Search by CRN", command=searchByCRN)
                search_menu.add_command(label="Search by Name", command=searchByName)
                search_menu.add_command(label="Search by Department", command=searchByDept)
                search_menu.add_command(label="Search by Instructor", command=searchByIn)
                search_menu.add_command(label="Search by Year", command=searchByYear)
                search_menu.add_command(label="Search by Time", command=searchByTime)
                search_menu.add_command(label="Search by Semester", command=searchBySem)
                search_menu.add_command(label="Search by Day", command=searchByDay)
                search_menu.add_separator()
                search_menu.add_command(label="Reset List", command=search_all)

                #Courses Table style
                style = ttk.Style()
                style.theme_use('default')
                style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
                style.map('Treeview', background=[('selected', "blue")])

                #Courses table layout
                list_frame = Frame(course)
                list_frame.pack(padx=10,pady=10, fill=X )
                list_scroll = Scrollbar(list_frame)
                list_scroll.pack(side=RIGHT, fill=Y)
                #Courses Table
                course_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
                course_list.pack( fill=X)
                list_scroll.config(command=course_list.yview)

                #Courses Table Cntent
                course_list['columns'] = ("CRN", "Title", "Department", "Instructor", "Time", "Days", "Semester", "Year", "Credits")
                course_list.column("#0", width=0, stretch=NO)
                course_list.column("CRN", anchor=W, width=25)
                course_list.column("Title", anchor=CENTER, width=125)
                course_list.column("Department", anchor=CENTER, width=20)
                course_list.column("Instructor", anchor=CENTER, width=75)
                course_list.column("Time", anchor=CENTER, width=20)
                course_list.column("Days", anchor=CENTER, width=20)
                course_list.column("Semester", anchor=CENTER, width=40)
                course_list.column("Year", anchor=CENTER, width=30)
                course_list.column("Credits", anchor=CENTER, width=30)

                #Courses Table Labels
                course_list.heading("#0", text="", anchor=W)
                course_list.heading("CRN", text="CRN", anchor=W)
                course_list.heading("Title", text="Title", anchor=CENTER)
                course_list.heading("Department", text="Department",anchor=CENTER)
                course_list.heading("Instructor", text="Instructor", anchor=CENTER)
                course_list.heading("Time", text="Time",anchor=CENTER)
                course_list.heading("Days", text="Days", anchor=CENTER)
                course_list.heading("Semester", text="Semester", anchor=CENTER)
                course_list.heading("Year", text="Year", anchor=CENTER)
                course_list.heading("Credits", text="Credits", anchor=CENTER)

                #Exit Button
                gb_btn = Button(course, text = 'Go Back', font="calibri 12 ", width=7, command = go_back)
                gb_btn.pack(pady=10, side='bottom')
                search_all()

            #Schedule Button Function
            def schedule_button():
                #Close instructor function window
                instructor.withdraw()
                global schedule

                #go back button function
                def go_back():
                    schedule.withdraw()
                    instructor.deiconify()
                
                #Schedule Window
                schedule = Tk()
                schedule.title("Schedule")
                schedule.configure(bg="#D3D3D3")
                app_width = 750
                app_height = 500
                screen_width = schedule.winfo_screenwidth()
                screen_height = schedule.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                schedule.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                #Exit Button
                gb_btn = Button(schedule, text = 'Go Back', font="calibri 12 ", width=7, command = go_back)
                gb_btn.pack(pady=10, side='bottom')

            #Roster Button Function
            def roster_button():
                pass

            #Logout Button Function
            def logout_button():
                instructor.destroy()
                self.main.deiconify()
                
            #Instructor function window widgets
            course_btn = Button(i_frame, text="Courses", font="calibri 12", command=course_button)
            course_btn.grid(row=0, column=0, padx=10, pady=10)
            schedule_btn = Button(i_frame, text="Schedule", font="calibri 12", command=schedule_button)
            schedule_btn.grid(row=0, column=1, padx=10, pady=10)
            roster_btn = Button(i_frame, text="Roster", font="calibri 12", command=roster_button)
            roster_btn.grid(row=0, column=2, padx=10, pady=10)

            #Logout Button
            exit_btn = Button(instructor, text = 'Logout', font="calibri 12 ", width=7, command = logout_button)
            exit_btn.pack(pady=10,side='bottom')

        #instructor login window dimensions
        inst_login = Tk()
        inst_login.title("Instructor")
        inst_login.configure(bg="#D3D3D3")
        app_width = 450
        app_height = 250
        screen_width = inst_login.winfo_screenwidth()
        screen_height = inst_login.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)
        inst_login.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        #Login frame w/widgets
        login_frame = LabelFrame(inst_login, text="Login", font="calibri 12 ", bg="#D3D3D3")
        login_frame.pack(pady=10)

        #first name
        e_label = Label(login_frame, text="Email", font="calibri 12 ", bg="#D3D3D3")
        e_label.grid(row=0, column=0, padx=10, pady=10)
        e_entry = Entry(login_frame)
        e_entry.grid(row=0, column=1, padx=10, pady=10)

        #id
        id_label = Label(login_frame, text="ID", font="calibri 12",  bg="#D3D3D3")
        id_label.grid(row=1, column=0, padx=10, pady=10)
        id_entry = Entry(login_frame)
        id_entry.grid(row=1, column=1, padx=10, pady=10)

        #login button 
        login_btn = Button(inst_login, text="Login", font="calibri 12 ", width=7, command=i_login_btn)
        login_btn.pack(side='top')
        
        #Login Status
        login_status = Entry(inst_login)
        login_status.pack(side='top',pady=5)

        #exit button
        exit_btn = Button(inst_login, text = 'Exit', font="calibri 12 ", width=7, command = main_menu)
        exit_btn.pack(pady=10, side='bottom')

    #admin login page
    def admin_login__page(self):

        #Main window stays closed until exit button is pressed
        self.main.withdraw()

        #Exit button function
        def main_menu():
            self.main.deiconify()
            admin_login.withdraw()

        #Login button function
        def a_login_btn():
            #Close Login window
            admin_login.withdraw()

            #Admin Function Window
            admin = Tk()
            admin.title("Admin")
            admin.configure(bg="#D3D3D3")
            app_width = 300
            app_height = 200
            screen_width = admin.winfo_screenwidth()
            screen_height = admin.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            admin.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            i_frame = Frame(admin, bg="#D3D3D3" )
            i_frame.pack(pady=30)

            #Course Button function
            def course_button():
                admin.withdraw()

                #exit button functiion
                def go_back():
                    course.withdraw()
                    admin.deiconify()
                
                #course search window
                course = Tk()
                course.title("Courses")
                course.configure(bg="#D3D3D3")
                app_width = 1000
                app_height = 400
                screen_width = course.winfo_screenwidth()
                screen_height = course.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                course.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                #display all courses onto table
                def search_all():
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE")
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()                 

                #SEARCH FUNCTIONS
                #################################################################
                #search courses by crn function
                def search_CRN():
                    #search entry box value
                    crn = crn_entry.get()
                    #destory search window
                    searchCRN.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE CRN = ?", (crn,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by name function
                def search_Name():
                    #search entry box value
                    name = name_entry.get()
                    #destory search window
                    searchName.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE TITLE LIKE ?", (name,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()

                #search courses by department function
                def search_Dept():
                    #search entry box value
                    dept = dept_entry.get()
                    #destory search window
                    searchDept.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE DEPARTMENT LIKE ?", (dept,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()

                #search courses by instructor function
                def search_In():
                    #search entry box value
                    inst = in_entry.get()
                    #destory search window
                    searchIn.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE INSTRUCTOR LIKE ?", (inst,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by year function
                def search_Year():
                    #search entry box value
                    year = yr_entry.get()
                    #destory search window
                    searchYear.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE YEAR LIKE ?", (year,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by time function
                def search_Time():
                    #search entry box value
                    time = time_entry.get()
                    #destory search window
                    searchTime.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE TIME LIKE ?", (time,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
            
                #search courses by semester function
                def search_Sem():
                    #search entry box value
                    sem = sem_entry.get()
                    #destory search window
                    searchSem.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE SEMESTER LIKE ?", (sem,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                
                #search courses by day function
                def search_Day():
                    #search entry box value
                    day = day_entry.get()
                    #destory search window
                    searchDay.destroy()
                    #clear table
                    for record in course_list.get_children():
                        course_list.delete(record)
                    conn = sqlite3.connect('cursebackend/schooldatabase.db')
                    c = conn.cursor()

                    c.execute("SELECT * FROM COURSE WHERE DAYS LIKE ?", (day,))
                    records = c.fetchall()

                    
                    count = 0

                    for record in records:
                        if count % 2 == 0:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                            course_list.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                    conn.commit()
                #################################################################
            
                #SEARCH FUNCTION WINDOWS
                #################################################################
                #search courses by CRN window
                def searchByCRN():
                    global crn_entry, searchCRN
                    searchCRN = Toplevel(course)
                    searchCRN.title("Search by CRN")
                    searchCRN.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchCRN.winfo_screenwidth()
                    screen_height = searchCRN.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchCRN.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchCRN_frame = LabelFrame(searchCRN, text="CRN", font="calibri 12 ", bg="#D3D3D3")
                    searchCRN_frame.pack(padx=10, pady=10)

                    crn_entry = Entry(searchCRN_frame, font="calibri")
                    crn_entry.pack(padx=10, pady=10)

                    search_button = Button(searchCRN, text="Search Course", font="calibri 12 ", bg="#D3D3D3", command=search_CRN)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by name window
                def searchByName():
                    global name_entry, searchName
                    searchName = Toplevel(course)
                    searchName.title("Search by Name")
                    searchName.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchName.winfo_screenwidth()
                    screen_height = searchName.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchName.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchName_frame = LabelFrame(searchName, text="Name", font="calibri 12 ", bg="#D3D3D3")
                    searchName_frame.pack(padx=10, pady=10)

                    name_entry = Entry(searchName_frame, font="calibri")
                    name_entry.pack(padx=10, pady=10)

                    search_button = Button(searchName, text="Search Name", font="calibri 12 ", bg="#D3D3D3", command=search_Name)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by department window
                def searchByDept():
                    global dept_entry, searchDept
                    searchDept = Toplevel(course)
                    searchDept.title("Search by Department")
                    searchDept.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchDept.winfo_screenwidth()
                    screen_height = searchDept.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchDept.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchDept_frame = LabelFrame(searchDept, text="Department", font="calibri 12 ", bg="#D3D3D3")
                    searchDept_frame.pack(padx=10, pady=10)

                    dept_entry = Entry(searchDept_frame, font="calibri")
                    dept_entry.pack(padx=10, pady=10)

                    search_button = Button(searchDept, text="Search Department", font="calibri 12 ", bg="#D3D3D3", command=search_Dept)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by instructor window
                def searchByIn():
                    global in_entry, searchIn
                    searchIn = Toplevel(course)
                    searchIn.title("Search by Instructor")
                    searchIn.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchIn.winfo_screenwidth()
                    screen_height = searchIn.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchIn.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchIn_frame = LabelFrame(searchIn, text="Instructor", font="calibri 12 ", bg="#D3D3D3")
                    searchIn_frame.pack(padx=10, pady=10)

                    in_entry = Entry(searchIn_frame, font="calibri")
                    in_entry.pack(padx=10, pady=10)

                    search_button = Button(searchIn, text="Search Instructor", font="calibri 12 ", bg="#D3D3D3", command=search_In)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by year window
                def searchByYear():
                    global yr_entry, searchYear
                    searchYear = Toplevel(course)
                    searchYear.title("Search by Year")
                    searchYear.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchYear.winfo_screenwidth()
                    screen_height = searchYear.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchYear.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchYear_frame = LabelFrame(searchYear, text="Year", font="calibri 12 ", bg="#D3D3D3")
                    searchYear_frame.pack(padx=10, pady=10)

                    yr_entry = Entry(searchYear_frame, font="calibri")
                    yr_entry.pack(padx=10, pady=10)

                    search_button = Button(searchYear, text="Search Year", font="calibri 12 ", bg="#D3D3D3", command=search_Year)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by time window
                def searchByTime():
                    global time_entry, searchTime
                    searchTime = Toplevel(course)
                    searchTime.title("Search by Year")
                    searchTime.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchTime.winfo_screenwidth()
                    screen_height = searchTime.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchTime.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchTime_frame = LabelFrame(searchTime, text="Time", font="calibri 12 ", bg="#D3D3D3")
                    searchTime_frame.pack(padx=10, pady=10)

                    time_entry = Entry(searchTime_frame, font="calibri")
                    time_entry.pack(padx=10, pady=10)

                    search_button = Button(searchTime, text="Search Time", font="calibri 12 ", bg="#D3D3D3", command=search_Time)
                    search_button.pack(padx=20, pady=20)
                
                #search courses by semester window    
                def searchBySem():        
                    global sem_entry, searchSem
                    searchSem = Toplevel(course)
                    searchSem.title("Search by Semester")
                    searchSem.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchSem.winfo_screenwidth()
                    screen_height = searchSem.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchSem.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchSem_frame = LabelFrame(searchSem, text="Semester", font="calibri 12 ", bg="#D3D3D3")
                    searchSem_frame.pack(padx=10, pady=10)

                    sem_entry = Entry(searchSem_frame, font="calibri")
                    sem_entry.pack(padx=10, pady=10)

                    search_button = Button(searchSem, text="Search Semester", font="calibri 12 ", bg="#D3D3D3", command=search_Sem)
                    search_button.pack(padx=20, pady=20)

                #search courses by day window
                def searchByDay():
                    global day_entry, searchDay
                    searchDay = Toplevel(course)
                    searchDay.title("Search by Day")
                    searchDay.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = searchDay.winfo_screenwidth()
                    screen_height = searchDay.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    searchDay.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    searchDay_frame = LabelFrame(searchDay, text="Day", font="calibri 12 ", bg="#D3D3D3")
                    searchDay_frame.pack(padx=10, pady=10)

                    day_entry = Entry(searchDay_frame, font="calibri")
                    day_entry.pack(padx=10, pady=10)

                    search_button = Button(searchDay, text="Search Day", font="calibri 12 ", bg="#D3D3D3", command=search_Day)
                    search_button.pack(padx=20, pady=20)
                #################################################################
                
                #search functions menu
                c_menu = Menu(course)
                course.config(menu=c_menu)
                search_menu = Menu(c_menu, tearoff=0)
                c_menu.add_cascade(label="Search", menu=search_menu)
                search_menu.add_command(label="Search by CRN", command=searchByCRN)
                search_menu.add_command(label="Search by Name", command=searchByName)
                search_menu.add_command(label="Search by Department", command=searchByDept)
                search_menu.add_command(label="Search by Instructor", command=searchByIn)
                search_menu.add_command(label="Search by Year", command=searchByYear)
                search_menu.add_command(label="Search by Time", command=searchByTime)
                search_menu.add_command(label="Search by Semester", command=searchBySem)
                search_menu.add_command(label="Search by Day", command=searchByDay)
                search_menu.add_separator()
                search_menu.add_command(label="Reset List", command=search_all)

                #Course Table style
                style = ttk.Style()
                style.theme_use('default')
                style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
                style.map('Treeview', background=[('selected', "blue")])

                #Course Table layout
                list_frame = Frame(course)
                list_frame.pack(padx=10,pady=10, fill=X )
                list_scroll = Scrollbar(list_frame)
                list_scroll.pack(side=RIGHT, fill=Y)

                #Course Table
                course_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
                course_list.pack( fill=X)
                list_scroll.config(command=course_list.yview)

                #Course Table contents
                course_list['columns'] = ("CRN", "Title", "Department", "Instructor", "Time", "Days", "Semester", "Year", "Credits")
                course_list.column("#0", width=0, stretch=NO)
                course_list.column("CRN", anchor=W, width=25)
                course_list.column("Title", anchor=CENTER, width=125)
                course_list.column("Department", anchor=CENTER, width=20)
                course_list.column("Instructor", anchor=CENTER, width=75)
                course_list.column("Time", anchor=CENTER, width=20)
                course_list.column("Days", anchor=CENTER, width=20)
                course_list.column("Semester", anchor=CENTER, width=40)
                course_list.column("Year", anchor=CENTER, width=30)
                course_list.column("Credits", anchor=CENTER, width=30)

                #Course Table labels
                course_list.heading("#0", text="", anchor=W)
                course_list.heading("CRN", text="CRN", anchor=W)
                course_list.heading("Title", text="Title", anchor=CENTER)
                course_list.heading("Department", text="Department",anchor=CENTER)
                course_list.heading("Instructor", text="Instructor", anchor=CENTER)
                course_list.heading("Time", text="Time",anchor=CENTER)
                course_list.heading("Days", text="Days", anchor=CENTER)
                course_list.heading("Semester", text="Semester", anchor=CENTER)
                course_list.heading("Year", text="Year", anchor=CENTER)
                course_list.heading("Credits", text="Credits", anchor=CENTER)

                #Add Course Function
                def add():
                    crn = CRN_entry1.get()
                    title = title_entry1.get()
                    dept = dept_entry1.get()
                    inst = inst_entry1.get()
                    time = time_entry1.get()
                    day = day_entry1.get()
                    sem = sem_entry1.get()
                    year = year_entry1.get()
                    cred = cred_entry1.get()
                    addCourse.destroy()

                #Remove Course function
                def remove():
                    rmvCourse.destroy()
                    
                #Add Course Button Window
                def add_course():
                    global addCourse, CRN_entry1, title_entry1, dept_entry1, inst_entry1, time_entry1, day_entry1, sem_entry1, year_entry1, cred_entry1
                    addCourse = Toplevel(course)
                    addCourse.title("Add Course")
                    addCourse.configure(bg="#D3D3D3")
                    app_width = 850
                    app_height = 400
                    screen_width = addCourse.winfo_screenwidth()
                    screen_height = addCourse.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    addCourse.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    addCourse_frame = LabelFrame(addCourse, text="Course Information", font="calibri 12 ", bg="#D3D3D3")
                    addCourse_frame.pack(fill="x", expand="yes", padx=20, side='top')


                    crn_txt = Label(addCourse_frame, text="CRN", font="calibri 12 ", bg="#D3D3D3")
                    crn_txt.grid(row=0, column=0, padx=5, pady=5)
                    CRN_entry1 = Entry(addCourse_frame, font="calibri")
                    CRN_entry1.grid(row=0, column=1, padx=5, pady=5)

                    title_txt = Label(addCourse_frame, text="Title", font="calibri 12 ", bg="#D3D3D3")
                    title_txt.grid(row=1, column=0, padx=5, pady=5)
                    title_entry1 = Entry(addCourse_frame, font="calibri")
                    title_entry1.grid(row=1, column=1, padx=5, pady=5)

                    dept_txt = Label(addCourse_frame, text="Department", font="calibri 12 ", bg="#D3D3D3")
                    dept_txt.grid(row=2, column=0, padx=5, pady=5)
                    dept_entry1 = Entry(addCourse_frame, font="calibri")
                    dept_entry1.grid(row=2, column=1, padx=5, pady=5)

                    inst_txt = Label(addCourse_frame, text="Instructor", font="calibri 12 ", bg="#D3D3D3")
                    inst_txt.grid(row=0, column=2, padx=5, pady=5)
                    inst_entry1 = Entry(addCourse_frame, font="calibri")
                    inst_entry1.grid(row=0, column=3, padx=5, pady=5)

                    time_txt = Label(addCourse_frame, text="Time", font="calibri 12 ", bg="#D3D3D3")
                    time_txt.grid(row=1, column=2, padx=5, pady=5)
                    time_entry1 = Entry(addCourse_frame, font="calibri")
                    time_entry1.grid(row=1, column=3, padx=5, pady=5)

                    day_txt = Label(addCourse_frame, text="Day(s)", font="calibri 12 ", bg="#D3D3D3")
                    day_txt.grid(row=2, column=2, padx=5, pady=5)
                    day_entry1 = Entry(addCourse_frame, font="calibri")
                    day_entry1.grid(row=2, column=3, padx=5, pady=5)

                    sem_txt = Label(addCourse_frame, text="Semester", font="calibri 12 ", bg="#D3D3D3")
                    sem_txt.grid(row=0, column=4, padx=5, pady=5)
                    sem_entry1 = Entry(addCourse_frame, font="calibri")
                    sem_entry1.grid(row=0, column=5, padx=5, pady=5)

                    year_txt = Label(addCourse_frame, text="year", font="calibri 12 ", bg="#D3D3D3")
                    year_txt.grid(row=1, column=4, padx=5, pady=5)
                    year_entry1 = Entry(addCourse_frame, font="calibri")
                    year_entry1.grid(row=1, column=5, padx=5, pady=5)

                    cred_txt = Label(addCourse_frame, text="Credits", font="calibri 12 ", bg="#D3D3D3")
                    cred_txt.grid(row=2, column=4, padx=5, pady=5)
                    cred_entry1 = Entry(addCourse_frame, font="calibri")
                    cred_entry1.grid(row=2, column=5, padx=5, pady=5)

                    add_button = Button(addCourse, text="Add Course", font="calibri 12 ", bg="#D3D3D3", command=add)
                    add_button.pack(padx=5, pady=20)
                    
                #Rmv Course Button Window
                def rmv_course():
                    global rmvCourse
                    rmvCourse = Toplevel(course)
                    rmvCourse.title("Add Course")
                    rmvCourse.configure(bg="#D3D3D3")
                    app_width = 400
                    app_height = 200
                    screen_width = rmvCourse.winfo_screenwidth()
                    screen_height = rmvCourse.winfo_screenheight()
                    x = (screen_width / 2) - (app_width / 2)
                    y = (screen_height / 2 ) - (app_height / 2)
                    rmvCourse.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                    rmv_frame = LabelFrame(rmvCourse, text="Remove by CRN", font="calibri 12 ", bg="#D3D3D3")
                    rmv_frame.pack(padx=10, pady=10)

                    rmv_entry = Entry(rmv_frame, font="calibri")
                    rmv_entry.pack(padx=10, pady=10)

                    rmv_button = Button(rmvCourse, text="Remove Course", font="calibri 12 ", bg="#D3D3D3", command=remove)
                    rmv_button.pack(padx=20, pady=20)

                #Course Command Frame
                cmd_frame = LabelFrame(course, text="Commands", font="calibri 12 ", bg="#D3D3D3")
                cmd_frame.pack(pady=10)

                #COURSE COMMAND 
                add_btn = Button(cmd_frame, text="Add Course", command = add_course)
                add_btn.grid(row=0, column=0, padx=10, pady=10)
                rmv = Button(cmd_frame, text="Remove Course", command = rmv_course)
                rmv.grid(row=0, column=1, padx=10, pady=10)



                ###########################################################
                #Exit Button
                gb_btn = Button(course, text = 'Go Back', font="calibri 12 ", width=7, command = go_back)
                gb_btn.pack(pady=10, side='bottom')

                #display data on table
                search_all()

                #go back button function
                def go_back():
                    schedule.withdraw()
                    admin.deiconify()
                
                #Exit Button
                gb_btn = Button(schedule, text = 'Go Back', font="calibri 12 ", width=7, command = go_back)
                gb_btn.pack(pady=10, side='bottom')

            #roster button function
            def roster_button():
                pass

            #logout button function
            def logout_button():
                admin.destroy()
                self.main.deiconify()
                
            #Admin function window widgets
            course_btn = Button(i_frame, text="Courses", font="calibri 12", command=course_button)
            course_btn.grid(row=0, column=0, padx=10, pady=10)
            roster_btn = Button(i_frame, text="Roster", font="calibri 12", command=roster_button)
            roster_btn.grid(row=0, column=2, padx=10, pady=10)

            #Logout Button
            exit_btn = Button(admin, text = 'Logout', font="calibri 12 ", width=7, command = logout_button)
            exit_btn.pack(pady=10,side='bottom')

        #admin login window dimensions
        admin_login = Tk()
        admin_login.title("Admin")
        admin_login.configure(bg="#D3D3D3")
        app_width = 450
        app_height = 250
        screen_width = admin_login.winfo_screenwidth()
        screen_height = admin_login.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)
        admin_login.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        #Login frame w/widgets
        login_frame = LabelFrame(admin_login, text="Login", font="calibri 12 ", bg="#D3D3D3")
        login_frame.pack(pady=10)

        #first name
        e_label = Label(login_frame, text="Email", font="calibri 12 ", bg="#D3D3D3")
        e_label.grid(row=0, column=0, padx=10, pady=10)
        e_entry = Entry(login_frame)
        e_entry.grid(row=0, column=1, padx=10, pady=10)

        #id
        id_label = Label(login_frame, text="ID", font="calibri 12",  bg="#D3D3D3")
        id_label.grid(row=1, column=0, padx=10, pady=10)
        id_entry = Entry(login_frame)
        id_entry.grid(row=1, column=1, padx=10, pady=10)

        #login button 
        login_btn = Button(admin_login, text="Login", font="calibri 12 ", width=7, command=a_login_btn)
        login_btn.pack(side='top')
        
        #Login Status
        login_status = Entry(admin_login)
        login_status.pack(side='top',pady=5)

        #exit Button
        exit_btn = Button(admin_login, text = 'Exit', font="calibri 12 ", width=7, command = main_menu)
        exit_btn.pack(pady=10, side='bottom')
        
a = MainApp()
