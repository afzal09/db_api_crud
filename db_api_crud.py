import sqlite3
from sqlite3 import Error, OperationalError
import typing
class operations():
    def __init__(self):
            try:
                self.conn = sqlite3.connect('students.db')
                self.cur = self.conn.cursor()
                self.cur.execute('create table students(id integer primary key not null , name varchar(50), contact integer(20));')
            except OperationalError as e:
                print(e)

    def create_record(self,name: str, contact: int):
        try:
            self.cur.execute(f'insert into students(name,contact) values("{name}","{contact}");')
            print("#--- inserted one record succesfully ---#")
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
    
    def read_record(self,name:str):
        try:
            res = self.cur.execute(f"select * from students where name='{name}';")
            print(res.fetchone())
        except OperationalError as e:
            print(e)

    def update_record(self,old_name:str, old_contact:int, new_name:str, new_contact:int):
        try:
            res = self.cur.execute(f'update students set name="{new_name}" ,contact="{new_contact}" where name="{old_name}" and contact="{old_contact}";')
            print("#--- Updated one record ---# \n","\tchanges applied\n",f"{old_name} ---> {new_name}",f"{old_contact}--->{new_contact}")
            self.conn.commit()
        except Error as e:
            print(e)

    def delete_record(self,name:str):
        try:
            res = self.cur.execute(f"delete from students where name='{name}'")
            print(f"#--- record deleted for {name}")
            self.conn.commit()
        except Error as e:
            print(e)

    def close(self):
        self.cur.close()