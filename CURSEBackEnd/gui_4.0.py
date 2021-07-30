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

        #Main App Window
        self.main = Tk()
        self.main.title("CURSE")
        self.main.configure(bg="#D3D3D3")

        

        self.main_menu()

        self.main.mainloop()


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
            login_btn = Button(self.login, text="Login", font="calibri 12 ", width=7, command=verify_login ) # **********
            login_btn.pack(side='top')
            
            #Login status/either successful or invalid
            login_status = Entry(self.login)
            login_status.pack(side='top',pady=5)

            #Exit Button
            exit_btn = Button(self.login, text = 'Exit', font="calibri 12 ", width=7, command = main_menu)
            exit_btn.pack(pady=10, side='bottom')

        login_layout()


    def student_page(self) -> None:
        pass

    def admin_page(self) -> None:
        pass

    def instructor_page(self) -> None:
        pass

    def courses_page(self) -> None:
        pass



GUI = MainApp()