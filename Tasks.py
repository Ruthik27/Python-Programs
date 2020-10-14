import pymsql
from tkinter import *
from tkinter import messagebox

def search():
    try:
        con = pymsql.connect(user='root', password='', host='localhost', database='db')
        cur = con.cursor()
        sql = "select * from student where Rollno='%s'"%Rollno.get()
        cur.execute(sql)
        result = cur.fetchone()
        name.set(result[1])
        age.set(result[2])
        e1.configure(state = 'disabled')
        con.close()
    except:
        messagebox.showinfo('No Data','No such data available')
        clear()
