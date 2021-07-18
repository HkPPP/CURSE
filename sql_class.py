import sqlite3



class sql_functions:
    def __init__(self, path) -> None:
        self.con = sqlite3.connect(path) 
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()

    def add_func(self, table, value):
        self.command = f"INSERT into {table} values{value};"
        self.exec_and_commit(self.command)

    def delete_func(self, table, column, object):
        self.command = f"DELETE from {table} where {column} is {object};"
        self.exec_and_commit(self.command)

    def select_func(self, table, column, object):
        self.command = f"SELECT from {table} where {column} is {object};"
        self.exec_and_commit(self.command)

    def custom_cmd(self, cmd):
        self.exec_and_commit(cmd)

    def exec_and_commit(self, cmd):
        self.cur.execute(cmd)
        self.con.commit()