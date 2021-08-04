from tkinter import *
from tkinter import ttk


try: 
    from admin import admin
    from student import student
    from user import user
    from instructor import instructor
    from userLogin import userLogin
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CURSEBackEnd.admin import admin
    from CURSEBackEnd.student import student
    from CURSEBackEnd.user import user
    from CURSEBackEnd.instructor import instructor
    from CURSEBackEnd.userLogin import userLogin


class MainApp:

    def __init__(self) -> None:
        self.login_class = userLogin()
        self.cred: dict
        self.user: user
        

        #Main App Window
        self.main = Tk()
        self.main.title("CURSE")
        self.main.configure(bg="#D3D3D3")

        

        self.main_menu()

        self.main.mainloop()

    def create_user(self):
        utype = self.cred['utype'].lower()

        if utype == 'admin':
            self.user = admin(self.cred['fname'], self.cred['lname'], self.cred['ID'])
            self.admin_page()
        elif utype == 'instructor':
            self.user = instructor(self.cred['fname'], self.cred['lname'], self.cred['ID'])
            self.instructor_page()
        elif utype == 'student':
            self.user = student(self.cred['fname'], self.cred['lname'], self.cred['ID'])
            self.student_page()
        else:
            raise Exception

    def courses_page(self, utype):
        #course search window
        def courses_layout(frame):
            frame.title("Courses")
            frame.configure(bg="#D3D3D3")
            app_width = 1000
            app_height = 300
            screen_width = frame.winfo_screenwidth()
            screen_height = frame.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            frame.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            
            #Exit Button
            gb_btn = Button(frame, text = 'Go Back', font="calibri 12 ", width=7, command = go_back)
            gb_btn.pack(pady=10, side='bottom')
    
        #searching cascated menu
        def cas_menu(c_menu):
            #search functions menu
            self.course.config(menu=c_menu)
            search_menu = Menu(c_menu, tearoff=0)
            c_menu.add_cascade(label="Search", menu=search_menu)
            search_menu.add_command(label="Search by CRN", command=lambda: search_window("CRN"))
            search_menu.add_command(label="Search by Name", command=lambda: search_window("Name"))
            search_menu.add_command(label="Search by Department", command=lambda: search_window("Department"))
            search_menu.add_command(label="Search by Instructor", command=lambda: search_window("Instructor"))
            search_menu.add_command(label="Search by Year", command=lambda: search_window("Year"))
            search_menu.add_command(label="Search by Time", command=lambda: search_window("Time"))
            search_menu.add_command(label="Search by Semester", command=lambda: search_window("Semester"))
            search_menu.add_command(label="Search by Day", command=lambda: search_window("Day"))
            search_menu.add_separator()
            search_menu.add_command(label="Reset List", command=lambda: search_function("All", "All", course_list))
        
        #course table display
        def course_table(style, list_frame, list_scroll, course_list):
                #Courses Table style
                style.theme_use('default')
                style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
                style.map('Treeview', background=[('selected', "blue")])

                #Table layout
                list_frame.pack(padx=10,pady=10, fill=X )
                list_scroll.pack(side=RIGHT, fill=Y)

                #Courses Table
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

        #exit button function
        def go_back():
            self.course.withdraw()
            utype.deiconify()

        #search functions
        def search_function(search_type, search_term, course_list):
            s_type = search_type.lower()

            if s_type != "all":
                search.destroy()

            if s_type == "crn":
                records = self.user.searchCourseByCRN(search_term)
            elif s_type == "name":
                records = self.user.searchCourseByName(search_term)
            elif s_type == "department":
                records = self.user.searchCoursebyDept(search_term)
            elif s_type == "instructor":
                pass
            elif s_type == "year":
                records = self.user.searchCoursebyYear(search_term)
            elif s_type == "time":
                pass
            elif s_type == "semester":
                records = self.user.searchCoursebySem(search_term)
            elif s_type == "day":
                pass
            elif s_type == "all":
                records = self.user.searchAllCourse()
            else:
                raise Exception(f"Unknown search type: {search_type}")

            for record in course_list.get_children():
                        course_list.delete(record)

            for i, record in enumerate(records, start=0):
                if i % 2 == 0:
                    course_list.insert(parent='', index='end', iid=i, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                else:
                    course_list.insert(parent='', index='end', iid=i, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
        
        #search windows
        def search_window(search_type):
            global search 
            search = Toplevel(self.course)
            search.title("Search by " + search_type)
            search.configure(bg="#D3D3D3")
            app_width = 400
            app_height = 200
            screen_width = search.winfo_screenwidth()
            screen_height = search.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            search.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

            searchCRN_frame = LabelFrame(search, text=search_type, font="calibri 12 ", bg="#D3D3D3")
            searchCRN_frame.pack(padx=10, pady=10)

            crn_entry = Entry(searchCRN_frame, font="calibri")
            crn_entry.pack(padx=10, pady=10)

            search_button = Button(search, text="Search Course", font="calibri 12 ", bg="#D3D3D3", command=lambda: search_function(search_type, crn_entry.get(), course_list))
            search_button.pack(padx=20, pady=20)

        # Constructing Search window
        self.course = Tk()
        courses_layout(self.course)

        c_menu = Menu(self.course)
        cas_menu(c_menu)

        style = ttk.Style()
        list_frame = Frame(self.course)
        list_scroll = Scrollbar(list_frame)
        course_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
        course_table(style, list_frame, list_scroll, course_list)

        search_function("All", "All", course_list)

    def schedule_page(self,utype):
        
        #schedule window
        def schedule_layout(frame):
            frame.title("Schedule")
            frame.configure(bg="#D3D3D3")
            app_width = 1000
            app_height = 300
            screen_width = frame.winfo_screenwidth()
            screen_height = frame.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            frame.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

            #Command frame
            
            #Exit Button
            gb_btn = Button(frame, text = 'Go Back', font="calibri 12 ", width=7, command=go_back)
            gb_btn.pack(pady=10, side='bottom')
        
        #command menu
        def command_menu(c_menu):
            #command buttons
            self.schedule.config(menu=c_menu)
            cmd = Menu(c_menu, tearoff=0)
            c_menu.add_cascade(label="Commands", menu=cmd)
            cmd.add_command(label="Add Course", command=add_window)
            cmd.add_command(label="Drop Course", command=drop_window)
            cmd.add_separator()
            cmd.add_command(label="Print Schedule", command=get_schedule)

        #schedule table display
        def schedule_table(style, list_frame, list_scroll, schedule_list):
            #Courses Table style
            style.theme_use('default')
            style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
            style.map('Treeview', background=[('selected', "blue")])

            #Table layout
            list_frame.pack(padx=10,pady=10, fill=X )
            list_scroll.pack(side=RIGHT, fill=Y)

            #Courses Table
            schedule_list.pack( fill=X)
            list_scroll.config(command=schedule_list.yview)

            #Courses Table Content
            schedule_list['columns'] = ("CRN", "Title", "Department", "Instructor", "Time", "Days", "Semester", "Year", "Credits")
            schedule_list.column("#0", width=0, stretch=NO)
            schedule_list.column("CRN", anchor=W, width=25)
            schedule_list.column("Title", anchor=CENTER, width=125)
            schedule_list.column("Department", anchor=CENTER, width=20)
            schedule_list.column("Instructor", anchor=CENTER, width=75)
            schedule_list.column("Time", anchor=CENTER, width=20)
            schedule_list.column("Days", anchor=CENTER, width=20)
            schedule_list.column("Semester", anchor=CENTER, width=40)
            schedule_list.column("Year", anchor=CENTER, width=30)
            schedule_list.column("Credits", anchor=CENTER, width=30)

            #Courses Table labels
            schedule_list.heading("#0", text="", anchor=W)
            schedule_list.heading("CRN", text="CRN", anchor=W)
            schedule_list.heading("Title", text="Title", anchor=CENTER)
            schedule_list.heading("Department", text="Department",anchor=CENTER)
            schedule_list.heading("Instructor", text="Instructor", anchor=CENTER)
            schedule_list.heading("Time", text="Time",anchor=CENTER)
            schedule_list.heading("Days", text="Days", anchor=CENTER)
            schedule_list.heading("Semester", text="Semester", anchor=CENTER)
            schedule_list.heading("Year", text="Year", anchor=CENTER)
            schedule_list.heading("Credits", text="Credits", anchor=CENTER)
        
        #Exit Button Function
        def go_back():
            self.schedule.withdraw()
            utype.deiconify()

        #print schedule
        def get_schedule():
            records = self.user.getSchedule()
            for record in schedule_list.get_children():
                        schedule_list.delete(record)

            for i, record in enumerate(records, start=0):
                if i % 2 == 0:
                    schedule_list.insert(parent='', index='end', iid=i, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                else:
                    schedule_list.insert(parent='', index='end', iid=i, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
        
        #add course function
        def add_function(CRN):
            addCRN.destroy()
            register = self.user.registerCourseByCRN(CRN)

        #drop course function    
        def drop_function(CRN):
            dropCRN.destroy()
            drop = self.user.dropCourseByCRN(CRN)
        
        #add course window
        def add_window():
            global addCRN
            addCRN = Toplevel(self.schedule)
            addCRN.title("Add Course by CRN")
            addCRN.configure(bg="#D3D3D3")
            app_width = 400
            app_height = 200
            screen_width = addCRN.winfo_screenwidth()
            screen_height = addCRN.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            addCRN.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

            addCRN_frame = LabelFrame(addCRN, text="Add Course by CRN", font="calibri 12 ", bg="#D3D3D3")
            addCRN_frame.pack(padx=10, pady=10)

            crn_entry = Entry(addCRN_frame, font="calibri")
            crn_entry.pack(padx=10, pady=10)

            add_button = Button(addCRN, text="Add Course", font="calibri 12 ", bg="#D3D3D3", command=lambda: add_function( crn_entry.get()))
            add_button.pack(padx=20, pady=20)

        #drop course window
        def drop_window():
            global dropCRN
            dropCRN = Toplevel(self.schedule)
            dropCRN.title("Drop Course by CRN")
            dropCRN.configure(bg="#D3D3D3")
            app_width = 400
            app_height = 200
            screen_width = dropCRN.winfo_screenwidth()
            screen_height = dropCRN.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            dropCRN.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

            dropCRN_frame = LabelFrame(dropCRN, text="Drop Course by CRN", font="calibri 12 ", bg="#D3D3D3")
            dropCRN_frame.pack(padx=10, pady=10)

            crn_entry = Entry(dropCRN_frame, font="calibri")
            crn_entry.pack(padx=10, pady=10)

            drop_button = Button(dropCRN, text="Drop Course", font="calibri 12 ", bg="#D3D3D3", command=lambda: drop_function(crn_entry.get()))
            drop_button.pack(padx=20, pady=20)
        
        #construct schedule window
        self.schedule = Tk()
        schedule_layout(self.schedule)

        #construct cascade menu
        c_menu = Menu(self.schedule)
        command_menu(c_menu)

        style = ttk.Style()
        list_frame = Frame(self.schedule)
        list_scroll = Scrollbar(list_frame)
        schedule_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
        schedule_table(style, list_frame, list_scroll, schedule_list)

    def roster_page(self,utype):
        
        #roster window layout
        def roster_layout(frame):
            frame.title("Roster")
            frame.configure(bg="#D3D3D3")
            app_width = 1000
            app_height = 300
            screen_width = frame.winfo_screenwidth()
            screen_height = frame.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            frame.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            
            #Exit Button
            gb_btn = Button(frame, text = 'Go Back', font="calibri 12 ", width=7, command = go_back)
            gb_btn.pack(pady=10, side='bottom')
       
        #search function
        def search_roster(CRN, roster_list):
            searchRoster.destroy()
            
            roster = self.user.getRosterFromACourse(CRN)
            for i, record in enumerate(roster, start=0):
                
                if i % 2 == 0:
                    roster_list.insert(parent='', index='end', iid=i, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('evenrow',))
                else:
                    roster_list.insert(parent='', index='end', iid=i, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('oddrow',))
            
        #searchwindow
        def search_window():
            global searchRoster 
            searchRoster = Toplevel(self.roster)
            searchRoster.title("Search Course")
            searchRoster.configure(bg="#D3D3D3")
            app_width = 400
            app_height = 200
            screen_width = searchRoster.winfo_screenwidth()
            screen_height = searchRoster.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            searchRoster.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

            searchCRN_frame = LabelFrame(searchRoster, text="Enter CRN", font="calibri 12 ", bg="#D3D3D3")
            searchCRN_frame.pack(padx=10, pady=10)

            crn_entry = Entry(searchCRN_frame, font="calibri")
            crn_entry.pack(padx=10, pady=10)

            search_button = Button(searchRoster, text="Search Course", font="calibri 12 ", bg="#D3D3D3", command=lambda: search_roster(crn_entry.get(), roster_list))
            search_button.pack(padx=20, pady=20)
       
        #search menu
        def command_menu(s_menu):
            #command buttons
            self.roster.config(menu=s_menu)
            cmd = Menu(s_menu, tearoff=0)
            s_menu.add_cascade(label="Commands", menu=cmd)
            cmd.add_command(label="Search Course", command=search_window)

        #Exit Button Function
        def go_back():
            self.roster.withdraw()
            utype.deiconify()

        #roster table
        def roster_table(style, list_frame, list_scroll, roster_list):
            #Courses Table style
            style.theme_use('default')
            style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
            style.map('Treeview', background=[('selected', "blue")])

            #Table layout
            list_frame.pack(padx=10,pady=10, fill=X )
            list_scroll.pack(side=RIGHT, fill=Y)

            #Courses Table
            roster_list.pack( fill=X)
            list_scroll.config(command=roster_list.yview)

            #roster table content
            roster_list['columns'] = ("ID", "Name", "Surname", "Gradyear", "Major", "Email")
            roster_list.column("#0", width=0, stretch=NO)
            roster_list.column("ID", anchor=W, width=25)
            roster_list.column("Name", anchor=CENTER, width=40)
            roster_list.column("Surname", anchor=CENTER, width=40)
            roster_list.column("Gradyear", anchor=CENTER, width=25)
            roster_list.column("Major", anchor=CENTER, width=40)
            roster_list.column("Email", anchor=CENTER, width=40)

            #roster table labels
            roster_list.heading("#0", text="", anchor=W)
            roster_list.heading("ID", text="ID", anchor=W)
            roster_list.heading("Name", text="Name", anchor=CENTER)
            roster_list.heading("Surname", text="Surname", anchor=CENTER)
            roster_list.heading("Gradyear", text="Gradyear", anchor=CENTER)
            roster_list.heading("Major", text="Major", anchor=CENTER)
            roster_list.heading("Email", text="Email", anchor=CENTER)

        self.roster = Tk()
        roster_layout(self.roster)

        s_menu = Menu(self.roster)
        command_menu(s_menu)

        style = ttk.Style()
        list_frame = Frame(self.roster)
        list_scroll = Scrollbar(list_frame)
        roster_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
        roster_table(style, list_frame, list_scroll, roster_list)

    def user_page(self, utype):
        
        #student user window
        def stud_layout():
            self.userP.withdraw()
            #exit button function
            def go_back():
                s_frame.withdraw()
                self.userP.deiconify()

            #student user table display
            def stud_table(style, list_frame, list_scroll, stud_list):
                #Courses Table style
                style.theme_use('default')
                style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
                style.map('Treeview', background=[('selected', "blue")])

                #Table layout
                list_frame.pack(padx=10,pady=10, fill=X )
                list_scroll.pack(side=RIGHT, fill=Y)

                #Courses Table
                stud_list.pack( fill=X)
                list_scroll.config(command=stud_list.yview)

                #roster table content
                stud_list['columns'] = ("ID", "Name", "Surname", "Gradyear", "Major", "Email")
                stud_list.column("#0", width=0, stretch=NO)
                stud_list.column("ID", anchor=W, width=25)
                stud_list.column("Name", anchor=CENTER, width=40)
                stud_list.column("Surname", anchor=CENTER, width=40)
                stud_list.column("Gradyear", anchor=CENTER, width=25)
                stud_list.column("Major", anchor=CENTER, width=40)
                stud_list.column("Email", anchor=CENTER, width=40)

                #roster table labels
                stud_list.heading("#0", text="", anchor=W)
                stud_list.heading("ID", text="ID", anchor=W)
                stud_list.heading("Name", text="Name", anchor=CENTER)
                stud_list.heading("Surname", text="Surname", anchor=CENTER)
                stud_list.heading("Gradyear", text="Gradyear", anchor=CENTER)
                stud_list.heading("Major", text="Major", anchor=CENTER)
                stud_list.heading("Email", text="Email", anchor=CENTER)
            
            #add student function
            def add_Stud(id, name, surname, grad, major, email, ):
                addStud.destroy()
         
            #add student window
            def add_stud():

                global addStud
                addStud = Toplevel(s_frame)
                addStud.title("Add Student")
                addStud.configure(bg="#D3D3D3")
                app_width = 850
                app_height = 400
                screen_width = addStud.winfo_screenwidth()
                screen_height = addStud.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                addStud.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                addCourse_frame = LabelFrame(addStud, text="Student Information", font="calibri 12 ", bg="#D3D3D3")
                addCourse_frame.pack(fill="x", expand="yes", padx=20, side='top')

                id_txt = Label(addCourse_frame, text="ID", font="calibri 12 ", bg="#D3D3D3")
                id_txt.grid(row=0, column=0, padx=5, pady=5)
                id_entry= Entry(addCourse_frame, font="calibri")
                id_entry.grid(row=0, column=1, padx=5, pady=5)

                name_txt = Label(addCourse_frame, text="Name", font="calibri 12 ", bg="#D3D3D3")
                name_txt.grid(row=1, column=0, padx=5, pady=5)
                name_entry = Entry(addCourse_frame, font="calibri")
                name_entry.grid(row=1, column=1, padx=5, pady=5)

                surname_txt = Label(addCourse_frame, text="Surname", font="calibri 12 ", bg="#D3D3D3")
                surname_txt.grid(row=2, column=0, padx=5, pady=5)
                surname_entry = Entry(addCourse_frame, font="calibri")
                surname_entry.grid(row=2, column=1, padx=5, pady=5)

                grad_txt = Label(addCourse_frame, text="Gradyear", font="calibri 12 ", bg="#D3D3D3")
                grad_txt.grid(row=0, column=2, padx=5, pady=5)
                grad_entry = Entry(addCourse_frame, font="calibri")
                grad_entry.grid(row=0, column=3, padx=5, pady=5)

                major_txt = Label(addCourse_frame, text="Major", font="calibri 12 ", bg="#D3D3D3")
                major_txt.grid(row=1, column=2, padx=5, pady=5)
                major_entry = Entry(addCourse_frame, font="calibri")
                major_entry.grid(row=1, column=3, padx=5, pady=5)

                email_txt = Label(addCourse_frame, text="Email", font="calibri 12 ", bg="#D3D3D3")
                email_txt.grid(row=2, column=2, padx=5, pady=5)
                email_entry = Entry(addCourse_frame, font="calibri")
                email_entry.grid(row=2, column=3, padx=5, pady=5)
                
                add_button = Button(addStud, text="Add Student", font="calibri 12 ", bg="#D3D3D3", command=lambda: add_Stud(
                    id_entry.get(), name_entry.get(), surname_entry.get(), grad_entry.get(), major_entry.get(), email_entry.get()))
                add_button.pack(padx=5, pady=20)
                    
            #remove student function
            def rmv_Stud():
                rmvStud.destroy()
            
            #remove student window
            def rmv_stud():
                global rmvStud
                rmvStud = Toplevel(s_frame)
                rmvStud.title("Remove Student")
                rmvStud.configure(bg="#D3D3D3")
                app_width = 400
                app_height = 200
                screen_width = rmvStud.winfo_screenwidth()
                screen_height = rmvStud.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                rmvStud.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                rmv_frame = LabelFrame(rmvStud, text="Remove by CRN", font="calibri 12 ", bg="#D3D3D3")
                rmv_frame.pack(padx=10, pady=10)

                rmv_entry = Entry(rmv_frame, font="calibri")
                rmv_entry.pack(padx=10, pady=10)

                rmv_button = Button(rmvStud, text="Remove Student", font="calibri 12 ", bg="#D3D3D3", command = rmv_Stud)
                rmv_button.pack(padx=20, pady=20)
           
            #cmd menu
            def cmd_menu(c_menu):
                #command buttons
                s_frame.config(menu=c_menu)
                cmd = Menu(c_menu, tearoff=0)
                c_menu.add_cascade(label="Commands", menu=cmd)
                cmd.add_command(label="Add Student", command=add_stud)
                cmd.add_command(label="Remove Student", command=rmv_stud)
            
            global s_frame
            s_frame = Tk()
            s_frame.title("Student Users")
            s_frame.configure(bg="#D3D3D3")
            app_width = 1000
            app_height = 300
            screen_width = s_frame.winfo_screenwidth()
            screen_height = s_frame.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            s_frame.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

            style = ttk.Style()
            list_frame = Frame(s_frame)
            list_scroll = Scrollbar(list_frame)
            stud_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
            stud_table(style, list_frame, list_scroll, stud_list)
          
            exit_btn = Button(s_frame, text = 'Exit', font="calibri 12 ", width=7, command = go_back)
            exit_btn.pack(pady=10,side='bottom')


            c_menu = Menu(s_frame)
            cmd_menu(c_menu)
 
        #instructor user window
        def inst_layout():
            self.userP.withdraw()
            #exit button function
            def go_back():
                i_frame.withdraw()
                self.userP.deiconify()
               
            #Instructor user table display
            def inst_table(style, list_frame, list_scroll, inst_list):
                #Courses Table style
                style.theme_use('default')
                style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
                style.map('Treeview', background=[('selected', "blue")])

                #Table layout
                list_frame.pack(padx=10,pady=10, fill=X )
                list_scroll.pack(side=RIGHT, fill=Y)

                #instructor user Table
                inst_list.pack( fill=X)
                list_scroll.config(command=inst_list.yview)

                #instructor user table content
                inst_list['columns'] = ("ID", "Name", "Surname", "Title", "Hire Year", "Dept", "Email")
                inst_list.column("#0", width=0, stretch=NO)
                inst_list.column("ID", anchor=W, width=25)
                inst_list.column("Name", anchor=CENTER, width=40)
                inst_list.column("Surname", anchor=CENTER, width=40)
                inst_list.column("Title", anchor=CENTER, width=25)
                inst_list.column("Hire Year", anchor=CENTER, width=40)
                inst_list.column("Dept", anchor=CENTER, width=40)
                inst_list.column("Email", anchor=CENTER, width=40)

                #instructor user table labels
                inst_list.heading("#0", text="", anchor=W)
                inst_list.heading("ID", text="ID", anchor=W)
                inst_list.heading("Name", text="Name", anchor=CENTER)
                inst_list.heading("Surname", text="Surname", anchor=CENTER)
                inst_list.heading("Title", text="Title", anchor=CENTER)
                inst_list.heading("Hire Year", text="Hire Year", anchor=CENTER)
                inst_list.heading("Dept", text="Deptartment", anchor=CENTER)
                inst_list.heading("Email", text="Email", anchor=CENTER)
            
            #add instructor function
            def add_Inst(id, name, surname, title, hireyear, dept, email):
                addInst.destroy()
            
            #add instructor window
            def add_inst():

                global addInst
                addInst = Toplevel(i_frame)
                addInst.title("Add Instructor")
                addInst.configure(bg="#D3D3D3")
                app_width = 850
                app_height = 400
                screen_width = addInst.winfo_screenwidth()
                screen_height = addInst.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                addInst.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                addInst_frame = LabelFrame(addInst, text="Instructor Information", font="calibri 12 ", bg="#D3D3D3")
                addInst_frame.pack(fill="x", expand="yes", padx=20, side='top')

                id_txt = Label(addInst_frame, text="ID", font="calibri 12 ", bg="#D3D3D3")
                id_txt.grid(row=0, column=0, padx=5, pady=5)
                id_entry= Entry(addInst_frame, font="calibri")
                id_entry.grid(row=0, column=1, padx=5, pady=5)

                name_txt = Label(addInst_frame, text="Name", font="calibri 12 ", bg="#D3D3D3")
                name_txt.grid(row=1, column=0, padx=5, pady=5)
                name_entry = Entry(addInst_frame, font="calibri")
                name_entry.grid(row=1, column=1, padx=5, pady=5)

                surname_txt = Label(addInst_frame, text="Surname", font="calibri 12 ", bg="#D3D3D3")
                surname_txt.grid(row=2, column=0, padx=5, pady=5)
                surname_entry = Entry(addInst_frame, font="calibri")
                surname_entry.grid(row=2, column=1, padx=5, pady=5)

                title_txt = Label(addInst_frame, text="Title", font="calibri 12 ", bg="#D3D3D3")
                title_txt.grid(row=0, column=2, padx=5, pady=5)
                title_entry = Entry(addInst_frame, font="calibri")
                title_entry.grid(row=0, column=3, padx=5, pady=5)

                year_txt = Label(addInst_frame, text="Hire Year", font="calibri 12 ", bg="#D3D3D3")
                year_txt.grid(row=0, column=4, padx=5, pady=5)
                year_entry = Entry(addInst_frame, font="calibri")
                year_entry.grid(row=0, column=5, padx=5, pady=5)

                dept_txt = Label(addInst_frame, text="Department", font="calibri 12 ", bg="#D3D3D3")
                dept_txt.grid(row=1, column=2, padx=5, pady=5)
                dept_entry = Entry(addInst_frame, font="calibri")
                dept_entry.grid(row=1, column=3, padx=5, pady=5)

                email_txt = Label(addInst_frame, text="Email", font="calibri 12 ", bg="#D3D3D3")
                email_txt.grid(row=2, column=2, padx=5, pady=5)
                email_entry = Entry(addInst_frame, font="calibri")
                email_entry.grid(row=2, column=3, padx=5, pady=5)
                
                add_button = Button(addInst, text="Add Instructor", font="calibri 12 ", bg="#D3D3D3", command=lambda: add_Inst(id_entry.get(), name_entry.get(), surname_entry.get(), title_entry.get(), year_entry.get(), dept_entry.get(), email_entry.get()))
                add_button.pack(padx=5, pady=20)
                      
            #remove student window
            def rmv_inst():
                global rmvInst
                rmvInst = Toplevel(i_frame)
                rmvInst.title("Remove Instructor")
                rmvInst.configure(bg="#D3D3D3")
                app_width = 400
                app_height = 200
                screen_width = rmvInst.winfo_screenwidth()
                screen_height = rmvInst.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                rmvInst.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                rmv_frame = LabelFrame(rmvInst, text="Remove by CRN", font="calibri 12 ", bg="#D3D3D3")
                rmv_frame.pack(padx=10, pady=10)

                rmv_entry = Entry(rmv_frame, font="calibri")
                rmv_entry.pack(padx=10, pady=10)

                rmv_button = Button(rmvInst, text="Remove Instructor", font="calibri 12 ", bg="#D3D3D3")
                rmv_button.pack(padx=20, pady=20)
           
            #cmd menu
            def cmd_menu(c_menu):
                #command buttons
                i_frame.config(menu=c_menu)
                cmd = Menu(c_menu, tearoff=0)
                c_menu.add_cascade(label="Commands", menu=cmd)
                cmd.add_command(label="Add Instructor", command=add_inst)
                cmd.add_command(label="Remove Instructor", command=rmv_inst)

            global i_frame
            i_frame = Tk()
            i_frame.title("Instructor Users")
            i_frame.configure(bg="#D3D3D3")
            app_width = 1000
            app_height = 300
            screen_width = i_frame.winfo_screenwidth()
            screen_height = i_frame.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            i_frame.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
       
            style = ttk.Style()
            list_frame = Frame(i_frame)
            list_scroll = Scrollbar(list_frame)
            inst_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
            inst_table(style, list_frame, list_scroll, inst_list)
          
            exit_btn = Button(i_frame, text = 'Exit', font="calibri 12 ", width=7, command = go_back)
            exit_btn.pack(pady=10,side='bottom')


            c_menu = Menu(i_frame)
            cmd_menu(c_menu)
            
        #user list window
        def user_layout(u_frame):
            
            u_frame.title("Users")
            u_frame.configure(bg="#D3D3D3")
            app_width = 300
            app_height = 200
            screen_width = u_frame.winfo_screenwidth()
            screen_height = u_frame.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            u_frame.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            
            #Course Command Frame
            cmd_frame = LabelFrame(u_frame, text="Users", font="calibri 12 ", bg="#D3D3D3")
            cmd_frame.pack(pady=10)

            #COURSE COMMAND 
            student_btn = Button(cmd_frame, text="Student", command = stud_layout)
            student_btn.grid(row=0, column=0, padx=10, pady=10)
            inst_btn = Button(cmd_frame, text="Instructor", command = inst_layout)
            inst_btn.grid(row=0, column=1, padx=10, pady=10)
            #Exit Button
            gb_btn = Button(u_frame, text = 'Go Back', font="calibri 12 ", width=7, command = go_back)
            gb_btn.pack(pady=10, side='bottom')

        #exit button function
        def go_back():
            self.userP.withdraw()
            s_frame.withdraw()
            i_frame.withdraw()
            utype.deiconify()

        self.userP = Tk()
        user_layout(self.userP)
        
    def main_menu(self) -> None:
        # main Window dimensions
        ####################################################
        app_width = 425
        app_height = 300
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)

        self.main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        ####################################################

        # Main Window Text Widgets
        ####################################################
        self.title = Label(self.main, text="CURSE Registration System", bg="#D3D3D3", fg="black", font="calibri 24 bold", width=app_width, anchor=CENTER)
        self.title.pack()

        self.option_txt = Label(self.main, text="Select a user type", bg="#D3D3D3", fg="black", font="calibri 18 bold", width=app_width, anchor=CENTER)
        self.option_txt.pack(pady=10)
        ####################################################

        # Main Window Button frame widget
        ####################################################
        user_frame = LabelFrame(self.main, text="User Type", font="calibri 12 ", bg="#D3D3D3")
        user_frame.pack(pady=10)

        s_button = Button(user_frame, text="  Student  ", font="calibri 12 ", command=lambda: self.login_page("Student"))
        s_button.grid(row=0, column=0, padx=10, pady=10)

        i_button = Button(user_frame, text="  Instructor  ", font="calibri 12 ",command=lambda: self.login_page("Instructor"))
        i_button.grid(row=0, column=1, padx=10, pady=10)
        
        a_button = Button(user_frame, text="  Admin  ", font="calibri 12 ", command=lambda: self.login_page("Admin"))
        a_button.grid(row=0, column=2, padx=10, pady=10)

        exit_btn = Button(self.main, text = 'Exit', font="calibri 12 ", width=7, command = self.main.destroy)
        exit_btn.pack(pady=10, side='bottom')
        ####################################################

    def login_page(self, title) -> None:
        #Main window stays closed until exit button is pressed
        self.main.withdraw()
        
        #close student window and reopen main menu/Exit Button Function
        def main_menu():
            self.main.deiconify()
            self.login.withdraw()

        #Student login Window Dimensions
        def login_layout():

            def verify_login():
                verified = self.login_class.logIn(title, id_entry.get(), e_entry.get())
                login_status.delete(0,END)
                if verified is True:
                    self.cred = self.login_class.getCredentials()
                    login_status.insert(0,"Logged in")
                    self.create_user()
                    self.login.withdraw()
                else:
                    login_status.insert(0,"Wrong ID or email")

            # Login window
            self.login = Tk()
            self.login.title(title)
            self.login.configure(bg="#D3D3D3")
            app_width = 450
            app_height = 250
            screen_width = self.login.winfo_screenwidth()
            screen_height = self.login.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            self.login.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

            #Login frame w/widgets
            login_frame = LabelFrame(self.login, text="Login", font="calibri 12 ", bg="#D3D3D3")
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
            login_btn = Button(self.login, text="Login", font="calibri 12 ", width=7, command=verify_login) # **********
            login_btn.pack(side='top')
            
            #Login status/either successful or invalid
            login_status = Entry(self.login)
            login_status.pack(side='top',pady=5)

            #Exit Button
            exit_btn = Button(self.login, text = 'Exit', font="calibri 12 ", width=7, command = main_menu)
            exit_btn.pack(pady=10, side='bottom')

        login_layout()

    def student_page(self) -> None:

        def course_button():
            self.student.withdraw()
            self.courses_page(self.student)

        def schedule_button():
            self.student.withdraw()
            self.schedule_page(self.student)

        #logout button function
        def logout_button():
            self.login_class.logOut(self.user)
            self.student.destroy()
            self.main.deiconify()
            
            self.student.withdraw()
            self.courses_page(self.student)
        
        #Student Functions Window
        self.student = Tk()
        self.student.title("Student")
        self.student.configure(bg="#D3D3D3")
        app_width = 300
        app_height = 200
        screen_width = self.student.winfo_screenwidth()
        screen_height = self.student.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)
        self.student.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        s_frame = Frame(self.student, bg="#D3D3D3" )
        s_frame.pack(pady=30)

        #Student Function Window Widgets
        course_btn = Button(s_frame, text="Courses", font="calibri 12", command=course_button)
        course_btn.grid(row=0, column=0, padx=10, pady=10)
        schedule_btn = Button(s_frame, text="Schedule", font="calibri 12", command=schedule_button)
        schedule_btn.grid(row=0, column=1, padx=10, pady=10)

        #Logout Button
        exit_btn = Button(self.student, text = 'Logout', font="calibri 12 ", width=7, command = logout_button)
        exit_btn.pack(pady=10,side='bottom')
                    
    def admin_page(self) -> None:
       
        def course_button():
            self.admin.withdraw()
            self.courses_page(self.admin)

        def user_button():
            self.admin.withdraw()
            self.user_page(self.admin)

        def logout_button():
            self.login_class.logOut(self.user)
            self.admin.destroy()
            self.main.deiconify()

        def add_course_btn():
            
            def add_course_function(crn, title, dept, inst, time, day, sem, year, cred):
                addCourse.destroy()
    
            addCourse = Toplevel(self.admin)
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

            add_button = Button(addCourse, text="Add Course", font="calibri 12 ", bg="#D3D3D3", command=lambda: add_course_function(
                CRN_entry1.get(), title_entry1.get(), dept_entry1.get(), inst_entry1.get(), time_entry1.get(), day_entry1.get(), sem_entry1.get(), year_entry1.get(), cred_entry1.get()))
            add_button.pack(padx=5, pady=20)
        
        def rmv_course_btn():
            
            def rmv_course_function(crn):
                rmvCourse.destroy()
            rmvCourse = Toplevel(self.admin)
            rmvCourse.title("Remove Course")
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

            rmv_button = Button(rmvCourse, text="Remove Course", font="calibri 12 ", bg="#D3D3D3", command= lambda: rmv_course_function(rmv_entry.get()))
            rmv_button.pack(padx=20, pady=10, side='bottom')
        
        #Admin Function Window
        self.admin = Tk()
        self.admin.title("Admin")
        self.admin.configure(bg="#D3D3D3")
        app_width = 300
        app_height = 300
        screen_width = self.admin.winfo_screenwidth()
        screen_height = self.admin.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)
        self.admin.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        i_frame = Frame(self.admin, bg="#D3D3D3" )
        i_frame.pack(pady=30)

        #Admin function window widgets
        course_btn = Button(i_frame, text="Courses", font="calibri 12", command=course_button)
        course_btn.grid(row=0, column=0, padx=10, pady=10)
        user_btn = Button(i_frame, text="Users", font="calibri 12", command=user_button)
        user_btn.grid(row=0, column=1, padx=10, pady=10)
        add_btn = Button(i_frame, text="Add Courses", font="calibri 12", command=add_course_btn)
        add_btn.grid(row=1, column=0, padx=10, pady=10)
        rmv_btn = Button(i_frame, text="Remove Courses", font="calibri 12", command=rmv_course_btn)
        rmv_btn.grid(row=1, column=1, padx=10, pady=10)
        #Logout Button
        exit_btn = Button(self.admin, text = 'Logout', font="calibri 12 ", width=7, command = logout_button)
        exit_btn.pack(pady=10,side='bottom')

    def instructor_page(self) -> None:

        #course button function
        def course_button():
            self.instructor.withdraw()
            self.courses_page(self.instructor)

        #schedule button function
        def schedule_button():
            self.instructor.withdraw()
            
           #schedule table display
            def schedule_table(style, list_frame, list_scroll, schedule_list):
                #Courses Table style
                style.theme_use('default')
                style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
                style.map('Treeview', background=[('selected', "blue")])

                #Table layout
                list_frame.pack(padx=10,pady=10, fill=X )
                list_scroll.pack(side=RIGHT, fill=Y)

                #Courses Table
                schedule_list.pack( fill=X)
                list_scroll.config(command=schedule_list.yview)

                #Courses Table Content
                schedule_list['columns'] = ("CRN", "Title", "Department", "Instructor", "Time", "Days", "Semester", "Year", "Credits")
                schedule_list.column("#0", width=0, stretch=NO)
                schedule_list.column("CRN", anchor=W, width=25)
                schedule_list.column("Title", anchor=CENTER, width=125)
                schedule_list.column("Department", anchor=CENTER, width=20)
                schedule_list.column("Instructor", anchor=CENTER, width=75)
                schedule_list.column("Time", anchor=CENTER, width=20)
                schedule_list.column("Days", anchor=CENTER, width=20)
                schedule_list.column("Semester", anchor=CENTER, width=40)
                schedule_list.column("Year", anchor=CENTER, width=30)
                schedule_list.column("Credits", anchor=CENTER, width=30)

                #Courses Table labels
                schedule_list.heading("#0", text="", anchor=W)
                schedule_list.heading("CRN", text="CRN", anchor=W)
                schedule_list.heading("Title", text="Title", anchor=CENTER)
                schedule_list.heading("Department", text="Department",anchor=CENTER)
                schedule_list.heading("Instructor", text="Instructor", anchor=CENTER)
                schedule_list.heading("Time", text="Time",anchor=CENTER)
                schedule_list.heading("Days", text="Days", anchor=CENTER)
                schedule_list.heading("Semester", text="Semester", anchor=CENTER)
                schedule_list.heading("Year", text="Year", anchor=CENTER)
                schedule_list.heading("Credits", text="Credits", anchor=CENTER)

            #Exit Button Function
            def go_back(utype):
                self.schedule.withdraw()
                utype.deiconify()
           
            #schedule table display
            def schedule_table(style, list_frame, list_scroll, schedule_list):
                #Courses Table style
                style.theme_use('default')
                style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
                style.map('Treeview', background=[('selected', "blue")])

                #Table layout
                list_frame.pack(padx=10,pady=10, fill=X )
                list_scroll.pack(side=RIGHT, fill=Y)

                #Courses Table
                schedule_list.pack( fill=X)
                list_scroll.config(command=schedule_list.yview)

                #Courses Table Content
                schedule_list['columns'] = ("CRN", "Title", "Department", "Instructor", "Time", "Days", "Semester", "Year", "Credits")
                schedule_list.column("#0", width=0, stretch=NO)
                schedule_list.column("CRN", anchor=W, width=25)
                schedule_list.column("Title", anchor=CENTER, width=125)
                schedule_list.column("Department", anchor=CENTER, width=20)
                schedule_list.column("Instructor", anchor=CENTER, width=75)
                schedule_list.column("Time", anchor=CENTER, width=20)
                schedule_list.column("Days", anchor=CENTER, width=20)
                schedule_list.column("Semester", anchor=CENTER, width=40)
                schedule_list.column("Year", anchor=CENTER, width=30)
                schedule_list.column("Credits", anchor=CENTER, width=30)

                #Courses Table labels
                schedule_list.heading("#0", text="", anchor=W)
                schedule_list.heading("CRN", text="CRN", anchor=W)
                schedule_list.heading("Title", text="Title", anchor=CENTER)
                schedule_list.heading("Department", text="Department",anchor=CENTER)
                schedule_list.heading("Instructor", text="Instructor", anchor=CENTER)
                schedule_list.heading("Time", text="Time",anchor=CENTER)
                schedule_list.heading("Days", text="Days", anchor=CENTER)
                schedule_list.heading("Semester", text="Semester", anchor=CENTER)
                schedule_list.heading("Year", text="Year", anchor=CENTER)
                schedule_list.heading("Credits", text="Credits", anchor=CENTER)
        
            #print schedule
            def get_schedule():
                records = self.user.getSchedule()
                for record in schedule_list.get_children():
                            schedule_list.delete(record)

                for i, record in enumerate(records, start=0):
                    if i % 2 == 0:
                        schedule_list.insert(parent='', index='end', iid=i, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                    else:
                        schedule_list.insert(parent='', index='end', iid=i, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
           
            #schedule window
            def schedule_layout(frame):
                frame.title("Schedule")
                frame.configure(bg="#D3D3D3")
                app_width = 1000
                app_height = 300
                screen_width = frame.winfo_screenwidth()
                screen_height = frame.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                frame.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                
                #Exit Button
                gb_btn = Button(frame, text = 'Go Back', font="calibri 12 ", width=7, command=lambda: go_back(self.instructor))
                gb_btn.pack(pady=10, side='bottom')
                #Print Schedule
                get_btn = Button(frame, text="Print Schedule", font="calibri 12 ", width=7, command=get_schedule)
                get_btn.pack(ipadx=18, pady=10, side = 'bottom')
                
            #construct schedule window
            self.schedule = Tk()
            schedule_layout(self.schedule)

            style = ttk.Style()
            list_frame = Frame(self.schedule)
            list_scroll = Scrollbar(list_frame)
            schedule_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
            schedule_table(style, list_frame, list_scroll, schedule_list)

        #roster button function       
        def roster_button():
            self.instructor.withdraw()
            self.roster_page(self.instructor)

        #logout button function
        def logout_button():
            self.login_class.logOut(self.user)
            self.instructor.destroy()
            self.main.deiconify()

        #Instructor Functions Window
        self.instructor = Tk()
        self.instructor.title("Instructor")
        self.instructor.configure(bg="#D3D3D3")
        app_width = 300
        app_height = 200
        screen_width = self.instructor.winfo_screenwidth()
        screen_height = self.instructor.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)
        self.instructor.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        i_frame = Frame(self.instructor, bg="#D3D3D3" )
        i_frame.pack(pady=30)

        #Instructor function window widgets
        course_btn = Button(i_frame, text="Courses", font="calibri 12", command=course_button)
        course_btn.grid(row=0, column=0, padx=10, pady=10)
        schedule_btn = Button(i_frame, text="Schedule", font="calibri 12", command=schedule_button)
        schedule_btn.grid(row=0, column=1, padx=10, pady=10)
        roster_btn = Button(i_frame, text="Roster", font="calibri 12", command=roster_button)
        roster_btn.grid(row=0, column=2, padx=10, pady=10)

        #Logout Button
        exit_btn = Button(self.instructor, text = 'Logout', font="calibri 12 ", width=7, command = logout_button)
        exit_btn.pack(pady=10,side='bottom')

GUI = MainApp()