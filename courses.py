from tkinter import *
import sqlite3


#create new database
conn = sqlite3.connect('courses.db')

#cursor
cursor = conn.cursor()

#courses table
sql_command = ("""CREATE TABLE Courses (
        Title       text        PRIMARY KEY     NOT NULL,
	    CRN			int     NOT NULL,
	    dept 		text    NOT NULL,
	    instructor 	text    NOT NULL,
	    classTime	int     NOT NULL,
	    days		text    NOT NULL,
	    semester	text    NOT NULL,
	    courseYear 	int     NOT NULL,
	    credits	 	int     NOT NULL)
        ;""")

cursor.execute(sql_command)

conn.commit()

conn.close()