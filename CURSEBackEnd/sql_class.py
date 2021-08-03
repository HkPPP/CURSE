#Sql class done by Hank Pham(80%) and Kevin Huang(20%)

import sqlite3

class sql_functions:
    """This class is used for executing SQL queries using Python."""

    def __init__(self, path="schooldatabase.db") -> None:
        """Connect to database and create a cursor."""

        self.__database = path 
        self.con = sqlite3.connect(self.__database) 
        self.cur = self.con.cursor() 

    def __del__(self):
        """Delete cursor and close database when destructed."""
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()

    def set_database_path(self, path):
        """Set database path ot name."""
        self.__database = path

    def create_table(self, name, column):
        """CREATE TABLE [NAME] ([COLUMN]))"""

        self.command = f"CREATE TABLE {name} ({column});"
        self.exec_and_commit(self.command)

    def insert_into_table_values(self, table, value):
        """INSERT INTO [TABLE] VALUES ([VALUE])"""

        self.command = f"INSERT INTO {table} values ({value});"
        self.exec_and_commit(self.command)

    def delete_from_table_where(self, table, column, condition):
        """DELETE FROM [TABLE] WHERE [COLUMN] = [CONDITION]"""

        self.command = f"DELETE from {table} where {column} = {condition};"
        self.exec_and_commit(self.command)

    def select_from_where(self, table, row, column, condition):
        """SELECT [ROW] FROM [TABLE] WHERE [COLUMN] = [CONDITION]"""

        self.command = f"SELECT {row} from {table} where {column} = {condition};"
        self.exec_and_commit(self.command)
        self.result = self.cur.fetchall()
        return self.result
        
    def select_from(self, table, row):
        """SELECT [ROW] FROM [TABLE]"""

        self.command = f"SELECT {row} from {table};"
        self.exec_and_commit(self.command)
        self.result = self.cur.fetchall()
        return self.result

    def custom_cmd(self, cmd):
        """Execute and commit a custom SQL command."""
        self.exec_and_commit(cmd)

    def exec_and_commit(self, cmd):
        """Execute SQL command and update the database."""
        self.cur.execute(cmd)
        self.con.commit()

    def get_last_rowID(self, table):
        """Get the number of rows ever created."""

        #Note: Even if some rows are deleted, MAX(ROWID) still returns the maximum number ever of rows in the table 
        self.command = f"SELECT MAX(ROWID) from {table};"
        self.cur.execute(self.command)
        self.result = self.cur.fetchall()
        return self.result[0][0]

    def get_partial_matches(self, table, row, column, condition):
        """Return an array of rows that contain partial matches of a word."""
        
        self.command = f"SELECT {row} from {table} where {column} like {condition};"
        self.cur.execute(self.command)
        self.result = self.cur.fetchall()
        return self.result

    def cross_join_table(self, table1, table2):
        """SELECT FROM [TABLE1] CROSS JOIN [TABLE2] """
        self.command = f"SELECT from {table1} CROSS JOIN {table2}"
        self.exec_and_commit(self.command)


    def select_from_where_in(self, table1, row1, column1, table2, row2, column2, condition):
        """SELECT [row1] FROM [table1] WHERE [column1] IN (SELECT [row2] FROM [table2] WHERE [column2] = [condition])"""
        self.command = f"SELECT {row1} FROM {table1} WHERE {column1} IN (SELECT {row2} FROM {table2} WHERE {column2} = {condition})"
        self.cur.execute(self.command)
        self.result = self.cur.fetchall()
        return self.result





















