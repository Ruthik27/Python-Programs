import pymsql   #for database
from tkinter import *    # for cursor
from tkinter import messagebox  # same for window operation

def search():
    try:
        con = pymsql.connect(user='root', password='', host='localhost', database='db')  #connection
        cur = con.cursor()    #same
        sql = "select * from student where Rollno='%s'"%Rollno.get()   #querry tht should be performed
        cur.execute(sql)     #execution
        result = cur.fetchone()   #getting one value
        name.set(result[1])
        age.set(result[2])
        e1.configure(state = 'disabled')
        con.close()
    except:
        messagebox.showinfo('No Data','No such data available')
        clear()

def clear():   # to clear values
    Rollno.set('') #setting to null
    name.set('')
    age.set('')
    e1.configure(state='normal')

def add():  # using the same just changing querry and messagebox info
    try:
        con = pymsql.connect(user='root', password='', host='localhost', database='db')
        cur = con.cursor()
        sql = "insert into student values('%s','%s','%s')" %(Rollno.get(),name.get(),age.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Rrcord saved...')
    except:
        messagebox.showinfo('Error','Error in data entry...')

def update(): # using the same just changing querry and messagebox info
    try:
        con = pymsql.connect(user='root', password='', host='localhost', database='db')
        cur = con.cursor()
        sql = "update student set name = '%s', age = '%s' where Rollno = '%s'" %(name.get(), age.get(), Rollno.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Rrcord updated...')
    except:
        messagebox.showinfo('Error','Error occured...')

def delete(): # using the same just changing querry and messagebox info
    try:
        con = pymsql.connect(user='root', password='', host='localhost', database='db')
        cur = con.cursor()
        sql = "delete from student where Rollno = '%s'" %(Rollno.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Rrcord deleted...')
    except:
        messagebox.showinfo('Error','Error occured...')
